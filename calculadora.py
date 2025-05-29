import tkinter as tk
from math import factorial, comb, perm
from tkinter import messagebox

# Função para inserir números e operadores
def click(valor):
    entrada_var.set(entrada_var.get() + str(valor))

# Função para limpar a entrada
def limpar():
    entrada_var.set("")

# Função para calcular o resultado
def calcular():
    try:
        expressao = entrada_var.get()
        resultado = eval(expressao)
        entrada_var.set(str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", f"Expressão inválida!\n{e}")
        entrada_var.set("")

# Funções combinatórias
def calcular_fatorial():
    try:
        valor = int(entrada_var.get())
        entrada_var.set(str(factorial(valor)))
    except Exception as e:
        messagebox.showerror("Erro", f"Entrada inválida para fatorial!\n{e}")
        entrada_var.set("")

def calcular_combinacao():
    try:
        n, k = map(int, entrada_var.get().split(","))
        entrada_var.set(str(comb(n, k)))
    except Exception as e:
        messagebox.showerror("Erro", "Digite no formato: N,K para combinação.")
        entrada_var.set("")

def calcular_arranjo():
    try:
        n, k = map(int, entrada_var.get().split(","))
        entrada_var.set(str(perm(n, k)))
    except Exception as e:
        messagebox.showerror("Erro", "Digite no formato: N,K para arranjo.")
        entrada_var.set("")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("400x650")
janela.resizable(False, False)
janela.configure(bg="#1e1e1e")

# Centralizar a janela na tela
largura_janela = janela.winfo_reqwidth()
altura_janela = janela.winfo_reqheight()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = int((largura_tela - largura_janela) / 2)
pos_y = int((altura_tela - altura_janela) / 2)
janela.geometry(f"+{pos_x}+{pos_y}")

# Estilo dos botões
estilo_botao = {
    "font": ("Arial", 16, "bold"),
    "bd": 3,
    "relief": tk.RAISED,
    "width": 5,
    "height": 1
}

estilo_botao_operador = {
    "font": ("Arial", 16, "bold"),
    "bd": 3,
    "relief": tk.RAISED,
    "bg": "#FF9500",
    "fg": "white",
    "width": 5,
    "height": 1
}

estilo_botao_especial = {
    "font": ("Arial", 16, "bold"),
    "bd": 3,
    "relief": tk.RAISED,
    "bg": "#A5A5A5",
    "fg": "black",
    "width": 5,
    "height": 1
}

estilo_botao_igual = {
    "font": ("Arial", 16, "bold"),
    "bd": 3,
    "relief": tk.RAISED,
    "bg": "#FF9500",
    "fg": "white",
    "width": 5,
    "height": 1
}

# Campo de entrada
entrada_var = tk.StringVar()
entrada = tk.Entry(
    janela, 
    textvariable=entrada_var,
    font=("Arial", 28),
    bd=10,
    insertwidth=2,
    width=10,
    borderwidth=0,
    bg="#1e1e1e",
    fg="white",
    justify='right',
    highlightthickness=2,
    highlightbackground="#333333",
    highlightcolor="#0078D7"
)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 10), sticky="ew")

# Frame para os botões
botoes_frame = tk.Frame(janela, bg="#1e1e1e")
botoes_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Botões numéricos e operadores básicos - Linha modificada
botoes = [
    ('7', 1, 0, estilo_botao), ('8', 1, 1, estilo_botao), ('9', 1, 2, estilo_botao), ('/', 1, 3, estilo_botao_operador),
    ('4', 2, 0, estilo_botao), ('5', 2, 1, estilo_botao), ('6', 2, 2, estilo_botao), ('*', 2, 3, estilo_botao_operador),
    ('1', 3, 0, estilo_botao), ('2', 3, 1, estilo_botao), ('3', 3, 2, estilo_botao), ('-', 3, 3, estilo_botao_operador),
    ('0', 4, 0, estilo_botao), ('.', 4, 1, estilo_botao), (',', 4, 2, estilo_botao), ('+', 4, 3, estilo_botao_operador),
    ('=', 5, 3, estilo_botao_igual)  # Botão de igual movido para linha 5
]

for (texto, linha, coluna, estilo) in botoes:
    if texto == "=":
        cmd = calcular
    else:
        cmd = lambda x=texto: click(x)
    
    botao = tk.Button(
        botoes_frame,
        text=texto,
        command=cmd,
        **estilo
    )
    botao.grid(row=linha, column=coluna, padx=5, pady=5, ipadx=5, ipady=5)

# Botões de funções especiais - Agora na linha 6
tk.Button(
    botoes_frame,
    text="C",
    command=limpar,
    **estilo_botao_especial
).grid(row=6, column=0, padx=5, pady=5, ipadx=5, ipady=5)

tk.Button(
    botoes_frame,
    text="n!",
    command=calcular_fatorial,
    **estilo_botao_especial
).grid(row=6, column=1, padx=5, pady=5, ipadx=5, ipady=5)

tk.Button(
    botoes_frame,
    text="C(n,k)",
    command=calcular_combinacao,
    **estilo_botao_especial
).grid(row=6, column=2, padx=5, pady=5, ipadx=5, ipady=5)

tk.Button(
    botoes_frame,
    text="A(n,k)",
    command=calcular_arranjo,
    **estilo_botao_especial
).grid(row=6, column=3, padx=5, pady=5, ipadx=5, ipady=5)

# Configuração de peso das linhas/colunas para centralização
for i in range(7):  # Ajustado para 7 linhas
    botoes_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    botoes_frame.grid_columnconfigure(i, weight=1)

janela.mainloop()