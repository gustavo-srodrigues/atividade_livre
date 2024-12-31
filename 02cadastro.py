import json 
import re

CAMINHO_ARQUIVO = 'tinydb_usuários.py'

class Leitor:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

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
validacao = None

while validacao != True:
    idade = input("Digite sua idade novamente: ")
    validacao = ehIdade(idade)
dados_leitor.append(idade)




#with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    #json.dump(bd, arquivo)