import os
import subprocess
import threading
import datetime
import time
import json


def obter_informacoes_particoes():
    info_part = []
    comando = "sudo fdisk -l"

    # Executar o comando e capturar a saída
    retorno = subprocess.run(comando, shell=True, capture_output=True, text=True).stdout
    
    # Processar a saída do comando
    linhas = retorno.split('\n')
    for linha in linhas:
        if linha.startswith('/dev/sd'):
            informacoes = {}

            # Extração das informações
            part_info = linha.split()
            informacoes = {"Part" : part_info[0],  "Tamanho" : part_info[4]}

            info_part.append(informacoes)

    return info_part

def aquisicao_nr_processos ():
    processos = []
    for p in os.listdir('/proc'):
        if p.isdigit():
            processos.append(p)
    return processos

def aquisicao_dados_processos():
    # Carrega todos os diretorios que tem como nome um numero inteiro, ou seja, sao diretorios de processos
    processos = aquisicao_nr_processos()
    proc = []
    #Abre o arquivo "status" de todos os processos e retira as informacoes necessaria 
    for id_proc in processos:
        with open(f"/proc/{id_proc}/status", 'r') as arquivo:
            status = arquivo.readlines()
            memo = 0
        #Percorre o arquivo status de cada processo procurando pelas informacoe necessarias
        for s in status:
            if s.startswith('Pid:'):
                pid = s.split('\t')[1].strip() 
            if s.startswith('Name:'):
                name = s.split('\t')[1].strip() 
            
        processo = {"PID": pid,
                    "Nome": name}
        
        proc.append ({"Processo": processo})

    return proc
            
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
        caminho_item = os.path.join(diretorio, item)
        if os.path.isdir(caminho_item):
            arq = {"tipo": "pasta",
                   "nome": item,
                   "caminho": caminho_item,
                   "tamanho": os.path.getsize(caminho_item),# em bytes
                   "dtIns" : str(datetime.datetime.fromtimestamp(os.path.getctime(caminho_item)).date()),#data de criacao    
                   "dtMod" : str(datetime.datetime.fromtimestamp(os.path.getmtime(caminho_item)).date()),#data de modificacao
                   "perm" : oct(os.stat(caminho_item).st_mode)[-3:]}
        else:
            arq = {"tipo": "arquivo",
                   "nome": item,
                   "caminho": caminho_item,
                   "tamanho": os.path.getsize(caminho_item),# em bytes
                   "dtIns" : str(datetime.datetime.fromtimestamp(os.path.getctime(caminho_item)).date()),#data de criacao    
                   "dtMod" : str(datetime.datetime.fromtimestamp(os.path.getmtime(caminho_item)).date()),#data de modificacao
                   "perm" : oct(os.stat(caminho_item).st_mode)[-3:]}
        conteudo.append(arq)
         # PERMICOES
        # 0: Sem permissao de leitura, gravacao ou execucao.
        # 1: Permissao de execucao apenas.
        # 2: Permissao de gravacao apenas.
        # 3: Permissao de gravacao e execucao.
        # 4: Permissao de leitura apenas.
        # 5: Permissao de leitura e execucao.
        # 6: Permissao de leitura e gravacao.
        # 7: Permissao de leitura, gravacao e execucao
    return conteudo

def grava_dados():
    diretorio = "/home/phsecchi/Untitled Folder/dashboardb" # pasta inicial para aquisicao de dados
    pid = aquisicao_nr_processos()[-1] # por default ele adquire os dados do processo com o maior pid
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
        time.sleep(10)

#Define a thread e inicia
thr_aq_dados = threading.Thread(target= grava_dados)
thr_aq_dados.start()