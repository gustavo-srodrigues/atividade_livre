import re
import json


CAMINHO_ARQUIVO = "tinydb_codigos_login.json"

class Resenhas:
    def __init__(self, titulo, texto):
        self.titulo = titulo
        self. texto = texto


class Usuario:
    def __init__(self, nome, codigo):
        self.nome = nome
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
ocupacao = ""
validacao = bool




print(' ______________________ ')
print()
print('   MITHRANDIR LIVROS   ')
print(' ______________________ ')
print()

ocupacao = '' 
ocupacao = input('Você é leitor(a) ou Monitor(a)? [L/M]: ')
ocupacao = ocupacao.upper()
while (ocupacao != 'M' and ocupacao != 'L'):
    ocupacao = input('Inválido, tente novamente: M -> Monitor(a) e L -> leitor: ')
    ocupacao = ocupacao.upper()
print("\n" * 130000)






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


if ocupacao == "M":
    #criação e validação do código de login (monitores)
    codigo = input("Digite o código de login que desejas que contenha 3 digitos: ")
    validacao = ehCodigoMonitor(codigo)
    while validacao != True:
        codigo = input("código inválido, digite um código que contenha 3 inteiros: ")
        validacao = ehCodigoMonitor(codigo)
    dados_usuario.append(codigo)

elif ocupacao == "L":
    # criação e validação de código de login (leitores)
    codigo = input("Digite um código de login que desejas que contenha 5 digitos: ")
    validacao = ehCodigoLeitor(codigo)
    while validacao != True:
        codigo = input("código inválido, digite um código que contenha 5 inteiros: ")
        validacao = ehCodigoLeitor(codigo)
    dados_usuario.append(codigo)



print(dados_usuario)