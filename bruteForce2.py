alfabeto='abcdefghijklmnopqrstuvwxyz'

def cifra_cezar(texto:str,chave:int,isCript:int,alfabeto="abcdefghijklmnopqrstuvwxyz")->str:
    from unidecode import unidecode
    texto=unidecode(texto)
    texto=texto.replace(' ','')
    texto=texto.lower()
    cifredText=''
    alfabetoLen=len(alfabeto)
    # print(alfabeto);
    # print(alfabetoLen);
    for a in texto:
        try:
            value=alfabeto.index(a);
        except:
            print(a);
        value=value+((-1)**isCript)*chave
        value=value%alfabetoLen
        cifredText=cifredText+alfabeto[value];
    return cifredText


def cifredText(texto):
    print(texto)
    alfabetoLen=len(alfabeto)
    # for b in range(alfabetoLen+1):
    newalfabeto=" "+alfabeto
    # newalfabeto=alfabeto[:b]+" "+alfabeto[b:];
    print(f"****************\n{newalfabeto}\n****************");

    for a in range(alfabetoLen):
        # "cript=0 decript=1: "
        newText=cifra_cezar(texto,a,1,newalfabeto);
        print(newText,a);
        # alfabetoLen

def decifreTextWithSpace(text):
    alfabetoLen=len(alfabeto)
    for b in range(alfabetoLen+1):
        newalfabeto=alfabeto[:b]+" "+alfabeto[b:];
        print(f"****************\n{newalfabeto}\n****************");

        for a in range(alfabetoLen):
            # "cript=0 decript=1: "
            newText=cifra_cezar(texto,a,1,newalfabeto);
            print(newText,a);
texto=input()
cifredText(texto);