from scipy import linalg
import numpy as np
alfabeto='abcdefghijklmnopqrstuvwxyz '
alfabetoLen=len(alfabeto);
import random
# print(linalg.det(a));
i=0
class Hill:
    def __init__(self,matriz,alfabeto='abcdefghijklmnopqrstuvwxyz '):
        self.len_matriz=matriz.shape[0]*matriz.shape[1];
        self.matriz=matriz
        self.alfabeto=alfabeto
        self.alfabeto_len=len(self.alfabeto)
    def make_box(self,text):
        resto=len(text)%self.len_matriz
        if(resto!=0):
            for _ in range(self.len_matriz-resto):
                text=text+alfabeto[random.randint(0, self.alfabeto_len-1)];
            pass;
        print(text);
        num_interaction=len(text)/self.len_matriz
        # print(num_interaction);
        # print(int(num_interaction));
        matrizes=[]
        for _ in range(int(len(text)/self.len_matriz)):
            new_mat=[]
            # print(self.matriz[0])
            for cols in self.matriz:
                # print(row);
                row=[]
                for _ in cols:
                    value=alfabeto.index(text[0]);
                    row.append(value)
                    text=text[1:]
                new_mat.append(row);
            matrizes.append(new_mat)
            pass;
        # print(text);
        return matrizes,text;

    def cifre(self,text):
        matrizes,text=self.make_box(text);
        cifred_text='';
        # print(matrizes,text)
        for box in matrizes:
            cifred_matriz= np.matmul(box,self.matriz)
            cifred_matriz=cifred_matriz%(self.alfabeto_len-1)
            # print(cifred_matriz)
            cifred_text=cifred_text+self.passToText(cifred_matriz)
        return cifred_text;

    def passToText(self,cifredMatriz):
        # print(cifredMatriz);
        new_text=''
        for row in cifredMatriz:
            for value in row:
                value=round(value, 3);
                if(value.is_integer()):
                    # print(value);
                    pass;
                else:
                    print(value);
                    # print(round(value, 3));
                    raise Exception("value is not integer");
                    # value=self.inv_mod(value)
                    # pass;
                # new_value=value%alfabetoLen
                new_value=int(value);
                new_text=new_text+alfabeto[new_value]
        return new_text;
    def inv_mod(self,number):
        new_number=number
        i=2;
        while(not new_number.is_integer()):
            new_number=number*i;
            # print(round(new_number, 3));
            new_number=round(new_number, 3)
            i+=1;
        return new_number;
matriz = np.array([[1, 2],[2, 2]])
det=np.linalg.det( matriz )%26
k_1=(-det+26)**-1
print(k_1);
matriz_inv=(k_1*np.linalg.inv(matriz))%27
print(matriz_inv);
hullCript=Hill(matriz)
text=input();
text_cifred=hullCript.cifre(text);
print(f"Texto cifrado: {text_cifred}");
hull_decript=Hill(matriz_inv)
text_decifred=hull_decript.cifre(text_cifred);
print(f"Texto decifrado: {text_decifred}");

# def is_all_int(matriz):
#     for a in matriz:
#         for b in a:
#             if(not b.is_integer()):
#                 return False;
#     return True;
# print(is_all_int(matriz_inv));
# matriz_inv=matriz_inv*3*4*matriz
# print(matriz_inv*3*4*matriz)
# i=1;
# while (not is_all_int(matriz_inv*i)):
#     i+=1;
# if(is_all_int(matriz_inv*i)):
#         matriz_inv=matriz_inv*i;


# print("")
# print(cifred)
# no_cifred= np.matmul(cifred,matriz_inv)
# print(no_cifred)

