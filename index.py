from datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk

# ==============Janela===============#
janela = Tk()
janela.title("Cadastro de visitantes")
janela.geometry("1000x600")
janela.configure(background="gray10")
janela.resizable(width=False, height=False)
#janela.attributes("-alpha", 0.9)

# =============Icon da janela========#
janela.iconbitmap("images/ico.ico")

# ==========Carregando logo==========#
logo = PhotoImage(file='images/181548.png')
fotoUsuario = PhotoImage(file='images/face.png')

# ===========================Widgets===============================#
LeftFrame = Frame(janela, width=200, height=1000,  bg="gray16", relief="raise")
LeftFrame.pack(side=LEFT)

RightFtame = Frame(janela, width=790, height=1000,
                   bg="gray25", relief="raise")
RightFtame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="gray16")
LogoLabel.place(x=10, y=20)

fotoLebel = Label(RightFtame, image=fotoUsuario, bg="gray16")

# .place(x=640, y=30)


# =========================== Botôes menu ============================
botao = ttk.Button(LeftFrame, text="Novo visitante ", width=30)
botao.place(x=5, y=200)

botao = ttk.Button(LeftFrame, text="Cadastra funcionário", width=30)
botao.place(x=5, y=240)

botao = ttk.Button(LeftFrame, text="Novo morador", width=30)
botao.place(x=5, y=280)

botao = ttk.Button(LeftFrame, text="Informação do condomínio", width=30)
botao.place(x=5, y=320)

botao = ttk.Button(LeftFrame, text="Relatório", width=30)
botao.place(x=5, y=360)

botao = ttk.Button(LeftFrame, text="Agendamento", width=30)
botao.place(x=5, y=400)

# =======================Cadastro===========================
# Entrada nome
nomeVisitante = Label(RightFtame, text="Nome:", font=(
    "Century  Gothic", 15), bg="gray18", fg="white")
nomeVisitante.place(x=50, y=100, height=25)

entradaNome = ttk.Entry(RightFtame, width=30)
entradaNome.place(x=115, y=100, height=25)

# Eentrada RG
numeroGR = Label(RightFtame, text="RG: ", font=(
    "areal", 15), bg="gray18", fg="white")
numeroGR.place(x=310, y=100)

entradaRG = ttk.Entry(RightFtame, width=20)
entradaRG.place(x=360, y=100, height=25)

# Local de Destino
localDeDestino = Label(RightFtame, text="Bloco: ", font=(
    "Century  Gothic", 15), bg="gray18", fg="white")
localDeDestino.place(x=50, y=140, height=25)

entradaDestino = ttk.Entry(RightFtame, width=10)
entradaDestino.place(x=120, y=140, height=25)

# Local da sala
localDaSala = Label(RightFtame, text="Sala: ", font=(
    "Century  Gothic", 15), bg="gray18", fg="white")
localDaSala.place(x=200, y=140, height=25)

entradaDestino = ttk.Entry(RightFtame, width=10)
entradaDestino.place(x=260, y=140, height=25)

# Visitado
visitado = Label(RightFtame, text="visitado: ", font=(
    "Century  Gothic", 15), bg="gray18", fg="white")
visitado.place(x=50, y=180)

entradavisitado = ttk.Entry(RightFtame, width=65)
entradavisitado.place(x=138, y=180, height=25)

# Obs:
obs = Label(RightFtame, text="Obs: ", font=(
    "Century  Gothic", 15), bg="gray18", fg="white")
obs.place(x=50, y=450)

entradaObs = ttk.Entry(RightFtame, width=100)
entradaObs.place(x=110, y=450, height=110)

# Pesquisar visitante
Pesquisar = Label(RightFtame, text="Pesquisar: ", font=(
    "areal", 15), bg="gray18", fg="white")
Pesquisar.place(x=50, y=50)

entradaRG = ttk.Entry(RightFtame, width=60)
entradaRG.place(x=160, y=50, height=25)

# Telefone
telefone = Label(RightFtame, text="Telefone: ", font=(
    "Century  Gothic", 15), bg="gray18", fg="white")
telefone.place(x=50, y=230)

entradaTelefone = ttk.Entry(RightFtame, width=30)
entradaTelefone.place(x=147, y=230, height=25)

# placa do veículo
placa = Label(RightFtame, text="Placa do veículo: ", font=(
    "Century  Gothic", 15), bg="gray18", fg="white")
placa.place(x=50, y=265)

entradaPlaca = ttk.Entry(RightFtame, width=19)
entradaPlaca.place(x=215, y=265, height=25)

# check
bloqueado = ttk.Checkbutton(
    RightFtame, text="Bloqueado"
).place(x=50, y=310)

motorista = ttk.Checkbutton(
    RightFtame, text="Motorista"
).place(x=140, y=310)

# Tipo de visita

tipo = Label(RightFtame, text="Tipo de visita: ", font=(
    "Century  Gothic", 11), bg="gray18", fg="white")
tipo.place(x=50, y=350)

valor_a = IntVar()
ra_1 = ttk.Radiobutton(RightFtame, text="Delivery",
                       variable=valor_a, value=1)
ra_1.place(x=147, y=350)

valor_b = IntVar()
ra_1 = ttk.Radiobutton(RightFtame, text="visita domiciliar",
                       variable=valor_b, value=2)
ra_1.place(x=230, y=350)

janela.mainloop()
