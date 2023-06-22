import os
import subprocess
import threading
import datetime
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
            processos.append(p)
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

def listar_pastas_e_arquivos(diretorio):
    conteudo = []
    for item in os.listdir(diretorio):
        item_caminho = os.path.join(diretorio, item)
        if os.path.isdir(item_caminho):
            arq = {"tipo": "pasta",
                   "nome": item,
                   "caminho": item_caminho}
        else:
            arq = {"tipo": "arquivo",
                   "nome": item,
                   "caminho": item_caminho,
                   "tamanho": os.path.getsize(item_caminho),# em bytes
                   "dtIns" : str(datetime.datetime.fromtimestamp(os.path.getctime(item_caminho))),
                   "dtMod" : str(datetime.datetime.fromtimestamp(os.path.getmtime(item_caminho))),
                   "perm" : oct(os.stat(item_caminho).st_mode)[-3:]}
        conteudo.append(arq)
    return conteudo

def grava_dados():
    diretorio = "/home/phsecchi/GitHub/dashboardb"
    pid = aquisicao_dados_processos()[-1]
    while True:
        Dados = {"Particoes": obter_informacoes_particoes(),
                 "Processos": aquisicao_dados_processos(),
                 "ArqProcess": obter_arquivos_em_uso(pid),
                 "PastaArq" : listar_pastas_e_arquivos(diretorio),
                }
        #Escreve Dados em um arquivo JSON       
        with open("Dados.json","w") as arquivo:
            json.dump(Dados,arquivo,indent= 4)
        
        #Aguarda 5 seg
        time.sleep(5)

#Define a thread e inicia
thr_aq_dados = threading.Thread(target= grava_dados)
thr_aq_dados.start()