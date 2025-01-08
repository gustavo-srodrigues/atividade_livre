import json
import re

# Caminhos para os arquivos JSON
USUARIOS_DB = "usuarios.json"
LIVROS_DB = "livros.json"
RESENHAS_DB = "resenhas.json"

# Funções de validação
def eh_nome_valido(nome):
    return bool(re.match(r"^[A-Za-z\u00C0-\u017F\s]+$", nome))

def eh_codigo_valido(codigo, tipo):
    return codigo.isdigit() and ((tipo == "L" and len(codigo) == 5) or (tipo == "M" and len(codigo) == 3))

# Classes
class Usuario:
    def __init__(self, nome, codigo):
        self._nome = nome  # Encapsulamento usando atributos protegidos
        self._codigo = codigo

    @property
    def nome(self):
        return self._nome

    @property
    def codigo(self):
        return self._codigo

    def exibir_informacoes(self):
        return f"Nome: {self._nome}, Código: {self._codigo}"

class Leitor(Usuario):
    def pesquisar_autor(self, autor):
        with open(LIVROS_DB, "r") as f:
            livros = json.load(f)
        return [livro for livro in livros if livro["autor"].lower() == autor.lower()]

    def publicar_resenha(self, titulo_livro, titulo_resenha, texto):
        with open(RESENHAS_DB, "r") as f:
            resenhas = json.load(f)
        resenhas.append({"titulo_livro": titulo_livro, "titulo_resenha": titulo_resenha, "texto": texto})
        with open(RESENHAS_DB, "w") as f:
            json.dump(resenhas, f, indent=4)

    def ver_ultimas_resenhas(self):
        with open(RESENHAS_DB, "r") as f:
            resenhas = json.load(f)
        if resenhas:
            for resenha in resenhas[-5:]:
                print(f"Livro: {resenha['titulo_livro']}, Resenha: {resenha['titulo_resenha']}, Texto: {resenha['texto']}")
        else:
            print("Nenhuma resenha encontrada.")

    def avaliar_livro(self, titulo_livro, nota):
        with open(LIVROS_DB, "r") as f:
            livros = json.load(f)
        for livro in livros:
            if livro["titulo"].lower() == titulo_livro.lower():
                if "notas" not in livro:
                    livro["notas"] = []
                livro["notas"].append(nota)
                break
        with open(LIVROS_DB, "w") as f:
            json.dump(livros, f, indent=4)

    def exibir_informacoes(self):  # Polimorfismo
        return f"Leitor - {super().exibir_informacoes()}"

class Monitor(Usuario):
    def cadastrar_livro(self, autor, titulo, ano):
        with open(LIVROS_DB, "r") as f:
            livros = json.load(f)
        livros.append({"autor": autor, "titulo": titulo, "ano": ano})
        with open(LIVROS_DB, "w") as f:
            json.dump(livros, f, indent=4)

    def remover_livro(self, titulo):
        with open(LIVROS_DB, "r") as f:
            livros = json.load(f)
        livros = [livro for livro in livros if livro["titulo"].lower() != titulo.lower()]
        with open(LIVROS_DB, "w") as f:
            json.dump(livros, f, indent=4)

    def exibir_informacoes(self):  # Polimorfismo
        return f"Monitor - {super().exibir_informacoes()}"

# Funções utilitárias
def carregar_usuarios():
    try:
        with open(USUARIOS_DB, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_usuario(usuario):
    usuarios = carregar_usuarios()
    usuarios.append({"nome": usuario.nome, "codigo": usuario.codigo, "tipo": "Leitor" if isinstance(usuario, Leitor) else "Monitor"})
    with open(USUARIOS_DB, "w") as f:
        json.dump(usuarios, f, indent=4)

def exibir_ranking():
    with open(LIVROS_DB, "r") as f:
        livros = json.load(f)
    livros_com_media = [
        {"titulo": livro["titulo"], "media": sum(livro.get("notas", [])) / len(livro.get("notas", []))}
        for livro in livros if livro.get("notas")
    ]
    livros_com_media.sort(key=lambda x: x["media"], reverse=True)
    print("\nRanking dos Livros Mais Bem Avaliados:")
    for livro in livros_com_media[:5]:
        print(f"{livro['titulo']} - Nota Média: {livro['media']:.2f}")

def menu_principal():
    print("\nBem-vindo ao Mithrandir Livros!")
    tipo = input("Você é Leitor (L) ou Monitor (M)? ").upper()
    while tipo not in ("L", "M"):
        tipo = input("Escolha inválida. Por favor, digite L para Leitor ou M para Monitor: ").upper()

    nome = input("Digite seu nome: ")
    while not eh_nome_valido(nome):
        nome = input("Nome inválido. Digite novamente: ")

    codigo = input("Digite seu código de login: ")
    while not eh_codigo_valido(codigo, tipo):
        codigo = input(f"Código inválido. Deve conter {'5' if tipo == 'L' else '3'} dígitos: ")

    if tipo == "L":
        usuario = Leitor(nome, codigo)
    else:
        usuario = Monitor(nome, codigo)

    salvar_usuario(usuario)
    print(f"Bem-vindo(a), {usuario.nome}! Você agora é {'Leitor' if tipo == 'L' else 'Monitor'} no Mithrandir Livros.")

    while True:
        if isinstance(usuario, Leitor):
            print("\nMenu Leitor:")
            print("1. Pesquisar autor")
            print("2. Publicar resenha")
            print("3. Ver últimas resenhas")
            print("4. Avaliar livro")
            print("5. Exibir informações")
            print("6. Ver ranking dos livros mais bem avaliados")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                autor = input("Digite o nome do autor: ")
                livros = usuario.pesquisar_autor(autor)
                if livros:
                    for livro in livros:
                        print(f"{livro['titulo']} ({livro['ano']})")
                else:
                    print("Nenhum livro encontrado para este autor.")

            elif opcao == "2":
                titulo_livro = input("Título do livro: ")
                titulo_resenha = input("Título da resenha: ")
                texto = input("Texto da resenha: ")
                usuario.publicar_resenha(titulo_livro, titulo_resenha, texto)
                print("Resenha publicada com sucesso!")

            elif opcao == "3":
                usuario.ver_ultimas_resenhas()

            elif opcao == "4":
                titulo_livro = input("Título do livro: ")
                nota = float(input("Nota (0 a 10): "))
                usuario.avaliar_livro(titulo_livro, nota)
                print("Livro avaliado com sucesso!")

            elif opcao == "5":
                print(usuario.exibir_informacoes())

            elif opcao == "6":
                exibir_ranking()

            elif opcao == "7":
                break

        elif isinstance(usuario, Monitor):
            print("\nMenu Monitor:")
            print("1. Cadastrar livro")
            print("2. Remover livro")
            print("3. Exibir informações")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                autor = input("Nome do autor: ")
                titulo = input("Título do livro: ")
                ano = input("Ano de publicação: ")
                usuario.cadastrar_livro(autor, titulo, ano)
                print("Livro cadastrado com sucesso!")

            elif opcao == "2":
                titulo = input("Título do livro a remover: ")
                usuario.remover_livro(titulo)
                print("Livro removido com sucesso!")

            elif opcao == "3":
                print(usuario.exibir_informacoes())

            elif opcao == "4":
                break

# Execução do programa
menu_principal()
