import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Cadastro de disciplinas')
root.geometry('700x600+100+50')

# criando frame
frame = tk.Frame(root, border=1, relief=tk.RAISED)
frame.grid()

nome_frame = tk.Frame(root)
nome_frame.grid()

label_nome = tk.Label(nome_frame, text="Nome da disciplina:")
label_nome.grid(row=0, column=0, padx=85, pady=15)

nome_entry = tk.Entry(nome_frame, bd=3)
nome_entry.grid(row=0, column=1)

# carga horaria
cargaH_frame = tk.Frame(root)
cargaH_frame.grid()

label_cargaH = tk.Label(cargaH_frame, text="Carga horária:")
label_cargaH.grid(row=0, column=0, padx=100, pady=15)

cargaH_entry = tk.Entry(cargaH_frame, bd=3)
cargaH_entry.grid(row=0, column=1)

# combox nivel disciplina
nivel_frame = tk.Frame(root)
nivel_frame.grid()

label_nivel = tk.Label(nivel_frame, text="Nível da disciplina:")
label_nivel.grid(row=0, column=0, padx=85, pady=15, sticky=tk.E)

Button_nivel = ttk.Combobox(nivel_frame)
Button_nivel['values'] = ('Ensino Médio', 'Técnico Subsequente', 'Superior')
Button_nivel.current(2)
Button_nivel.grid(row=0, column=1, padx=0)

# Botões (Cadastrar, Alterar, Remover, Cancelar)
botoes_frame = tk.Frame(root)
botoes_frame.grid()

button_cadastrar = tk.Button(botoes_frame, text="Cadastrar",  bg="light green")
button_cadastrar.grid(row=0, column=0, padx=10)

button_alterar = tk.Button(botoes_frame, text="Alterar", bg="yellow")
button_alterar.grid(row=0, column=1, padx=10, pady=10)

button_remover = tk.Button(botoes_frame, text="Remover", bg="orange")
button_remover.grid(row=0, column=2, padx=10)

button_cancelar = tk.Button(botoes_frame, text="Cancelar", bg="red")
button_cancelar.grid(row=0, column=3, padx=10)

# Configurar o layout da janela
frame.grid(row=0, column=0, pady=10)  # Ajuste o valor de pady conforme necessário
nome_frame.grid(row=1, column=0)
cargaH_frame.grid(row=2, column=0)
nivel_frame.grid(row=3, column=0)
botoes_frame.grid(row=4, column=0)


# Criar Treeview com 4 colunas
tree = ttk.Treeview(root, columns=("Coluna1", "Coluna2", "Coluna3", "Coluna4"), show="headings")

# Configurar cabeçalhos das colunas
tree.heading("Coluna1", text="ID")
tree.heading("Coluna2", text="Nome da Disciplina")
tree.heading("Coluna3", text="Nível da Disciplina")
tree.heading("Coluna4", text="Carga horária")


# Adicionar dados de exemplo
tree.insert("", "end", values=(" 1", "Banco de dados", "Superior", "72"))
tree.insert("", "end", values=(" 2", "Front-end", "Técnico Subsequente", "110"))
tree.insert("", "end", values=(" 3", "Dispositivos móveis", "Ensino Médio", "120"))
tree.insert("", "end", values=(" 4", "Métodos ágeis", "Técnico Subsequente", "48"))

# Ajustar a largura das colunas
tree.column("Coluna1", width=100)
tree.column("Coluna2", width=200)
tree.column("Coluna3", width=150)
tree.column("Coluna4", width=100)


# Adicionar barra de rolagem
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Posicionar Treeview e barra de rolagem na janela
tree.grid(row=5, column=0, sticky="nsew")
scrollbar.grid(row=5, column=1, sticky="ns")

# Configurar o layout da janela
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)

tk.mainloop()