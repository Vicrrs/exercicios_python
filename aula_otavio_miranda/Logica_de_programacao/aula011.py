# f_strings

nome = "Victor Roza Souza"
altura = 1.69
peso = 80
imc = peso / altura ** 2

linha_1 = "{} tem {} metros de altura!. E pesa {}"
formato = linha_1.format(nome, altura, peso)

print(formato)
