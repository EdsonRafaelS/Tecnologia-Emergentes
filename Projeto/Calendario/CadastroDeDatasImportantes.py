import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import sys
sys.path.append('C:/TDS - 3 MODULO/TECNOLOGIAS EMERGENTES/SEGUNDO BIMESTRE/Projeto')

from BancoDeDados import conecta_bd
# Importe a função adicionar_data_ao_banco do seu módulo BancoDeDados
from BancoDeDados import adicionar_data_ao_banco
from BancoDeDados import apagar_data_do_banco
from BancoDeDados import atualizar_data_no_banco
from BancoDeDados import carregar_dados_do_banco

window = tk.Tk()
window.title('Geração de cronogramas')

# Função para popular a Treeview com dados do banco
def carregar_dados():
    # Limpar dados existentes na Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Buscar dados do banco de dados
    dados = carregar_dados_do_banco()

    # Popular Treeview com os dados obtidos
    for linha in dados:
        tree.insert("", "end", text=linha[0], values=(linha[1], linha[2], linha[3]))



# Função para adicionar a linha no Treeview e no banco de dados
def adicionar_data():
    data = cal.get_date()
    descricao = desc_entry.get()
    tipo_data = type_combobox.get()

    if not (descricao and tipo_data):
        messagebox.showwarning('Aviso', 'Preencha todos os campos antes de adicionar.')
        return

    # Adicionar à tabela Datas_Importantes no banco de dados e obter o ID
    id_data_importante = adicionar_data_ao_banco(data, descricao, tipo_data)

    if id_data_importante is not None:
        # Adicionar à Treeview apenas se o ID não for nulo
        tree.insert("", "end", text=id_data_importante, values=(data, descricao, tipo_data))

        # Limpar os campos após adicionar
        desc_entry.delete(0, tk.END)
        type_combobox.set('')  # Pode definir um valor padrão se desejar

# Função para remover a linha selecionada no Treeview e no banco de dados
def remover_data():
    selected_item = tree.selection()
    if selected_item:
        # Obter o ID da linha selecionada diretamente do Treeview
        id_data_importante = tree.item(selected_item, 'text')

        # Certifique-se de que o ID não está vazio
        if id_data_importante:
            # Remover a linha do banco de dados
            apagar_data_do_banco(int(id_data_importante))

            # Remover a linha do Treeview
            tree.delete(selected_item)
        else:
            messagebox.showwarning('Aviso', 'ID da linha está vazio.')
    else:
        messagebox.showwarning('Aviso', 'Selecione uma linha para remover.')


# Função para alterar a linha selecionada no Treeview
def alterar_dados():
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showwarning('Aviso', 'Selecione uma linha para editar.')
        return

    # Obter dados da linha selecionada
    data, descricao, tipo_data = tree.item(selected_item, 'values')

    # Remover a linha selecionada da Treeview
    tree.delete(selected_item)

    # Preencher os campos com os dados existentes
    desc_entry.delete(0, tk.END)
    desc_entry.insert(0, descricao)
    type_combobox.set(tipo_data)

    # Atualizar a função do botão "Adicionar" para editar a linha
    def adicionar_data():
        # Obter os novos dados dos campos
        nova_data = cal.get_date()
        nova_descricao = desc_entry.get()
        novo_tipo_data = type_combobox.get()

        if not (nova_descricao and novo_tipo_data):
            messagebox.showwarning('Aviso', 'Preencha todos os campos antes de adicionar.')
            return

        # Adicionar à tabela Datas_Importantes no banco de dados e obter o ID
        id_data_importante = adicionar_data_ao_banco(nova_data, nova_descricao, novo_tipo_data)

        if id_data_importante is not None:
            # Adicionar à Treeview apenas se o ID não for nulo
            tree.insert("", "end", text=id_data_importante, values=(nova_data, nova_descricao, novo_tipo_data))

            # Limpar os campos após adicionar
            desc_entry.delete(0, tk.END)
            type_combobox.set('')  # Pode definir um valor padrão se desejar

    # Atualizar a função do botão "Adicionar"
    button_AdicionarData.configure(command=adicionar_data)

# Função para cancelar e fechar a janela
def cancelar():
    window.destroy()

cal = Calendar(window, selectmode='day', year=2023, month=11, day=1)
cal.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tk.Label(window, text='Descrição da data:').grid(row=1, column=0, padx=10, pady=10)
desc_entry = tk.Entry(window)
desc_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text='Tipo de data:').grid(row=2, column=0, padx=10, pady=10)
type_combobox = ttk.Combobox(window,state="readonly", values=['Feriado', 'Evento', 'Outro'])
type_combobox.grid(row=2, column=1, padx=10, pady=10)

tree = ttk.Treeview(window, columns=('Data', 'Descrição', 'Tipo de data'), show='headings')
tree.heading('Data', text='Data')
tree.heading('Descrição', text='Descrição')
tree.heading('Tipo de data', text='Tipo de data')
tree.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# Vincular a função carregar_dados ao evento de mapeamento da Treeview
tree.bind("<Map>", lambda event: carregar_dados())

button_AdicionarData = ttk.Button(window, text='Adicionar data', command=adicionar_data)
button_AdicionarData.grid(row=4, column=0, padx=10, pady=10)

button_RemoverData = ttk.Button(window, text='Remover data', command=remover_data)
button_RemoverData.grid(row=4, column=1, padx=10, pady=10)

button_AlterarData = ttk.Button(window, text='Alterar data', command=alterar_dados)
button_AlterarData.grid(row=4, column=2, padx=10, pady=10)

button_Cancelar = ttk.Button(window, text='Cancelar', command=cancelar)
button_Cancelar.grid(row=4, column=3, padx=10, pady=10)

window.mainloop()

