# Mithrandir Livros

**Descrição Geral**
- O Mithrandir Livros é um algoritmo para postagem e avaliação de livros, funcionando como uma mini biblioteca.

**Cadastro**
- **Seleção de Ocupação**: Usuário escolhe entre Monitor(a) ou Leitor(a).
- **Criação de Cadastro**:
  - Leitores fazem seu próprio código de login de 5 dígitos.
  - Monitores fazem seu próprio código de login de 3 dígitos.
- **Finalização de Cadastro**: Mensagens de boas-vindas personalizadas.

**Menu de Opções**
- **Monitor**:
  1. Cadastrar obra (autor, título, ano).
  2. Remover obra (pesquisa por autor).
  3. Ver leitores.
  4. Remover resenhas (pesquisa por título).
  5. Sair (volta para o login).
  
- **Leitor**:
  1. Pesquisar autor (exibe livros do autor).
  2. Pesquisar livro (exibe detalhes do livro).
  3. Ver últimas resenhas.
  4. Publicar resenha (título e conteúdo).
  5. Avaliar livro (atribuir nota).
  6. Ver livros mais bem avaliados.
  7. Sair (volta para o login).

**Banco de Dados**
- Utiliza arquivos .JSON para armazenar:
  - Autores e seus livros com notas.
  - Leitores e Monitores.
  - Resenhas e seus títulos.
