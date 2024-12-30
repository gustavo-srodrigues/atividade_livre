Um programa de avaliação e cadastro de livros.
Mithrandir Livros
# CADASTRO
## Seleção de ocupação
|
Bibliotecário(a) ou Leitor(a)? (B/L) (login com matrícula)
|


## Verificação de matrícula
|
se matricula não existir
encaminha p/ cadastro
|
se matricula existir encaminhar para menu de respectiva ocupação

## Criação de cadastro
Nome, idade, leitor ou bibliotecário -> 
se leitor -> fazer matricula de 6 digitos
se bibliotecário -> fazer matricula de 4 digitos

## Finalização de cadastro
MENSAGEM ( Bem Vindo(a) $NOME$!)
MENSAGEM (Você agora é um(a) leitor(a) do Mithrandir Livros!)
ou 
MENSAGEM (Você agora é um(a) bibliotecário(a) do Mithrandir Livros! Agradecemos sua ajuda!)


# MENU
## Bibliotecário
1. Cadastrar obra; 
[Nome do autor, Título do livro, Ano de publicação]
(deseja cadastrar mais algum autor? S) -> REPETE
(deseja cadastrar mais algum autor? N) -> volta para menu

2. Remover obra;
|
pesquisa nome do autor
remover? (S/N)
|
(deseja remover mais alguma obra? S) -> REPETE
(deseja remover mais alguma obra? N) -> volta para menu

3. Ver dos leitores; 
(opção para voltar para menu)

4. Remover resenhas; 
|
pesquisa titulo da resenha
remover? (S/N)
|
(deseja remover mais alguma resenha? S) -> REPETE
(deseja remover mais alguma resenha? N) -> volta para menu

6. Sair;
(volta para o login) 

## Leitor 
1. Pesquisar autor(a); 
|
aparece nome e livros do autor
|
(deseja pesquisar mais algum autor? S) -> REPETE
(deseja pesquisar mais algum autor? N) -> volta para menu

2. Pesquisar livro;
|
aparece nome do livro juntamente com o nome do autor e data de publicação
|
(deseja pesquisar mais algum livro? S) -> REPETE
(deseja pesquisar mais algum livro? N) -> volta para menu

3. Ver últimas resenhas;
|
se tiver -> última resenhas em ordem de postagem
se não-> (nenhuma resenha ainda...)
|
(opção para voltar para menu)

4. Publicar Resenha;
[titulo da resenha]
[resenha... ]
(deseja publicar mais alguma resenha? S) -> REPETE
(deseja publicar mais alguma resenha? N) -> volta para menu


5. Avaliar livro;
|
pesquisa livro
atribuir nota ao livro
|
(deseja avaliar mais algum livro? S) -> REPETE
(deseja avaliar mais algum livro? N) -> volta para menu


6. Ver livros mais bem avaliados;
|
se tiver -> 5 mais bem avaliados
se não-> (nenhum livro avaliado ainda...)
|
(opção para voltar para menu)

7. sair;
 (volta para o login)

# BANCO DE DADOS EM .JSON
Ter um banco de dados de autores e seus respectivos livros, junto com a nota.
Ter um bando de dados de leitores e bibliotecários, separados.
Ter um banco de dados das resenhas juntamente com seu titulo.