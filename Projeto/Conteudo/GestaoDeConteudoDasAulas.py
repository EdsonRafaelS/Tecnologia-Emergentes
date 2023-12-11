import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox import showinfo

def carregar_dados():
    semestre = periodo.get()
    disciplina = disciplinas.get()
    data = entry_data.get()
    aulas = entry_aula.get()
    conteudo = entry_conteudo.get()

    if semestre and disciplina and data and aulas and conteudo:
        tree.insert("", "end", values=(semestre, disciplina, data, conteudo, aulas))
        showinfo("Dados Carregados", "Dados adicionados ao TreeView com sucesso!")
        limpar_campos()
    else:
        showinfo("Aviso", "Preencha todos os campos antes de carregar os dados.")

def limpar_campos():
    entry_data.delete(0, tk.END)
    entry_aula.delete(0, tk.END)
    entry_conteudo.delete(0, tk.END)

def excluir_cronograma():
    tree.delete(*tree.get_children())
    limpar_campos()

def visualizar_cronograma():
    for item in tree.get_children():
        valores = tree.item(item, 'values')
        print("Semestre: {}, Disciplina: {}, Data: {}, Conteúdo: {}, Aulas: {}".format(valores[0], valores[1], valores[2], valores[3], valores[4]))


root = tk.Tk() 
root.title('Adicionar conteúdos das aulas...') 
root.geometry('650x450')   

root.columnconfigure(0, weight=900)
root.columnconfigure(1, weight=10)
root.columnconfigure(2, weight=10)
root.columnconfigure(3, weight=10)
root.columnconfigure(4, weight=10)
root.columnconfigure(5, weight=10)
root.columnconfigure(6, weight=10)
            
tk.Label(root, text = "Semestre :").grid(column = 0,row = 5, padx = 20, pady = 5,sticky=tk.W) 
           
n = tk.StringVar() 
periodo = ttk.Combobox(root,width=15 ,textvariable = n) 
periodo['values'] = (2022.1,2022.2,2023.1,2023.2)   
periodo.grid(column = 1,padx=5, pady=5 ,row = 5,sticky=tk.W) 
periodo.current() 
#==================================================================================#
tk.Label(root, text = "Disciplina :").grid(column = 2,row = 5, padx = 10, pady =20) 
           
d = tk.StringVar() 
disciplinas = ttk.Combobox(root, width = 18,textvariable = d) 
disciplinas['values'] = ("Banco de Dados-Técnico","Web front-End-Técnico") 
disciplinas.grid(column = 3, row = 5,sticky=tk.W)
disciplinas.current()
#======================================================================#
frame_botoes = tk.Frame(root)
frame_botoes.grid(row=5,column=4)

botao_carregar = tk.Button(frame_botoes, text='Carregar Dados...',command=carregar_dados)
botao_carregar.grid(row=5, pady=5, ipady=5,ipadx=5,padx=5)

#======================================================================#
label_data = tk.Label(root, text='Data:')
label_data.grid(column=0, row=6)

entry_data = tk.Entry(root)
entry_data.grid(row=6,column=1,sticky=tk.EW)

label_aula = tk.Label(root, text='Aulas:')
label_aula.grid(column=2, row=6)

entry_aula = tk.Entry(root)
entry_aula.grid(row=6,column=3)


label_conteudo = tk.Label(root, text='Conteúdo:')
label_conteudo.grid(column=0, row=8,padx=10,pady=10,sticky=tk.W)

entry_conteudo = tk.Entry(root)
entry_conteudo.grid(row=8,column=1)

#==========================================================#
# TreeView
columns = ("Semestre", "Disciplina", "Data", "Conteúdo", "Aulas")
tree = ttk.Treeview(root, columns=("Semestre", "Disciplina", "Data", "Conteúdo", "Aulas"), show="headings")

# Adicionando cabeçalhos ao TreeView
for col in columns:
    tree.heading("Semestre", text="Semestre")
    tree.heading("Disciplina", text="Disciplina")
    tree.heading("Data", text="Data")
    tree.heading("Conteúdo", text="Conteúdo")
    tree.heading("Aulas", text="Aulas")

# Ajustando as colunas
for col in columns:
    tree.column("Semestre",width=80,anchor=tk.CENTER)
    tree.column("Disciplina",width=200,anchor=tk.CENTER)
    tree.column("Data",width=70,anchor=tk.CENTER)
    tree.column("Conteúdo",width=200,anchor=tk.CENTER)
    tree.column("Aulas",width=50,anchor=tk.CENTER)

tree.grid(row=10, columnspan=5,ipadx=3,ipady=5,pady=3,padx=5,sticky=tk.NW)


#==============================================================#
# Botões adicionais

frame_botoes = tk.Frame(root)
frame_botoes.grid(row=33,sticky=tk.EW,column=0, columnspan=5)

botao_adicionar = tk.Button(frame_botoes, text='Adicionar nova data',command=carregar_dados)
botao_adicionar.grid(row=33,column=0, pady=5, ipady=3,ipadx=5,padx=5,sticky=tk.EW)

botao_atualiza = tk.Button(frame_botoes, text='Atualiza conteúdo',command=carregar_dados)
botao_atualiza.grid(row=33,column=1, pady=5, ipady=3,ipadx=5,padx=5,sticky=tk.EW)

botao_limpar = tk.Button(frame_botoes, text='Limpar dados',command=limpar_campos)
botao_limpar.grid(row=33,column=2, pady=5, ipady=3,ipadx=5,padx=5,sticky=tk.EW)

botao_excluir = tk.Button(frame_botoes, text='Excluir cronograma',command=excluir_cronograma)
botao_excluir.grid(row=33,column=3, pady=5, ipady=3,ipadx=5,padx=5,sticky=tk.EW)

botao_visualizar = tk.Button(frame_botoes, text='Visualizar cronograma',command=visualizar_cronograma)
botao_visualizar.grid(row=33,column=4, pady=5, ipady=3,ipadx=5,padx=5,sticky=tk.EW)

root.mainloop()