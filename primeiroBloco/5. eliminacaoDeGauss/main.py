import sympy as sp
import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SolucoesSistemaClass import SolucoesSistema
import OperacoesMatematicas as op

class EliminacaoGauss(SolucoesSistema):
    def __init__(self, matriz) -> None:
        super().__init__(matriz)

    def resolve(self):
        j = 0
        M = self.M
        B = self.B
        # transformação da matriz
        while j < self.k - 1:
            i = j + 1
            while i < self.k:
                m = M[i][j]/M[j][j]
                x = j
                while x < self.k:
                    M[i][x] -= m * M[j][x]
                    x += 1
                B[i] -= m * B[j]
                i+=1
            j+=1
        
        # substituições
        X = [0] * self.k
        for i in range(self.k-1, -1, -1):
            s = B[i]
            j = i + 1
            while j < self.k:
                s-=M[i][j]*X[j]
                j += 1
            X[i] = (s/M[i][i])
        
        X.reverse()
        lista_de_strings = [str(numero) for numero in X]
        string = ' '.join(lista_de_strings)
        return string
    
    def printMatriz(self, m):
        for i in m:
            for j in i:
                print(j, end=' ')
            print('\n')
        print()

def main():
    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.readlines()

    matriz = []
    for index, i in enumerate(linhas):
        linha = [float(j) for j in i.split()]
        
        if not len(linha) or len(linhas) == index:
            try:
                resultado = EliminacaoGauss(matriz).resolve()
            except Exception as e:
                resultado = f'ERRO: {e}'

            # Escreve os resultados no arquivo out.txt
            with open(os.path.join(dir_path, 'out.txt'), 'w') as arquivo:
                arquivo.write(str(resultado) + '\n\n')
            matriz.clear()
        else:
            matriz.append(linha)

if __name__ == '__main__':
    main()