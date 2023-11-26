import tkinter as tk
from tkinter import ttk

def adicionar_filho():
    # Função para adicionar um novo nó filho ao item selecionado na TreeView
    item_selecionado = tree.selection()
    if item_selecionado:
        tree.insert(item_selecionado, 'end', text='Novo Filho', values=('Valor do Filho'))

def adicionar_raiz():
    # Função para adicionar um novo nó raiz à TreeView
    tree.insert('', 'end', text='Nova Raiz', values=('Valor da Raiz'))

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de TreeView")

# Criar um TreeView
tree = ttk.Treeview(root, columns=("valores"))
tree.heading("#0", text="Itens")
tree.heading("valores", text="Valores")
tree.pack()



root.mainloop()
