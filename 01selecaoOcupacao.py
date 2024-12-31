

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