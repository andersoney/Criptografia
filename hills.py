import random
from scipy import linalg
import numpy as np
# from mypackage.hill import Hill


class Hill:
    def find_multiplicative_inverse(self, determinant, len_alfabeto):
        for i in range(len_alfabeto):
            inverse = determinant * i
            # print(f"inverse: {inverse}-{inverse % len_alfabeto}")
            if inverse % len_alfabeto == 1:
                # print(f"multiplicative_inverse:{i}\tlen_alfabeto:{len_alfabeto}")
                return i
        raise Exception("Não encontrado inverse multiplicative")

    def get_inverse(self, matriz, len_alfabeto):
        determinant = np.linalg.det(matriz)
        determinant = int(round(determinant, 1))
        print(f"Determinante: {determinant%len_alfabeto}")
        multiplicative_inverse = self.find_multiplicative_inverse(
            determinant, len_alfabeto)
        # print(f"multiplicative_inverse:{multiplicative_inverse}")
        matriz_inv = np.linalg.inv(matriz)*determinant
        matriz_inv = matriz_inv*multiplicative_inverse % len_alfabeto
        return matriz_inv

    def mult_matrix(self, matriz1, matriz2, len_alfabeto):
        # print(f"Matriz 1:\n{matriz1}")
        # print(f"Matriz 2:\n{matriz2}")
        return np.matmul(matriz1, matriz2) % len_alfabeto

    def normalize_text(self, text, len_matriz):
        len_text = len(text)
        resto = len_text % len_matriz
        if(resto != 0):
            for _ in range(len_matriz-resto):
                text = text+'o'
            pass
        else:
            pass
        # print(text)
        len_text = len(text)
        return text, len_text

    def one_matriz_convert(self, lenx, leny, alfabeto, text):
        arrays = []
        for _ in range(lenx):
            row = []
            for _ in range(leny):
                # print(text[0],alfabeto.index(text[0]));
                row.append(alfabeto.index(text[0]))
                text = text[1:]
                # print(text);
                pass
            arrays.append(row)
        local_matriz = np.array(arrays, dtype=np.float64)
        return local_matriz, text

    def convert_text_to_matrizes(self, text, shape, alfabeto):
        len_matriz = shape[0]*shape[1]
        text, len_text = self.normalize_text(text, len_matriz)
        num_natrizes = int(len_text/len_matriz)
        # print(num_natrizes)

        matrizes = []
        for _ in range(num_natrizes):
            local_matriz, text = self.one_matriz_convert(
                shape[0], shape[1], alfabeto, text)
            matrizes.append(local_matriz)
            pass
        # print(text)
        # print(matrizes)
        return matrizes

    def convert_matriz_to_text(self, matriz, alfabeto):
        # print(matriz)
        text = ''
        for row in matriz:
            for col in row:
                # print(col)
                text += alfabeto[int(col)]
        return text

    def encript(self, text, matriz, alfabeto):
        len_alfabeto = len(alfabeto)
        matriz_inv = self.get_inverse(matriz, len(alfabeto))
        # print(f"matriz_inv:\n{matriz_inv}")
        matrizes = self.convert_text_to_matrizes(text, matriz.shape, alfabeto)
        matriz_cripto = []
        for matriz_text in matrizes:
            # print(matriz_text)
            cripto = self.mult_matrix(matriz_text, matriz, len_alfabeto)
            # print(cripto)

            # print(decripto)
            matriz_cripto.append(cripto)
        cripto_text = ''
        for matriz_c in matriz_cripto:
            cripto_text += self.convert_matriz_to_text(matriz_c, alfabeto)
        return cripto_text

    def decript(self, cripto_text, matriz, alfabeto):
        len_alfabeto = len(alfabeto)
        matriz_inv = self.get_inverse(matriz, len(alfabeto))
        matrizes_cript = self.convert_text_to_matrizes(
            cripto_text, matriz.shape, alfabeto)
        matriz_decripto = []
        for matriz_text in matrizes_cript:
            decripto = self.mult_matrix(matriz_text, matriz_inv, len_alfabeto)
            matriz_decripto.append(decripto)
        decripto_text = ''
        for matriz_d in matriz_decripto:
            decripto_text += self.convert_matriz_to_text(matriz_d, alfabeto)
        return decripto_text


def testando_fatores_iniciais(alfabeto):
    hill = Hill()
    len_alfabeto = len(alfabeto)
    matriz2 = np.array([[2,  2], [14, 26]], dtype=np.float64)
    # print(f"Testando fatores Iniciais\n {'_'*100}")
    matriz = np.array([[9, 4], [5, 7]], dtype=np.float64)
    print(f"matriz: \n{matriz}")
    matriz_inv = hill.get_inverse(matriz, len(alfabeto))
    print(f"Inversa:\n{matriz_inv}")
    print(
        f"Matriz e Inversa: \n{hill.mult_matrix(matriz, matriz_inv, len_alfabeto)}")
    print(f"Testando criptografia e decriptografia\n{'&'*100}")
    print(matriz2)
    cripto = hill.mult_matrix(matriz2, matriz, len_alfabeto)
    print(cripto)
    decripto = hill.mult_matrix(cripto, matriz_inv, len_alfabeto)
    print(decripto)
    return matriz_inv


hill = Hill()
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
# matriz_inv = testando_fatores_iniciais(alfabeto)
# exit()

if(__name__ == '__main__'):
    matriz = np.array([[19,  4, 18],
                       [19,  0, 13],
                       [3, 14, 26]], dtype=np.float64)
    chave = 'cababababababa'
    # matriz,text = hill.one_matriz_convert(3,3,alfabeto,chave)
    matriz = np.array([[9, 4], [5, 7]], dtype=np.float64)
    print(f"Chave:\n{matriz}\tlen_alfabeto:{len(alfabeto)}")
    matriz_inv = hill.get_inverse(matriz, len(alfabeto))
    # text = "totestando nao me enche ze!\\\\\\\'\"".lower()
    text = input()
    text = text.replace(' ', '')
    cripto_text = hill.encript(text, matriz, alfabeto)
    print(cripto_text)
    print(f"Decriptando:")
    decripto_text = hill.decript(cripto_text, matriz, alfabeto)
    print(decripto_text)
pass
