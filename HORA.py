import ctypes #Fornece tipos de dados compativeis com C permitindo chamar funções em DLLs, nesse caso a função SetSystemTime que muda a hora do sistema. (Método de baixo nível).
import time #Fornece funções relacionadas à conversão de strings de "tempo".
import datetime #Obtem a hora do sistema.
import tkinter as tk #Interface gráfica.
import tkinter.font as font #Fonte do texto para a interface gráfica.
import requests #Faz requisições HTTP, neste caso um GET para obter a hora do servidor.
import os #Muda a hora do sistema. (Método de alto nível).


url = "https://www.timeapi.io/api/Time/current/zone?timeZone=America/Sao_Paulo" #URL da API que fornece a hora do servidor

def change_system_time(): #Função que muda a hora do sistema para a hora do servidor (horário de Brasília)
    response = requests.request("GET", url) #Faz a requisição GET
    checkresponse = response.json() #Transforma a resposta em um dicionário
    horaminuto = checkresponse["time"] #Pega a hora e os minutos
    segundos = checkresponse["seconds"] #Pega os segundos
    Horario = (f"{horaminuto}"":"f"{segundos}") #Junta a hora, os minutos e os segundos
    data = checkresponse["date"].split("/") #Pega a data completa e separa os valores em uma lista
    d2 = data
    d3 = str(d2[1] + "-" + d2[0] + "-" + d2[2]) #Junta os valores da lista em uma string no formato dia-mês-ano
    
    try:
        os.system('time ' + Horario) #Muda a hora do sistema
        os.system('date ' + d3) #Muda a data do sistema
        print("Horario mudado com sucesso.") #Mensagem de sucesso
        stop_loop() #Para o loop
    except:
        print("ERRO AO MUDAR A HORA") #Mensagem de erro

def stop_loop(): #Função que para o loop
    global running
    running = False
    label_var.set("O programa está DESLIGADO")

def start_loop(): #Função que inicia o loop
    global running
    running = True
    label_var.set("O programa está sendo EXECUTADO")
    update_time()


def update_time(): #Função que verifica a hora do sistema e muda a hora do sistema se necessário
    if running:
        #Gera uma variavel com a hora atual e outra com a hora que é utilizada como parametro para mudar a hora do sistema
        today_datetime = datetime.datetime.today()
        time2 = today_datetime.strftime("%d-%m-%Y %H:%M:%S")
        time3 = (time2[0:10] + " 23:50:" + time2[17:20])


        def set_system_time(new_time): #Função que muda a hora do sistema com ctypes
            # Converte a hora à um formato que pode ser usado pela função SetSystemTime
            system_time = (ctypes.c_ushort * 8)()
            system_time[0] = new_time.tm_year
            system_time[1] = new_time.tm_mon
            system_time[2] = new_time.tm_wday
            system_time[3] = new_time.tm_mday
            system_time[4] = new_time.tm_hour
            system_time[5] = new_time.tm_min
            system_time[6] = new_time.tm_sec
            system_time[7] = 0

            # Muda a hora do sistema
            ret = ctypes.windll.kernel32.SetSystemTime(ctypes.pointer(system_time))

            # Olha se a mudança de horário deu certo
            if ret == 0:
                print("ERRO")
            else:
                print("Horario mudado com sucesso.")
                restart_loop() #Reinicia o loop

        if time2 == time3: #Se a hora atual for igual a hora que deve ser mudada, muda a hora do sistema
            new_time = time.strptime(f"{time2[0:10]} 01:50:00", "%d-%m-%Y %H:%M:%S")
            new_time = time.mktime(new_time) #Converte new_time de datetime para UNIX timestamp para poder ser usado pela função SetSystemTime 
            new_time += 60*60*24  #Adiciona 1 dia para equivaler a hora do servidor
            new_time = time.localtime(new_time) #Faz a conversão de volta para datetime
            set_system_time(new_time) #Aciona a função que muda a hora do sistema
        root.after(10 * 100, update_time) #Verifica a hora do sistema a cada 1 segundo


def restart_loop(): #Função que reinicia o loop
    global running
    running = False
    time.sleep(1)
    running = True
    update_time()


root = tk.Tk() #Cria a interface gráfica

MyFont = font.Font(family='Mona-Sans-Bold') #Define a fonte do texto da interface gráfica

#Define as propriedades da interface gráfica (icone, titulo, tamanho)
root.iconbitmap("Insira o diretório do arquivo myIcon.ico\\myIcon.ico")
root.title('Horario Automático')
root.geometry('275x130')

running = True
label_var = tk.StringVar()
label_var.set("O programa está sendo EXECUTADO")
start_loop()

label = tk.Label(root, textvariable=label_var) #Cria um label que mostra se o programa está sendo executado ou não
label.pack()

start_button = tk.Button(root, text="Iniciar", command=start_loop, fg='#159703', padx = 21, pady = 2, font=MyFont) #Cria um botão que inicia o loop
start_button.pack()

stop_button = tk.Button(root, text="Parar", command=stop_loop, fg='#EF3407', padx = 23, pady = 2, font=MyFont) #Cria um botão que para o loop
stop_button.pack()

button = tk.Button(root, text="Mudar para Horário Local", command=change_system_time, fg='#000FFF', pady = 5, font=MyFont) #Cria um botão que muda a hora do sistema para a hora local
button.pack()

root.mainloop()