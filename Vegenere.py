alfabeto = "abcdefghijklmnopqrstuvwxyz !"
alfabetoCifra='abcdefghijklmnopqrstuvwxyz'
# texto = "bom dia brasil"
texto =input("Texto claro")
# chave = "testando"
print()
chave =input("chave")
print()
encripted = ''
for index, a in enumerate(texto):
    # print(a)
    position_char = alfabeto.index(a)
    # print(f"position_char: {position_char}")
    b = chave[index % len(chave)]
    position_chave = alfabeto.index(b)
    # print(f"position_chave: {position_chave}")
    newPosition = (position_chave+position_char) % len(alfabeto)
    # print(f"newPosition: {newPosition}")
    encripted += alfabeto[newPosition]
    # print(encripted);
    # exit();
print(f"Encripted: {encripted}")
dencripted = ''
# print(f"aa: {-3%26}")
for index, a in enumerate(encripted):
    # print(a)
    position_char = alfabeto.index(a)
    # print(f"position_char: {position_char}")
    b = chave[index % len(chave)]
    position_chave = alfabeto.index(b)
    # print(f"position_chave: {position_chave}")
    newPosition = (position_char-position_chave) % len(alfabeto)
    # print(f"newPosition: {newPosition}")
    dencripted += alfabeto[newPosition]
    # print(encripted);
    # exit();
print(f"Decripted: {dencripted}")
