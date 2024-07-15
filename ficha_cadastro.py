import os

def cadastrar_cliente():
    nome = input('Qual o nome do cliente: ')
    idade = input("Qual a idade do cliente: ")
    data_nascimento = input("Qual a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Qual o endereco do cliente: ")
    data_atendimento = input("Qual a data que foi realizada o atendimento (DD/MM/AAAA): ")
    observacoes = input("Alguma observação sobre este cliente: ")
    diagnostico = input("Qual o diagnostico desse cliente: ")
    
    data_atendimento = data_atendimento.replace('/','-')
    data_nascimento = data_nascimento.replace('/','-')
    
    # Criar uma nova pasta para o cliente
    pasta_base = '/Users/Desktop/cadastro-cliente/Clientes'
    pasta_cliente = nome.replace(" ", "_").capitalize()  
    caminho_pasta_cliente = os.path.join(pasta_base, pasta_cliente)
    
    # Confere se a pasta existe com o nome do cliente antes de criar
    if not os.path.exists(caminho_pasta_cliente):
        os.makedirs(caminho_pasta_cliente)
    
    # Cria uma pasta com o nome do cliente, seguido da data de atendimento para poder anexar fotos
    caminho_pasta_cliente = os.path.join(caminho_pasta_cliente, f'{pasta_cliente}_{data_atendimento}')
    if not os.path.exists(caminho_pasta_cliente):
        os.makedirs(caminho_pasta_cliente)
    
    
    
    # Nome do arquivo criado dentro da pasta do cliente
    nome_arquivo = os.path.join(caminho_pasta_cliente, f'{pasta_cliente}_{data_atendimento}.txt')
    
    # Escrever no arquivo de texto
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade}\n")
        arquivo.write(f"Data de Nascimento: {data_nascimento}\n")
        arquivo.write(f"Endereço: {endereco}\n")
        arquivo.write(f"Data do Atendimento: {data_atendimento}\n")
        arquivo.write(f"Observações: {observacoes}\n")
        arquivo.write(f"Diagnostico: {diagnostico}\n")

cadastrar_cliente()
