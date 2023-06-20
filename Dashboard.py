import subprocess
import threading
import time
import json


def obter_informacoes_particoes():
    informacoes_particoes = []
    comando = "sudo fdisk -l"

    # Executar o comando e capturar a saída
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    saida = resultado.stdout

    # Processar a saída do comando
    linhas = saida.split('\n')
    for linha in linhas:
        if linha.startswith('/dev/sd'):
            informacoes = {}

            # Extração das informações desejadas
            particao_info = linha.split()
            informacoes = "Part" + particao_info[0] + "Tamanho" + particao_info[4]

            informacoes_particoes.append(informacoes)

    return informacoes_particoes

def grava_dados():
    while True:
        Dados = {"Particoes": obter_informacoes_particoes()
                }
        #Escreve Dados em um arquivo JSON       
        with open("Dados.json","w") as arquivo:
            json.dump(Dados,arquivo,indent= 4)
        
        #Aguarda 5 seg
        time.sleep(5)

#Define a thread e inicia
thr_aq_dados = threading.Thread(target= grava_dados)
thr_aq_dados.start()