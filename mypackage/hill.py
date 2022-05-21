class Hill:
    def __init__(self, matriz, alfabeto='abcdefghijklmnopqrstuvwxyz '):
        self.len_matriz = matriz.shape[0]*matriz.shape[1]
        self.matriz = matriz
        self.alfabeto = alfabeto
        self.alfabeto_len = len(self.alfabeto)

    def make_box(self, text):
        resto = len(text) % self.len_matriz
        if(resto != 0):
            for _ in range(self.len_matriz-resto):
                text = text+alfabeto[random.randint(0, self.alfabeto_len-1)]
            pass
        print(text)
        num_interaction = len(text)/self.len_matriz
        # print(num_interaction);
        # print(int(num_interaction));
        matrizes = []
        for _ in range(int(len(text)/self.len_matriz)):
            new_mat = []
            # print(self.matriz[0])
            for cols in self.matriz:
                # print(row);
                row = []
                for _ in cols:
                    value = alfabeto.index(text[0])
                    row.append(value)
                    text = text[1:]
                new_mat.append(row)
            matrizes.append(new_mat)
            pass
        # print(text);
        return matrizes, text

    def cifre(self, text):
        matrizes, text = self.make_box(text)
        cifred_text = ''
        # print(matrizes,text)
        for box in matrizes:
            cifred_matriz = np.matmul(box, self.matriz)
            cifred_matriz = cifred_matriz % (self.alfabeto_len-1)
            # print(cifred_matriz)
            cifred_text = cifred_text+self.passToText(cifred_matriz)
        return cifred_text

    def passToText(self, cifredMatriz):
        # print(cifredMatriz);
        new_text = ''
        for row in cifredMatriz:
            for value in row:
                value = round(value, 3)
                if(value.is_integer()):
                    # print(value);
                    pass
                else:
                    print(value)
                    # print(round(value, 3));
                    raise Exception("value is not integer")
                    # value=self.inv_mod(value)
                    # pass;
                # new_value=value%alfabetoLen
                new_value = int(value)
                new_text = new_text+alfabeto[new_value]
        return new_text

        return new_number

    def find_multiplicative_inverse(self, determinant, len_alfabeto):
        for i in range(len_alfabeto):
            inverse = determinant * i
            if inverse % len_alfabeto == 1:
                return i
                break
        raise Exception("Não encontrado inverse multiplicative")