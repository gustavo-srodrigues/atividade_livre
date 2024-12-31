print(' ______________________ ')
print()
print('   MITHRANDIR LIVROS   ')
print(' ______________________ ')
print()

ocupacao = '' 
ocupacao = input('Você é leitor(a) ou bibliotecário(a)? [L/B]: ')
ocupacao = ocupacao.upper()
while (ocupacao != 'B' and ocupacao != 'L'):
    ocupacao = input('Inválido, tente novamente: B -> bibliotecário e L -> leitor: ')
    ocupacao = ocupacao.upper()
