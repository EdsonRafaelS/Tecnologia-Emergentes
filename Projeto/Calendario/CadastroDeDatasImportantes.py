import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk

root = tk.Tk()
root.title('Cadastro de Datas Importantes')
root.geometry('900x600')

#Frame principal
frame_principal = tk.Frame(root, borderwidth=2, relief='solid')
frame_principal.grid(row=0, column=0, padx=25, pady=25)
frame_principal.grid_columnconfigure(3, weight=300)

#Label de Inicio
label_text = tk.Label(frame_principal, text='Selecione a data desejada:', font='Arial 14')
label_text.grid(row=0, column=0, pady=20)

#Calendario da pagina
Caledario = Calendar(frame_principal, selectmode= 'day', year= 2023, month= 5, day=22, font='Arial 20')
Caledario.grid(row=2, columnspan=4)

#Texto da data
label_data = tk.Label(frame_principal, text='Descrição da data:',font='Arial 14')
label_data.grid(row=3, column=1, padx=20, pady=20)

#Entry da data
entry_data = tk.Entry(frame_principal, font='Arial 14')
entry_data.grid(row=3, column=2, padx=20, pady=20)

#Texto do Tipo de data
label_TipoDeData = tk.Label(frame_principal, text='Tipo de Data:', font='Arial 14')
label_TipoDeData.grid(row=4, column=1, padx=20, pady=20)

#Combobox Tipo de data
combobox_TipoDeDado = ttk.Combobox(frame_principal, font='Arial 14')
combobox_TipoDeDado['value'] = ('Sabado Letivo', 'Feriado', 'Sabado Reposição')
combobox_TipoDeDado.current(2)
combobox_TipoDeDado.grid(row=4, column=2, padx=20, pady=20)

#Treeview  Dados
colunas = ('Data', 'Descrição', 'Tipo de Alerta')
treeview_dados = ttk.Treeview(frame_principal, columns=colunas)

# Configurar os cabeçalhos das colunas
for coluna in colunas:
    treeview_dados.heading(coluna, text=coluna)

# Exibir o TreeView
treeview_dados.grid(rowspan=2, columnspan=3, row=4, column=0, padx=8)

root.grid_columnconfigure(3, weight=300) #Posicionamento fixo da pagina
root.grid_rowconfigure(1, weight=600) #Posicionamento fixo da pagina
root.mainloop()