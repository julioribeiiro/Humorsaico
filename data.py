import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import threading

i=0

def background(func):#---------ESTA FUNÇAO PERMITE A EXECUÇAO DE UMA FUNÇAO(NO CASO A ATUALIZAR) NO BACKGROUND DO TKINTER
    th = threading.Thread(target = func)
    th.start()

#CRIANDO LISTA PARA GRAFICO DE BARRAS
list_X = []
list_Y = []
lista = []

#CRIANDO LISTA PARA GRAFICO DE PIZZA DO 1 PERIODO
list_euforico=[]
list_feliz=[]
list_raivoso=[]
list_triste=[]
list_entediado=[]
list_ansioso=[]

#CRIANDO LISTA PARA GRAFICO DE PIZZA DO 2 PERIODO
list_euforico2=[]
list_feliz2=[]
list_raivoso2=[]
list_triste2=[]
list_entediado2=[]
list_ansioso2=[]

#CRIANDO LISTA PARA GRAFICO DE PIZZA DO 3 PERIODO
list_euforico3=[]
list_feliz3=[]
list_raivoso3=[]
list_triste3=[]
list_entediado3=[]
list_ansioso3=[]


#SALVANDO O EXCEL NUMA VARIAVEL
data =  'arquivos/banco_dados_branco.xlsx'
x1 = pd.ExcelFile(data)
df1 = x1.parse('Transformed by JSON-CSV.COM')
t = df1.shape

#SALVANDO O EXCEL NUMA VARIAVEL SEMANAL
semana = 'arquivos/data.xlsx'
x2 = pd.ExcelFile(semana)
df2 = x2.parse('Transformed by JSON-CSV.COM')
t1 = df2.shape

#CRIANDO FUNÇOES PARA DETERMINADO TIPOS
def cc():
    #FAZENDO O GRAFICO DE PIZZA PARA O CURSO DE CC
    labels = 'Euforico', 'Feliz', 'Entediado', 'Ansioso', 'Raivoso', 'Triste'
    sizes = sum(list_euforico),sum(list_feliz),sum(list_entediado),sum(list_ansioso),sum(list_raivoso),sum(list_triste)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    
    plt.show()

def design():
    #FAZENDO O GRAFICO DE PIZZA PARA O CURSO DE DESIGN
    labels = 'Euforico', 'Feliz', 'Entediado', 'Ansioso', 'Raivoso', 'Triste'
    sizes = sum(list_euforico2),sum(list_feliz2),sum(list_entediado2),sum(list_ansioso2),sum(list_raivoso2),sum(list_triste2)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    
    plt.show()

def periodo1():
    #FAZENDO O GRAFICO DE PIZZA PARA O 1 PERIODO
    labels = 'Euforico', 'Feliz', 'Entediado', 'Ansioso', 'Raivoso', 'Triste'
    sizes = sum(list_euforico),sum(list_feliz),sum(list_entediado),sum(list_ansioso),sum(list_raivoso),sum(list_triste)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    
    plt.show()
    
def periodo2():
    #FAZENDO O GRAFICO DE PIZZA PARA O 2 PERIODO
    labels = 'Euforico', 'Feliz', 'Entediado', 'Ansioso', 'Raivoso', 'Triste'
    sizes = sum(list_euforico2),sum(list_feliz2),sum(list_entediado2),sum(list_ansioso2),sum(list_raivoso2),sum(list_triste2)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    
    plt.show()

def periodo3():
    #FAZENDO O GRAFICO DE PIZZA PARA O 3 PERIODO
    labels = 'Euforico', 'Feliz', 'Entediado', 'Ansioso', 'Raivoso', 'Triste'
    sizes = sum(list_euforico3),sum(list_feliz3),sum(list_entediado3),sum(list_ansioso3),sum(list_raivoso3),sum(list_triste3)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    
    plt.show()

def euforico():
    #SALVANDO NAS LISTAS O HUMOR DA PESSOA
    global i
    global list_X
    global list_Y
    while i < t[0]:
        list_X.append(df1.loc[i, '|__nome'])
        list_Y.append(df1.loc[i, '|__humor__euforico'])
        i = i+1

def feliz():
    #SALVANDO NAS LISTAS O HUMOR DA PESSOA
    global i
    global list_X
    global list_Y
    while i < t[0]:
        list_X.append(df1.loc[i, '|__nome'])
        list_Y.append(df1.loc[i, '|__humor__feliz'])
        i = i+1

def entediado():
    #SALVANDO NAS LISTAS O HUMOR DA PESSOA
    global i
    global list_X
    global list_Y
    while i < t[0]:
        list_X.append(df1.loc[i, '|__nome'])
        list_Y.append(df1.loc[i, '|__humor__entediado'])
        i = i+1

def ansioso():
    #SALVANDO NAS LISTAS O HUMOR DA PESSOA
    global i
    global list_X
    global list_Y
    while i < t[0]:
        list_X.append(df1.loc[i, '|__nome'])
        list_Y.append(df1.loc[i, '|__humor__ansioso'])
        i = i+1

def raivoso():
    #SALVANDO NAS LISTAS O HUMOR DA PESSOA
    global i
    global list_X
    global list_Y
    while i < t[0]:
        list_X.append(df1.loc[i, '|__nome'])
        list_Y.append(df1.loc[i, '|__humor__raivoso'])
        i = i+1

def triste():
    #SALVANDO NAS LISTAS O HUMOR DA PESSOA
    global i
    global list_X
    global list_Y
    while i < t[0]:
        list_X.append(df1.loc[i, '|__nome'])
        list_Y.append(df1.loc[i, '|__humor__triste'])
        i = i+1





#PSICOLOGA IRA ESCOLHER UMA DESSAS OPÇOES

#SALVANDO EM LISTAS
def procura():
    global et_x
    x = int(et_x.get())
    x -= 2
    print(x)
    list_Y.append(df1.loc[x, '|__nome'])
    list_X.append(df1.loc[x, '|__humor__euforico'])
    lista.append(df2.loc[x, '|__humor__euforico'])
    list_X.append(df1.loc[x, '|__humor__feliz'])
    lista.append(df2.loc[x, '|__humor__feliz'])
    list_X.append(df1.loc[x, '|__humor__entediado'])
    lista.append(df2.loc[x, '|__humor__entediado'])
    list_X.append(df1.loc[x, '|__humor__ansioso'])
    lista.append(df2.loc[x, '|__humor__ansioso'])
    list_X.append(df1.loc[x, '|__humor__raivoso'])
    lista.append(df2.loc[x, '|__humor__raivoso'])
    list_X.append(df1.loc[x, '|__humor__triste'])
    lista.append(df2.loc[x, '|__humor__triste'])
    humor=list_Y[0]
    

    #CRIANDO GRAFICO DE PIZZA GERAL
    labels = 'Euforico', 'Feliz', 'Entediado', 'Ansioso', 'Raivoso', 'Triste'
    sizes = list_X[0],list_X[1],list_X[2],list_X[3],list_X[4],list_X[5]
    print(sizes)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    
    plt.show()
    
    #CRIANDO GRAFICO DE PIZZA SEMANAL
    labels = 'Euforico', 'Feliz', 'Entediado', 'Ansioso', 'Raivoso', 'Triste'
    sizes = lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    
    plt.show()

def ativa_bt():
    global confirma_bt
    confirma_bt["command"] = background(procura)


#PSICOLOGA QUIS ESCOLHER UMA PESSOA EM ESPECIFICA
def pessoa():
    global confirma_bt
    global et_x
    pessoa_pg = Toplevel()
    pessoa_pg.geometry("600x300+600+300")
    digite_lb = Label(pessoa_pg, text = "Digite o numero da pessoa(na tabela excel)\n que voce quer procurar")
    et_x = Entry(pessoa_pg)
    digite_lb.grid(row=0,column=0)
    et_x.grid(row=1,column=0)
    confirma_bt = Button(pessoa_pg, text = "Confirmar", command = ativa_bt)
    confirma_bt.grid(row = 2, column = 0)


#PSICOLOGA ESCOLHEU TODAS AS PESSOAS
def geral():
    humor=str(input('Escolha o humor que deseja prcurar:')).capitalize()
    #CHAMANDO AS FUNÇOES PARA CRIAR O GRAFICO
    if humor=="Euforico":
        euforico()
        humor="Euforia"
    elif humor == "Feliz":
        feliz()
        humor="Felicidade"
    elif humor == "Entediado":
        entediado()
        humor="Tedio"
    elif humor == "Ansioso":
        ansioso()
        humor="Ansiedade"
    elif humor == "Raivoso":
        raivoso()
        humor="Raiva"
    elif humor == "Triste":
        triste()
        humor="Tristeza"
    
    #CRIANDO O GRAFICO DE BARRAS DOS HUMORES
    tumbar = np.arange(len(list_X))
    fig, ax = plt.subplots()
    ax.barh(tumbar, list_Y , align='center')
    ax.set_yticks(tumbar)
    ax.set_yticklabels(list_X)
    ax.invert_yaxis()
    ax.set_xlabel(humor)
    ax.set_title("Grafico de " + humor)
    plt.show()

#PSICOLOGA ESCOLHEU CIRAR GRAFICO POR PERIODO
def periodo():
    
    #ELA IRA ESCOLHER  QUAL PERIODO IRA SELECIONAR
    x=int(input('Escolha qual periodo deseja procurar:'))
    
    #FAZENDO UM LOOP PARA ADICIONAR NAS LISTA
    while i<t[0]:
        solo=(df1.loc[i, '|__periodo'])
        if solo == 1:
            list_euforico.append(df1.loc[i, '|__humor__euforico'])
            list_feliz.append(df1.loc[i, '|__humor__feliz'])
            list_entediado.append(df1.loc[i, '|__humor__entediado'])
            list_ansioso.append(df1.loc[i, '|__humor__ansioso'])
            list_raivoso.append(df1.loc[i, '|__humor__raivoso'])
            list_triste.append(df1.loc[i, '|__humor__triste'])
        
        elif solo == 2:
            list_euforico2.append(df1.loc[i, '|__humor__euforico'])
            list_feliz2.append(df1.loc[i, '|__humor__feliz'])
            list_entediado2.append(df1.loc[i, '|__humor__entediado'])
            list_ansioso2.append(df1.loc[i, '|__humor__ansioso'])
            list_raivoso2.append(df1.loc[i, '|__humor__raivoso'])
            list_triste2.append(df1.loc[i, '|__humor__triste'])
        
        elif solo == 3:
            list_euforico3.append(df1.loc[i, '|__humor__euforico'])
            list_feliz3.append(df1.loc[i, '|__humor__feliz'])
            list_entediado3.append(df1.loc[i, '|__humor__entediado'])
            list_ansioso3.append(df1.loc[i, '|__humor__ansioso'])
            list_raivoso3.append(df1.loc[i, '|__humor__raivoso'])
            list_triste3.append(df1.loc[i, '|__humor__triste'])
        i+=1
        
    #CHAMANDO AS FUNÇOES PARA GERAR OS GRAFICOS    
    if x == 1:
        periodo1()
    elif x==2:
        periodo2()
    elif x==3:
        periodo3()


#PSICOLOGA ESCOLHEU GERAR GRAFICOS POR CURSO
def curso():
    
    #PSICOLOGA IRA SELECIONAR O CURSO DESEJADO
    x=int(input('Escolha qual curso deseja procurar(1 para CC, 2 para Design):'))
    
    #CIRANDO UM LOOP PARA ADICIONAR NAS LISTAS
    while i<t[0]:
        vrau=(df1.loc[i, '|__curso'])
        if vrau==1:
            list_euforico.append(df1.loc[i, '|__humor__euforico'])
            list_feliz.append(df1.loc[i, '|__humor__feliz'])
            list_entediado.append(df1.loc[i, '|__humor__entediado'])
            list_ansioso.append(df1.loc[i, '|__humor__ansioso'])
            list_raivoso.append(df1.loc[i, '|__humor__raivoso'])
            list_triste.append(df1.loc[i, '|__humor__triste'])
        elif vrau==2:
            list_euforico2.append(df1.loc[i, '|__humor__euforico'])
            list_feliz2.append(df1.loc[i, '|__humor__feliz'])
            list_entediado2.append(df1.loc[i, '|__humor__entediado'])
            list_ansioso2.append(df1.loc[i, '|__humor__ansioso'])
            list_raivoso2.append(df1.loc[i, '|__humor__raivoso'])
            list_triste2.append(df1.loc[i, '|__humor__triste'])
        i+=1
    
    
    #CHAMANDO AS FUNÇOES PARA GERAR OS GRAFICOS
    if x==1:
        cc()
    elif x==2:
        design()


root = Tk()
root.geometry("+600+300")

pessoa_bt = Button(root, text = "Pessoa", command = pessoa)
pessoa_bt.grid(row = 0, column = 0)

geral_bt = Button(root, text = "Geral", command = geral)
geral_bt.grid(row = 0, column = 1)

periodo_bt = Button(root, text = "Periodo", command = periodo)
pessoa_bt.grid(row = 0, column = 2)

curso_bt = Button(root, text = "Curso", command = curso)
curso_bt.grid(row = 0, column = 3)


root.mainloop()