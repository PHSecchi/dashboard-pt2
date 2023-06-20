import os
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

def aquisicao_dados_processos():
    # Carrega todos os diretorios que tem como nome um numero inteiro, ou seja, sao diretorios de processos
    processos = []
    for p in os.listdir('/proc'):
        if p.isdigit():
            obter_arquivos_em_uso(p)
            processos.append({"Processo_"+p : obter_arquivos_em_uso(p)})
    return processos

            
def obter_arquivos_em_uso(pid):
    arquivos_em_uso = []
    comando = f"sudo lsof -p {pid}"

    # Executar o comando e capturar a saída
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    saida = resultado.stdout

    # Processar a saída do comando
    linhas = saida.split('\n')
    for linha in linhas[1:]:
        if linha:
            informacoes_arquivo = linha.split()
            arquivo_em_uso = {
                'nome': informacoes_arquivo[-1],
                'tipo': informacoes_arquivo[4],
                'usuario': informacoes_arquivo[2],
                'pid': informacoes_arquivo[1],
                'dispositivo': informacoes_arquivo[0]
            }
            arquivos_em_uso.append(arquivo_em_uso)

    return arquivos_em_uso

def grava_dados():
    while True:
        Dados = {"Particoes": obter_informacoes_particoes(),
                 "Processos": aquisicao_dados_processos()
                }
        #Escreve Dados em um arquivo JSON       
        with open("Dados.json","w") as arquivo:
            json.dump(Dados,arquivo,indent= 4)
        
        #Aguarda 5 seg
        time.sleep(5)

#Define a thread e inicia
thr_aq_dados = threading.Thread(target= grava_dados)
thr_aq_dados.start()