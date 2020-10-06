"""
Missão: Implementar um algoritmo para determinar se uma string possui todos os caracteres exclusivos.

Nível de Dificuldade: Baixo

Premissas:

Podemos assumir que a string é ASCII? Sim Nota: As cadeias de caracteres Unicode podem exigir tratamento especial dependendo do seu idioma
Podemos supor que há distinção entre maiúsculas e minúsculas? * Sim
Podemos usar estruturas de dados adicionais? * Sim

Teste Cases

None -> False
'' -> True
'foo' -> False
'bar' -> True

Algoritmo: Hash Map Lookup

Manteremos um mapa hash (conjunto) para rastrear os caracteres únicos que encontramos.

Passos:

1. Faça um scan cada caracter
2. Para cada caracter:
Se o caracter não existir em um mapa de hash, adicione o caractere a um mapa de hash
Senão, retorne False
3. Retornar Verdadeiro

Nota:
Também podemos usar um dicionário, mas parece mais lógico usar um set, pois ele não contém elementos duplicados

"""
from nose.tools import assert_equal

class UniqueChars(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        for char in string:
            if string.count(char) > 1:
                return False
        return True

class TestUniqueChars(object):

    def test_unique_chars(self, func):
        assert_equal(func(None), False)
        assert_equal(func(''), True)
        assert_equal(func('foo'), False)
        assert_equal(func('bar'), True)
        print('Sua solução foi executada com sucesso! Parabéns!')

def main():
    test = TestUniqueChars()
    try:
        unique_chars = UniqueChars()
        test.test_unique_chars(unique_chars.has_unique_chars)
    except NameError:
        pass

if __name__ == '__main__':
    main()
