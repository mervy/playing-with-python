# https://pt.stackoverflow.com/questions/407298/como-fazer-um-bruteforce-em-python
from itertools import product
import time
import timeit

chars = [chr(i) for i in (range(97,123))]
#chars += [chr(i) for i in range (65,91)]
#chars += [chr(i) for i in range(48,58)]

# Abaixo, temos todos os caracteres usuais em uma senha: letras, simbolos e números
# chars = [chr(i) for i in range(32, 127)]

password = input("Digite a senha a ser procurada: ")
lenPass = len(password)
attempts = 0

def bruteforceOne(chars, password, lenPass):
    attempts = 0

    for i in product(chars, repeat=lenPass):       
        combine = ''.join(i)
        attempts += 1

        if (attempts % 500000 == 0):
            print('%10i --> %s' % (attempts, combine))

        if password == combine:           
            return ('A senha foi encontrada: "{}" após {} tentativas!'.format(combine, attempts))
            
    return ('Senha não encontrada')  
      
 
begin = timeit.default_timer()
print(bruteforceOne(chars, password, lenPass))
end = timeit.default_timer()
print('O tempo de execução foi de {} s'. format((end-begin)))
print('*' * 60 + '\n')