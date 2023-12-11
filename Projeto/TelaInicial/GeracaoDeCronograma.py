import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import PhotoImage
from PIL import Image, ImageTk

#Logo abaixo estará todas
#Função para abrir a tela de Gerenciar Ofertas da pasta Semestre
def AbrirGerenciarOfertas():
    caminho = 'C:\\TDS - 3 MODULO\\TECNOLOGIAS EMERGENTES\\SEGUNDO BIMESTRE\\Projeto\\Semestre\\CadastroDeOfertas.py'
    
    subprocess.Popen(["Python", caminho])
    
    root.destroy()

#Função para abrir a tela de Gerenciar Semestre da pasta Semestre
def AbrirGerenciarSemestre():
    caminho = 'C:\\TDS - 3 MODULO\\TECNOLOGIAS EMERGENTES\\SEGUNDO BIMESTRE\\Projeto\\Semestre\\CadastroSemestre.py'
    
    subprocess.Popen(["Python", caminho])
    
    root.destroy()

#Função para abrir a tela de Gerenciar Disciplina da pasta Disciplina
def AbrirGerenciarDisciplina():
    caminho = 'C:\\TDS - 3 MODULO\\TECNOLOGIAS EMERGENTES\\SEGUNDO BIMESTRE\\Projeto\\Disciplina\\CadastroDeDisciplina.py'  
    
    subprocess.Popen(["Python", caminho])
    
    root.destroy()

def SairDaPagina():
    root.destroy()

#Configurações da pagina
root = tk.Tk()
root.title('Geração de Cronometro')
root.geometry('900x250')
root.resizable(False,False)

#Criando o button Gerencia Ofertas
img_ofertas = PhotoImage(file='C:\TDS - 3 MODULO\TECNOLOGIAS EMERGENTES\SEGUNDO BIMESTRE\Projeto\TelaInicial\img/ofertas.png')
button_ofertas = tk.Button(root, text='Gerenciar Ofertas', image=img_ofertas, compound='top', command=lambda: AbrirGerenciarOfertas())  
button_ofertas.grid(row=0, column=0, padx=40, pady=20, ipadx=15, ipady=15)

#Criando o button Gerenciar Semestre
img_semestre = PhotoImage(file='C:\TDS - 3 MODULO\TECNOLOGIAS EMERGENTES\SEGUNDO BIMESTRE\Projeto\TelaInicial\img/semestre.png')
button_semestre = tk.Button(root, text='Gerenciar Semestres', image=img_semestre, compound='top', command=lambda : AbrirGerenciarSemestre())
button_semestre.grid(row=0, column=1, padx=20, pady=20, ipadx=15, ipady=15)

#Criando o button Gerenciar Disciplinas
img_disciplinas = PhotoImage(file='C:\TDS - 3 MODULO\TECNOLOGIAS EMERGENTES\SEGUNDO BIMESTRE\Projeto\TelaInicial\img/disciplina.png')
button_disciplina = tk.Button(root, text='Gerenciar Disciplinas', image=img_disciplinas, compound='top', command=lambda: AbrirGerenciarDisciplina())
button_disciplina.grid(row=0, column=2, padx=20, pady=20, ipadx=15, ipady=15)

#Criando o button Sair
img_sair = PhotoImage(file='C:\TDS - 3 MODULO\TECNOLOGIAS EMERGENTES\SEGUNDO BIMESTRE\Projeto\TelaInicial\img/sair.png')
button_sair = tk.Button(root, text='Sair', image=img_sair, compound='top', command=lambda: SairDaPagina())
button_sair.grid(row=0, column=3, padx=20, pady=20, ipadx=15, ipady=15)

#Iniciando a pagina
root
root.mainloop()