# https://academiahopper.com.br/random-como-gerar-e-quebrar-senhas-fortes/
# https://informacaotech.com/criando-seu-proprio-gerador-de-senhas-com-python/
print("[||||||----Generating Strong Passwords----||||||]")

import string
from random import choice

lower = string.ascii_lowercase # abcd...
upper = string.ascii_uppercase # ABCD...
allLetters = string.ascii_letters # abcd...ABCD...
digits = string.digits # 0123...
punctuation = string.punctuation #<=.^...
alls = allLetters + digits + punctuation

size = int(input("Qual o tamanho da senha? "))
types = alls
password = ''

for i in range(size):
    password += choice(types)
print (password)
