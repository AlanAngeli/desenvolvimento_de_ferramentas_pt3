"""

- Biblioteca webbrowser: fornece uma interface de alto nível para permitir a
exibição de documentos Web aos usuários.

- Biblioteca tkinter: fornece interface padrão do Python para o kit de
ferramentas gráficas Tk

"""

import webbrowser

from tkinter import *  # * importa tudo da biblioteca tkinter

root = Tk( )

root.title('Abrir browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mhygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
root.mainloop

