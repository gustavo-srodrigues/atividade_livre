import re

CAMINHO_ARQUIVO = 'tinydb_usuários.py'

class Usuario:
    def __init__(self, nome, idade, codigo):
        self.nome = nome
        self.idade = idade
        self.codigo = codigo

class Leitor:
    pass

class Monitor:
    pass

def ehNome(nome):
    if re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", nome):
        return True
    else:
        return False
    

def ehIdade(idade):
    if idade.isdigit():
        idade = int(idade)
        if (idade > 0) and (idade <= 122):
            return True
        return False
    else:
        return False

def ehCodigoLeitor(codigo):
    if codigo.isdigit():
        codigo = str(codigo)
        conta_numeros = len(codigo)
        codigo = int(codigo)
        if conta_numeros == 5:
            return True
        else:
            return False
    else:
        return False     
    


def ehCodigoMonitor(codigo):
    pass

dados_leitor = []

#validação do nome
nome = input("Digite seu nome: ")
if ehNome(nome):
    dados_leitor.append(nome)
else:
    nome = ""
    while nome == "":
        nome = input("Digite seu nome novamente: ")
        if ehNome(nome):
            dados_leitor.append(nome)
        else:
            nome = ""

#validação da idade
idade = input("Digite sua idade: ")
validacao = ehIdade(idade)
while validacao != True:
    idade = input("Digite sua idade novamente: ")
    validacao = ehIdade(idade)
dados_leitor.append(idade)

# criação e validação de código de login leitor
codigo = input("Digite um código de login que desejas que contenha 5 digitos: ")
validacao = ehCodigoLeitor(codigo)
while validacao != True:
    codigo = input("código inválido, digite um código que contenha 5 inteiros: ")
    validacao = ehCodigoLeitor(codigo)
dados_leitor.append(codigo)


print(f"Olá leitor seu nome é {dados_leitor[0]}, você tem {dados_leitor[1]} ano(s) e seu código de login é {dados_leitor[2]}")
