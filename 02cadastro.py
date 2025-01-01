import re
import json


CAMINHO_ARQUIVO = "tinydb_codigos_login.json"


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
    if codigo.isdigit():
        codigo = str(codigo)
        conta_numeros = len(codigo)
        if conta_numeros == 3:
            return True
        else:
            return False
    else:
        return False

#DECLARAÇÃO DE VARIÁVEIS
dados_usuario = []
nome = ""
idade = ""
codigo = ""
validacao = bool


#validação do nome
nome = input("Digite seu nome: ")
if ehNome(nome):
    dados_usuario.append(nome)
else:
    nome = ""
    while nome == "":
        nome = input("Digite seu nome novamente: ")
        if ehNome(nome):
            dados_usuario.append(nome)
        else:
            nome = ""



#validação da idade
idade = input("Digite sua idade: ")
validacao = ehIdade(idade)
while validacao != True:
    idade = input("Digite sua idade novamente: ")
    validacao = ehIdade(idade)
dados_usuario.append(idade)

# criação e validação de código de login (leitores)
codigo = input("Digite um código de login que desejas que contenha 5 digitos: ")
validacao = ehCodigoLeitor(codigo)
while validacao != True:
    codigo = input("código inválido, digite um código que contenha 5 inteiros: ")
    validacao = ehCodigoLeitor(codigo)
dados_usuario.append(codigo)

#criação e validação do código de login (monitores)
codigo = input("Digite o código de login que desejas que contenha 3 digitos: ")
validacao = ehCodigoMonitor(codigo)
while validacao != True:
    codigo = input("código inválido, digite um código que contenha 3 inteiros: ")
    validacao = ehCodigoMonitor(codigo)
dados_usuario.append(codigo)

user = Usuario(dados_usuario[0], dados_usuario[1], dados_usuario[2])
user_db = [user.__dict__]

with open (CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(user_db, arquivo, ensure_ascii=False, indent=2)