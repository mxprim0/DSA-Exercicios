"""
Missão: Gerar uma lista de números primos.

Nível de Dificuldade: Médio

Premissas:

1. É correto que 1 não seja considerado um número primo? * Sim
2. Podemos assumir que as entradas são válidas?      * Não
3. Podemos supor que isso se encaixa na memória?      * Sim

Teste Cases:

None -> Exception
Not an int -> Exception
20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]

Algoritmo:

1. Para um número ser primo, ele deve ser 2 ou maior e não pode ser divisível por outro número diferente de si mesmo (e 1).

2. Todos os números não-primos são divisíveis por um número primo.
- Use uma matriz (array) para manter o controle de cada número inteiro até o máximo
- Comece em 2, termine em sqrt (max)
- Podemos usar o sqrt (max) em vez do max porque:
Para cada valor que divide o número de entrada uniformemente, há um complemento b onde a b = n
Se a> sqrt (n) então b <sqrt (n) porque sqrt (n ^ 2) = n
* "Cross off" todos os números divisíveis por 2, 3, 5, 7, ...
configurando array [index] para False
"""
# Solução

from math import sqrt

class PrimeGenerator(object):

    def generate_primes(self, max_num):
        # Implemente aqui sua solução
        if max_num is None:
            raise TypeError('Não pode ser nulo')
        array = [True] * max_num
        array[0] = False
        array[1] = False
        prime = 2
        while prime <= sqrt(max_num):
            self._cross_off(array, prime)
        return array

    def _cross_off(self, array, prime):
        # Implemente aqui sua solução
        for index in range(prime * prime, len(array), prime):
            array[index] = False

    def _next_prime(self, array, prime):
        # Implemente aqui sua solução
        next = prime + 1
        while next < len(array) and not array[next]:
            next += 1
        return next

# Teste da Solução:
from nose.tools import assert_equal, assert_raises

class TestMath(object):

    def test_generate_primes(self):
        prime_generator = PrimeGenerator()
        assert_raises(TypeError, prime_generator.generate_primes, None)
        assert_raises(TypeError, prime_generator.generate_primes, 98.6)
        assert_equal(prime_generator.generate_primes(20), [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True])
        print('Sua solução foi executada com sucesso! Parabéns!')

def main():
    test = TestMath()
    test.test_generate_primes()

if __name__ == '__main__':
    main()