import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk

#Configurações da pagina
root = tk.Tk()
root.title('Geração de Cronometro')
root.geometry('700x200')
root.resizable(False,False)

#Criando o button Gerencia Ofertas
img_ofertas = PhotoImage(file='C:/Users/edsra/OneDrive/Documentos/TDS - 3 MODULO/TECNOLOGIAS EMERGENTES/SEGUNDO BIMESTRE/Projeto/TelaInicial/img/ofertas.png')
button_ofertas = tk.Button(root, text='Gerenciar Ofertas', image=img_ofertas, compound='top')
button_ofertas.grid(row=0, column=0, padx=20, pady=20)

#Criando o button Gerenciar Semestre
img_semestre = PhotoImage(file='C:/Users/edsra/OneDrive/Documentos/TDS - 3 MODULO/TECNOLOGIAS EMERGENTES/SEGUNDO BIMESTRE/Projeto/TelaInicial/img/semestre.png')
button_semestre = tk.Button(root, text='Gerenciar Semestre', image=img_semestre, compound='top')
button_semestre.grid(row=0, column=1, padx=20, pady=20)

#Criando o button Gerenciar Disciplinas
img_disciplinas = PhotoImage(file='C:/Users/edsra/OneDrive/Documentos/TDS - 3 MODULO/TECNOLOGIAS EMERGENTES/SEGUNDO BIMESTRE/Projeto/TelaInicial/img/disciplina.png')
button_disciplina = tk.Button(root, text='Gerenciar Disciplina', image=img_disciplinas, compound='top')
button_disciplina.grid(row=0, column=2, padx=20, pady=20)

#Criando o button Sair
img_sair = PhotoImage(file='C:/Users/edsra/OneDrive/Documentos/TDS - 3 MODULO/TECNOLOGIAS EMERGENTES/SEGUNDO BIMESTRE/Projeto/TelaInicial/img/sair.png')
button_sair = tk.Button(root, text='Sair', image=img_sair, compound='top')
button_sair.grid(row=0, column=3, padx=20, pady=20)

#Iniciando a pagina
root
root.mainloop()