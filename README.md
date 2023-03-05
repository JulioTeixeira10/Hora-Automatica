Este script é um programa Python que busca a hora atual de uma API e altera a hora do sistema para coincidir com ela. Ele também possui uma interface gráfica do usuário construída com tkinter, permitindo que os usuários iniciem e interrompam o processo de atualização do tempo.

Bibliotecas Utilizadas
ctypes: fornece tipos de dados compatíveis com C, permitindo que funções em DLLs sejam chamadas, neste caso, a função SetSystemTime que altera o tempo do sistema.
time: fornece funções relacionadas à conversão de strings de tempo.
datetime: recupera o tempo do sistema.
tkinter: fornece a interface gráfica do usuário.
tkinter.font: fornece a fonte de texto para a interface gráfica do usuário.
requests: faz solicitações HTTP, neste caso, uma solicitação GET para obter o tempo do servidor.
os: altera o tempo do sistema (método de alto nível).

Como Funciona
Quando o programa é iniciado, ele busca a hora atual da API especificada, extrai os valores de hora, minuto e segundo e os salva como strings. Em seguida, ele extrai a data em um formato completo e a salva como uma lista. Os valores da lista de data são unidos em uma string no formato "dia-mês-ano".

O programa então entra em um loop, verificando a hora atual em relação à hora de atualização desejada. Se a hora atual corresponder à hora de atualização, o tempo do sistema é atualizado com o novo tempo. O programa aguarda um segundo e, em seguida, repete o loop.

O programa possui uma interface gráfica do usuário com dois botões: Iniciar e Parar. O usuário pode clicar em Iniciar para iniciar o processo de atualização do tempo e em Parar para encerrá-lo.

Executando o Programa
Para executar o programa, verifique se você tem o Python instalado em sua máquina. Em seguida, execute o seguinte comando em seu terminal:
python time_change.py

Nota
Este programa foi feito apenas para sistemas Windows 10. Se você estiver usando um sistema operacional diferente, precisará modificar o código para que funcione com seu sistema.



