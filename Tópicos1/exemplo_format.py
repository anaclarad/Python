
from datetime import datetime

# Exemplos Interpolação e string

nome = "Ana clara"

print(f"Nome: {nome}")
print(f"Calculo Soma: {1 + 1}")

#Exemplos format

data_atual = datetime.now()

print(data_atual)

#Format
# yyyy/mm/dd
print(data_atual.strftime("%Y/%M/%d"))


idade = 20
print("Nome: {}\nIdade: {}".format( nome, idade))




nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

