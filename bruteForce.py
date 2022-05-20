alfabeto='abcdefghijklmnopqrstuvwxyz'
def cifra_cezar(texto:str,chave:int,isCript:int)->str:
    from unidecode import unidecode
    texto=unidecode(texto)
    texto=texto.replace(' ','')
    texto=texto.lower()
    cifredText=''
    alfabetoLen=len(alfabeto)
    for a in texto:
        try:
            value=alfabeto.index(a);
        except:
            print(a);
        value=value+((-1)**isCript)*chave
        value=value%alfabetoLen
        cifredText=cifredText+alfabeto[value];
    return cifredText

texto=input()
print(texto)
alfabetoLen=len(alfabeto)
for a in range(alfabetoLen):
    # "cript=0 decript=1: "
    newText=cifra_cezar(texto,a,1);
    print(newText,a);
    # alfabetoLen