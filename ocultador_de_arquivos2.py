import ctypes

pasta = input('Digite o caminho a ser ocultado ex C:/pasta: ')

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print('Pasta ocultada')
else:
    print('A pasta não foi ocultada')