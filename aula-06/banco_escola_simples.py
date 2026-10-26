import sqlite3
import tkinter as tk
from tkinter import messagebox

banco = sqlite3.connect("escola75.db")
cursor = banco.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS alunos(nome TEXT, idade INTERGER) ''')

def salvar():
    nome = txt_nome.get()
    idade = txt_idade.get()
    if nome == "" or idade == "":
        messagebox.showwarning("AVISO", "Preencha todos os campos.")
        return
    cursor.execute("INSERT INTO alunos VALUES (?, ?)", (nome, int(idade)))
    banco.commit()
    messagebox.showinfo("Sucesso!", "Aluno cadastrado.")
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)

def listar():
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM alunos")
    for aluno in cursor.fetchall():
        lista.insert(tk.END, f"{aluno[0]} - {aluno[1]} anos")

janela = tk.Tk()
janela.title("Cadastro de alunos")
janela.geometry("300x320")
tk.Label(janela, text = "Nome").pack()
txt_nome = tk.Entry(janela, width = 30)
txt_nome.pack()
tk.Label(janela, text = "Idade").pack()
txt_idade = tk.Entry(janela, width = 30)
txt_idade.pack()
tk.Button(janela, text = "Salvar", command = salvar).pack(pady = 5)
tk.Button(janela, text = "Listar alunos", command = listar).pack()
lista = tk.Listbox(janela, width = 35, height = 10)
lista.pack(pady = 10)
janela.mainloop()
