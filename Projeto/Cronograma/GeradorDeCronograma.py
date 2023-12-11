import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

root = tk.Tk()
root.title('Cadastro de disciplinas')
root.geometry('1050x600+100+50')

# Calendario 1 (à esquerda)
calendar_left = Calendar(root, selectmode='day', year=2023, month=5, day=22, font='arial 20')
calendar_left.grid(row=1, column=0, padx=20)

# Calendario 2 (à direita)
calendar_right = Calendar(root, selectmode='day', year=2023, month=5, day=22, font='arial 20')
calendar_right.grid(row=1, column=1, padx=20)

# Calendario titulo
Calendar_frame = tk.Frame(root)
Calendar_frame.grid(row=0, column=0, pady=10, padx=20, sticky=tk.W)

label_calendar = tk.Label(Calendar_frame, text="Data de inicio do semestre")
label_calendar.grid()

# Calendario titulo 2
Calendar2_frame = tk.Frame(root)
Calendar2_frame.grid(row=0, column=1, pady=10, padx=20, sticky=tk.W)

label_calendar = tk.Label(Calendar2_frame, text="Data de Termino do semestre")
label_calendar.grid()

# Dias da semana
dias_semana_frame = tk.Frame(root)
dias_semana_frame.grid(row=2, column=0, pady=5, padx=0, sticky=tk.W)

dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']

for idx, dia in enumerate(dias_semana):
    checkbox = tk.Checkbutton(dias_semana_frame, text=dia)
    checkbox.grid(row=0, column=idx, padx=5)

# Combox nivel semestre
semestre_frame = tk.Frame(root)
semestre_frame.grid(row=3, column=0, pady=2, padx=0, sticky=tk.W)

label_semestre = tk.Label(semestre_frame, text="Semestre")
label_semestre.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

Button_semestre = ttk.Combobox(semestre_frame)
Button_semestre['values'] = ('2023.1', '2023.2', '2024.1', '2024.2')
Button_semestre.current(2)
Button_semestre.grid(row=0, column=1, padx=0)

# Combox nivel Disciplina
disciplina_frame = tk.Frame(root)
disciplina_frame.grid(row=4, column=0, pady=2, padx=0, sticky=tk.W)

label_disciplina = tk.Label(disciplina_frame, text="Disciplina")
label_disciplina.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

Button_disciplina = ttk.Combobox(disciplina_frame)
Button_disciplina['values'] = ('Banco de Dados', 'Prog. Front-end', 'Prog. Back-end', 'Dispositivos Movéis')
Button_disciplina.current(2)
Button_disciplina.grid(row=0, column=1, padx=0)

# Botão Executar
btn_executar = tk.Button(root, text="Executar", bg="green")
btn_executar.grid(pady=5, row=3, column=1)

# Botão Sair
btn_sair = tk.Button(root, text="Sair", bg="red")
btn_sair.grid(pady=5, row=4, column=1)

tk.mainloop()