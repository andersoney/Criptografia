alfabeto=' abcdefghijklmnopqrstuvwxyz'
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

