import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def verificar():
    curso = combo.get()
    messagebox.showinfo("Curso selecionado", f"Você escolheu o curso: \n{curso}")

janela = tk.Tk()
janela.title("Cursos")
janela.geometry("300x180")
janela.resizable(False, False)

tk.Label(janela, text="Escolha um curso", font=("Arial", 12, "bold")).pack(pady=10)

combo = ttk.Combobox(janela, values = ["ADS", "Ciência da computação", "Sistemas de informação"], state="readonly", width=25)
combo.current(0)
combo.pack(pady=10)

tk.Button(janela, text="Confirmar", command=verificar).pack(pady=10)

janela.mainloop()
