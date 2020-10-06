"""
Missão: Implementar o Algoritmo de Ordenação "Selection sort".

Nível de Dificuldade: Alto

Premissas:

- As duplicatas são permitidas?
* Sim
- Podemos assumir que a entrada é válida?
* Não
- Podemos supor que isso se encaixa na memória?
* Sim

Teste Cases:

None -> Exception
[] -> []
One element -> [element]
Two or more elements

Algoritmo:

Podemos fazer isso de forma recursiva ou iterativa.
Iterativamente será mais eficiente, pois não requer sobrecarga de espaço extra com as chamadas recursivas.
Para cada elemento:
verifique cada elemento à direita para encontrar o min: Se min < elemento atual, swap
"""
# Solução:

class SelectionSort(object):

    def sort(self, data):
        # Implemente aqui sua solução
        if data is None:
            raise TypeError('Dados não podem ser nulos.')
        if len(data) < 2:
            return data
        for i in range(len(data) -1):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            if data[min_index] < data[i]:
                data[i], data[min_index] = data[min_index], data[i]
        return data

    def sort_interative_alt(self, data):
        if data is None:
            raise TypeError('Dados não podem ser nulos.')
        if len(data) < 2:
            return data
        for i in range(len(data) -1):
            self._swap(data, i, self._find_min_index(data, i))
        return data

    def sort_recursive(self, data):
        if data is None:
            raise TypeError('Dados não podem ser nulos.')
        if len(data) < 2:
            return data
        return self._sort_recursive(data, start=0)

    def _sort_recursive(self, data, start):
        if data is None:
            return TypeError('Dados não podem ser nulos.')
        if start < len(data) - 1:
            swap(data, start, self._find_min_index(data, start))
            self._sort_recursive(data, start + 1)
        return data

    def _find_min_index(selfself, data, start):
        min_index = start
        for i in range(start + 1, len(data)):
            if data[i] < data[min_index]:
                min_index = i
        return min_index

    def _swap(self, data, i, j):
        if i != j:
            data[i], data[j] = data[j], data[i]
        return data

# Teste da Solução:
from nose.tools import assert_equal, assert_raises

class TestSelectionSort(object):

    def test_selection_sort(self, func):
        print('None input')
        assert_raises(TypeError, func, None)

        print('Input vazio')
        assert_equal(func([]), [])

        print('Um elemento')
        assert_equal(func([5]), [5])

        print('Dois ou mais elementos')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        assert_equal(func(data), sorted(data))

        print('Sua solução foi executada com sucesso! Parabéns!')

def main():
    test = TestSelectionSort()
    try:
        selection_sort = SelectionSort()
        test.test_selection_sort(selection_sort.sort)
    except NameError:
        pass

if __name__ == '__main__':
    main()
