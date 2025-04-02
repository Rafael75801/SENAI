import os
import time

# Função para carregar o arquivo ASCII com os frames
def carregar_arquivo(arquivo):
    with open(arquivo, 'r') as file:
        return file.readlines()

# Função para limpar a tela no terminal (funciona no Windows e Linux)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal para rodar o Bad Apple
def rodar_bad_apple(arquivo):
    frames = carregar_arquivo(arquivo)
    total_frames = len(frames)
    
    while True:
        for frame in frames:
            limpar_tela()
            print(frame)  # Imprime o frame no terminal
            time.sleep(0.05)  # Ajuste a velocidade conforme necessário

# Caminho do arquivo ASCII (substitua pelo caminho correto)
arquivo_ascii = 'bad_apple_ascii.txt'

# Rodar Bad Apple
rodar_bad_apple(arquivo_ascii)
