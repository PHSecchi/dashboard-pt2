# Dashboard - Parte 2

Este projeto foi desenvolvido na disciplina de Sistemas Operacionais do curso de Sistemas de Informação, da Universidade Tecnológica Federal do Paraná, campus Curitiba.

Esta é a segunda parte do projeto de um *dashboard* para monitoramento de alguns status do sistema operacional Debian, que é baseado em Linux.

O software *Dashboard.py* utiliza o comando "sudo fdisk -l" para verificar os discos e as partições. Assim como na primeira parte, também acessa os arquivos da pasta `/proc`, onde estão armazenadas as informações do sistema, e coleta os seguintes dados:

- Nome da máquina;
- Dados de memória (uso e total);
- Processador (nome, núcleos, *threads* e uso);
- Informações de processos (PID, PPID, usuário e memória).

Além disso, o software verifica os diretórios e arquivos de um endereço específico (neste caso, "/home/user/Untitled Folder/dashboardb"), coletando dados de três níveis de profundidade.

Após a coleta, é gerado um arquivo JSON contendo as respectivas chaves e valores.

Por fim, o front-end, desenvolvido em IONIC, exibe as informações na tela.

