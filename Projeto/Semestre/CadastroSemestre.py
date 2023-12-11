import tkinter as tk
from tkinter import ttk, messagebox

def salvar():
    nome = combo_ano.get()
    selecao = combo_selecao.get()

    # Verificando se a combinação ano e semestre já existe na tabela
    for item in tree.get_children():
        if (tree.item(item, 'values')[0] == nome) and (tree.item(item, 'values')[1] == selecao):
            messagebox.showwarning("Erro", "Este ano e semestre já foram cadastrados.")
            return

    # Adicionando os dados à tabela
    tree.insert("", tk.END, values=(nome, selecao))

    # Exibindo os dados cadastrados
    mensagem = f"Ano: {nome}\nSemestre: {selecao}"
    messagebox.showinfo("Cadastro Realizado", mensagem)

def excluir():
    # Limpar os campos de entrada
    combo_ano.set("")  
    combo_selecao.set("")

def cancelar():
    root.destroy()

# Criando a janela principal
root = tk.Tk()
root.title("Cadastro de semestres")

# Adicionando margens
margem_lateral = 20
margem_superior = 20

# Obtendo as dimensões da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Calculando a posição para centralizar a janela
pos_x = largura_tela // 2 - 300  # Largura da janela: 600 (300 de cada lado)
pos_y = altura_tela // 2 - 200   # Altura da janela: 400 (200 de cada lado)

root.geometry(f'600x400+{pos_x}+{pos_y}')
root.resizable(False,False)

# Criando e posicionando os widgets na janela
label_ano = tk.Label(root, text="Selecione o ano:")
label_ano.grid(row=0, column=0, padx=(margem_lateral, 5), pady=(margem_superior, 10), sticky="e")
opcoes_ano = [str(ano) for ano in range(2022, 2030)]  # Anos de 2022 a 2029
combo_ano_var = tk.StringVar() 
combo_ano_var.set(opcoes_ano[0])
combo_ano = ttk.Combobox(root, textvariable=combo_ano_var, values=opcoes_ano, width=5)
combo_ano.grid(row=0, column=1, padx=5, pady=(margem_superior, 10))

label_selecao = tk.Label(root, text="Selecione o semestre:")
label_selecao.grid(row=0, column=2, padx=5, pady=(margem_superior, 10), sticky="e")
opcoes_selecao = ["1", "2"]
combo_selecao_var = tk.StringVar()
combo_selecao_var.set(opcoes_selecao[0])
combo_selecao = ttk.Combobox(root, textvariable=combo_selecao_var, values=opcoes_selecao, width=5)
combo_selecao.grid(row=0, column=3, padx=(5, margem_lateral), pady=(margem_superior, 10))

tree = ttk.Treeview(root, columns=("Ano", "Semestre"), show="headings")
tree.heading("Ano", text="Ano")
tree.heading("Semestre", text="Semestre")
tree.column("Ano", anchor="center")  # Alinhando a coluna "Ano" no centro
tree.column("Semestre", anchor="center")  # Alinhando a coluna "Semestre" no centro
tree.grid(row=1, column=0, columnspan=4, padx=margem_lateral, pady=10, sticky="ew")

# Botoes
button_salvar = tk.Button(root, text="Salvar", command=salvar, width=20)
button_salvar.grid(row=2, column=0, padx=(margem_lateral, 5), pady=10, sticky="ew")

button_excluir = tk.Button(root, text="Excluir", command=excluir, width=20)
button_excluir.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

button_cancelar = tk.Button(root, text="Cancelar", command=cancelar, width=20)
button_cancelar.grid(row=2, column=2, padx=(5, margem_lateral), pady=10, sticky="ew")

# Configurando para que os botões fiquem no final da tela
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure((0, 1, 2, 3), weight=1)  # Expandindo todas as colunas

# Iniciando o loop principal da aplicação
root.mainloop()