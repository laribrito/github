class SolucoesSistema:
    tolerance = 1e-6

    def __init__(self, matriz) -> None:
        if not self.ehMatrizValida(matriz):
            raise Exception('Essa matriz não é quadrada ou o vetor B não foi passado')
        
        self.M, self.B = self.separarMatriz(matriz)
        self.k = len(matriz)
        self.solution = None

    def vetorParaStr(self, v, sep=' '):
        lista_de_strings = [str(numero) for numero in v]
        string = sep.join(lista_de_strings)
        return string

    def test(self):
        if self.solution:
            for linha, esperado in zip(self.M, self.B):
                result = 0
                for sol, lin in zip(self.solution, linha):
                    result += sol * lin

                if abs(result - esperado)>SolucoesSistema.tolerance:
                    return 'A solução não é tão boa assim'
            return 'A solução é suficientemente boa'
        return 'Não há solução'

    def separarMatriz(self, matriz):
        m = []
        vetorF = []
        for linha in matriz:
            m.append(linha[:-1])
            vetorF.append(linha[-1])

        return m, vetorF

    def ehMatrizValida(self, matriz):
        qtdLinhas = len(matriz)
        for i in matriz:
            if len(i) != qtdLinhas + 1:
                return False
        
        return True
    
    def resolve(self):
        raise NotImplementedError("Deve implementar o método resolve() de acordo com a estratégia devida")
                
