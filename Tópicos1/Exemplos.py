#saída de dados
print('Ola, pessoa')
#exemplo de como estaria as aspas dulpas sem um fechamento
print('Explícito', 'é', 'melhor " do que implícito')
#exemplo de caractere de escape
print("Minha avó \" está doida")
#exemplo de separador 
nome="Ana Clara"
idade=18
print(nome,idade, sep='-')
print("Ana clara", 20 ,sep=', ')
#exemplo de end
print("Feira", end='. \n 1')
#segue abixo DocString
"""
    Esse é o DocString
"""
#tipo, int,float, string, boolean suscessivamente
print(type(20))
print(type(20.5))
print(type('Ana'))
print(type(True))

#operações matemáticas
#adição
adicao= 10+2
#subtração
subtracao= 10-2
#multiplicação
multiplicacao=10*2
#dvisão que sempre vai retornar float
div_float= 10/3
#divisão que sempre vai retornar um número inteiro
div_int=10/3
#exponenciação
expo=10**2
#modulo(resto da divisão)
modulo=55%2

#peculiaridades de alguns operadores
"""O operador de mais pode ser usado também para concatenação. Também vale ressaltar que o sinal de multiplicação é usado para repetir terminadas informações, abaixo vai alguns exemplos de uso"""
nome= 'Ana Clara'
sobrenome="Oliveira"
print(nome+sobrenome )

programing_2_vezes='programing' * 2
print(programing_2_vezes)
