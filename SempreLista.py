class SempreLista(list):
    def fix(self):
        return []
    def __init__(self, Objeto):
        lista = []
        def TupleToList(t):
            r = []
            for i in range(0, len(t)):
                r += [t[i]]
            return r
        tamanho = len(Objeto)
        for i in range(0, tamanho):
            lista += [Objeto[i]]

        for i in range(0, tamanho):
            if (type(lista[i]) == list):
                tamanho += len(lista[i]) - 1

        for i in range(0, tamanho):
            if type(lista[i]) == list:
                aux = lista[i]
                lista.remove(aux)
                lista = lista[:i] + aux + lista[i:]
            elif type(lista[i]) == tuple:
                lista = lista[:i] + TupleToList(lista[i]) + lista[i:]

        self += lista
''' 
Ex:'''
testTuple = (1,2,[3,4,5,6,7],8,9,[10,11],[12], (13,14))
testTupleResult = SempreLista(testTuple)
print(testTupleResult)
print(testTupleResult + [13,14,15])
print(type(testTupleResult))
''''''
