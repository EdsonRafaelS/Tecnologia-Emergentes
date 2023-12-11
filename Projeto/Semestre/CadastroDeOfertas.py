import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
#import BancoDeDados as bd

#Funções para adicionar a treeview
def AdicionarDadosTreeview():
    #Coletando dados de um combobox
    ano = button_ano.get()
    semestre = button_semestre.get()
    disciplina = button_disciplina.get()
    nivel_de_ensino = button_NivelDeEnsino.get()
    
    # Verifica se os dados já existem na treeview
    for item in treeview_conteudo.get_children():
        values = treeview_conteudo.item(item, 'values')
        if values == (ano, semestre, disciplina, nivel_de_ensino):
            messagebox.showinfo('Aviso', 'Dados duplicados. Não adicionado.')
            return
    
    #Adicionando a treeview
    #treeview_conteudo.insert('', 'end', values=(ano, semestre, disciplina, nivel_de_ensino))
    
    def InserirOferta():
        """INSERT INTO oferta """

#Excluir linha selecionada
def ExcluirLinha():
    #Obter a linha selecionada na treeview
    linha_selecionada = treeview_conteudo.selection()
    if not linha_selecionada:
        messagebox.showinfo('Aviso', 'Selecione uma linha para excluí-la.')
        return

    # Confirmar exclusão
    resposta = messagebox.askquestion('Confirmação', 'Você realmente quer excluir a linha selecionada?')
    if resposta == 'yes':
        treeview_conteudo.delete(linha_selecionada)
    
#Sair da pagina atual
def SairDaPagina():
    root.destroy()

#Codigo de criação da tela
root = tk.Tk()
root.title('Cadastro de Ofertas')
root.geometry('820x400') #Tamanho principal da tela
root.resizable(False,False) #Não permite 

#Label do ano
label_ano = ttk.Label(root, text='Ano:') #Nome que ira ficar encima do button
label_ano.grid(column=0, row=0, sticky=tk.N) #Posicionando o elemento

#Frame do ano
frame = Frame(root).grid(row = 0, column = 1)

#Combobox do ano
button_ano = ttk.Combobox(root, state="readonly") #Combobox é o botão que possui opções
button_ano['values'] = ('2021', '2022', '2023', '2024') #Cria a lista de seleção
button_ano.current(2)  #Define o item que ira ser selecionado automatico
button_ano.grid(column=0, row=1) #Posicionando o button


#Label de semestre
label_semestre = ttk.Label(root, text='Semestre:') #Nome que ira ficar encima do button
label_semestre.grid(column=1, row=0) #Posicionando o elemento

#Combobox do semestre
button_semestre = ttk.Combobox(root, state="readonly") #Combobox é o botão que possui opções
button_semestre['values'] = (1, 2) #Cria a lista de seleção
button_semestre.current(0) #Define o item que ira ser selecionado automatico
button_semestre.grid(column=1, row=1) #Posicionando o button

#Label da disciplina
label_disciplina = ttk.Label(root, text='Disciplina:')
label_disciplina.grid(column=2, row=0)

#Combobox de disciplina
button_disciplina = ttk.Combobox(root, state="readonly")
button_disciplina['values'] = ('Banco de Dados', 'Projeto Integrador', 'Algoritmos')
button_disciplina.current(0)
button_disciplina.grid(column=2, row=1)

#Label do Nível de Ensino
label_NivelDeEnsino = ttk.Label(root, text='Nível de Ensino')
label_NivelDeEnsino.grid(column=3, row=0)

#Combobox do Nível de Ensino
button_NivelDeEnsino = ttk.Combobox(root, state="readonly")
button_NivelDeEnsino['values'] = ('Superior', 'Técnico')
button_NivelDeEnsino.current(1)
button_NivelDeEnsino.grid(column=3, row=1)

#Treelview
colunas = ('Ano', 'Semestre', 'Disciplina', 'Nível')

# Crie o TreeView com colunas e cabeçalhos
treeview_conteudo = ttk.Treeview(root, columns=colunas, show='headings')

# Configurar os cabeçalhos das colunas
for coluna in colunas:  
    treeview_conteudo.heading(coluna, text=coluna)

# Exibir o TreeView
treeview_conteudo.grid(rowspan=2, columnspan=4, row=4, column=0, padx=8)

#Botão de Salvar
button_salvar = tk.Button(root, text='Salvar', bg='gray', command=lambda : AdicionarDadosTreeview())
button_salvar.grid(row=5, column=1, sticky=tk.S, ipadx=20, ipady=10)

#Botão de Excluir
button_excluir = tk.Button(root, text='Excluir', bg='gray', command=lambda: ExcluirLinha())
button_excluir.grid(row=5, column=2, sticky=tk.SW, ipadx=15 , ipady=10)

#Botão de Cancelar
button_cancelar = tk.Button(root, text='Cancelar', bg='gray', command=lambda: SairDaPagina())
button_cancelar.grid(row=5, column=2, sticky=tk.SE, ipadx=10, ipady=10)


root.grid_columnconfigure(4, weight=212) #Posicionamento fixo da pagina
root.grid_rowconfigure(4, weight=100) #Posicionamento fixo da pagina
root.mainloop()