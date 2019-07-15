# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:04:39 2019

@author: Aluno
"""
from tkinter import *
import time
import threading
import json
import random


#--------------VARIAVEIS-------------------

linhas = 1
completo = list()
completo_arquivo = list()
cor_aux = 'orange'
x = 10
y = 10
cont = 0
dalt_ativado = 0
n_verde = 0
n_vermelho = 0
n_roxo = 0
n_laranja = 0
n_azul = 0
n_amarelo = 0
sel = 'w'

#--------CONFIGURAÇÕES GERAIS DAS PAGINAS----------------

cor_verde = "green"
cor_vermelho = "red"
cor_azul = "blue"
cor_rosa = "purple"
cor_laranja = "orange"
cor_cinza = "#C9C4C0"
cor_amarelo = "yellow"
cor_braco = "white"
cor_preto = "black"
tamanho_pagina = "1368x768+0+0"



def info_arquivo():#-------TRANSFORMA A VARIAVEL DE LABELS EM ARQUIVO, PARA PODER REABRIR A PAGINA DEPOIS DE PINTADA
    global completo
    completo = []
    texto = open("arquivos/logo2.txt", "r")
    for i in texto:#----------PEGANDO LINHA A LINHA DO ARQUIVO
        completo.append(list(i))
    texto.close()

info_arquivo()

for i in range (len(completo)):#-----------TRANSFORMANDO ARQUIVO MATRIZ EM UMA LISTA SEPARADA POR /N
    for j in range (len(completo[i])):
        completo_arquivo.append(completo[i][j])


def background(func):#---------ESTA FUNÇAO PERMITE A EXECUÇAO DE UMA FUNÇAO(NO CASO A ATUALIZAR) NO BACKGROUND DO TKINTER
    th = threading.Thread(target = func)
    th.start()

#-------------ESTA FUNCAO SERVE PARA ATUALIZAR A LEGENDA------------

def cria_legenda():
    global n_verde
    global n_vermelho
    global n_roxo
    global n_laranja
    global n_azul
    global n_amarelo
    global euforico_ama
    n_verde = 0
    n_vermelho = 0
    n_roxo = 0
    n_laranja = 0
    n_azul = 0
    n_amarelo = 0
    
    with open("arquivos/banco_dados.json") as aaa:
        biblioteca = json.load(aaa)
    for i in biblioteca:
        n_laranja += biblioteca[i]["humor"]["euforico"]
        n_verde += biblioteca[i]["humor"]["feliz"]
        n_roxo += biblioteca[i]["humor"]["entediado"]
        n_amarelo += biblioteca[i]["humor"]["ansioso"]
        n_vermelho += biblioteca[i]["humor"]["raivoso"]
        n_azul += biblioteca[i]["humor"]["triste"]   
    
def scoreboard(rfid, biblioteca):
    if rfid == "0":
        score = "0"
    else:
        score = str(biblioteca[rfid]["score"])
    if len(score) == 1:
        score = "0000"+str(score)
    elif len(score) == 2:
        score = "000"+str(score)
    elif len(score) == 3:
        score = "00"+str(score)
    elif len(score) == 4:
        score = "0"+str(score)

    return score


#-----------------INTERFACE----------

def abre_parte2():
    global seta_pisca
    global usuario

    interface = Toplevel()
    interface.title("HUMORSAICO")
    interface.geometry(tamanho_pagina)
    interface["bg"] = cor_preto


    #-----FUNCOES-----------

    def grava_humor(qual):
        global rfid
        global dados
        dados[rfid]["humor"][qual] += 1
        with open ('arquivos/banco_dados.json', 'w') as semanal:
            json.dump(dados, semanal)
        with open ('arquivos/banco_dados_global.json', 'w') as total:
            json.dump(dados, total)

    def funcverde():
        global cor
        cor = "Ve"
        abre_janela()
        grava_humor("feliz")

    def funcvermelho():
        global cor
        cor = "V"
        abre_janela()
        grava_humor("raivoso")

    def funcrosa():
        global cor
        cor = "R"
        abre_janela()
        grava_humor("entediado")
        
    def funclaranja():
        global euforico_ama
        global cor
        cor = "La"
        abre_janela()
        grava_humor("euforico")
        
    def funcazul():
        global cor
        cor = "A"
        abre_janela()
        grava_humor("triste")
        
    def funcamarelo():
        global cor
        cor = "Am"
        abre_janela()
        grava_humor("ansioso")


    def funcdaltonico():
        global cor_verde
        global cor_vermelho
        global cor_rosa
        global cor_laranja
        global cor_azul
        global cor_amarelo
        global onOff
        global switchOn
        global dalt_ativado
        onOff["image"] = switchOn
        onOff.place(x = 1235, y = 60)
        cor_verde = "#EEC900"
        cor_vermelho = "#8B7500"
        cor_rosa = "#0000EE"
        cor_laranja = "#CDAD00"
        cor_azul = "#1874CD"
        cor_amarelo = "#FFFF00"
        dalt_ativado = 1
        time.sleep(1)


    def funcdaltonico1():
        global cor_verde
        global cor_vermelho
        global cor_rosa
        global cor_laranja
        global cor_azul
        global cor_amarelo
        global onOff
        global switchOff
        global dalt_ativado
        onOff["image"] = switchOff
        cor_verde = "green"
        cor_vermelho = "red"
        cor_rosa = "purple"
        cor_laranja = "orange"
        cor_azul = "blue"
        cor_amarelo = "yellow"
        dalt_ativado = 0
        time.sleep(1)

    def abre_instru():
        print("Abriu")
        instru = Toplevel()
        instru.geometry("+300+505")
        instru["background"] = cor_preto

        instrucoes_img = PhotoImage(file = "imagens/regras.png")
        instrucoes_lb = Label(instru, image = instrucoes_img, bg = cor_preto)
        instrucoes_lb.pack()
        info = [1]
        time.sleep(1)
        while info[0] != 'A':
            data = open('arquivos/data.txt', 'r')#-----LE-SE O ARQUIVO QUE CONTEM A INFORMAÇAO DO ARDUINO(POTENCIOMETROS PARA POSICAO E CLICK DE BOTAO)
            for i in data:
                info = i.split(',')
        instru.destroy()





    #----FUNÇÃO QUE VAI PERMITIR A SELEÇAO DE HUMOR UTILIZANDO ARDUINO------------------------------------------

    def selecionador():
        global seta_pisca
        global usuario
        global rfid
        global dalt_ativado
        global switchOff
        global switchOn
        global onOff
        dalt_ativado = 0
#------------------------CARREGAMENTO DE IMAGENS-------------------------------------------------

        #-------------------INTERFACE INTEIRA---------------------------------------------


        inteira_image = PhotoImage(file = "imagens/interface2.png")
        inteira = Label(interface, image = inteira_image)
        inteira.pack()

        seta = PhotoImage(file = "imagens/clique_inst.png")
        seta_pisca = Label(interface, image = seta, bg = cor_preto)
        seta2_pisca = Label(interface, image = seta, bg = cor_preto)
        seta2_pisca.place(x = 450, y = 550)

        switchOn = PhotoImage(file = "imagens/SwitchOn.png")
        switchOff = PhotoImage(file = "imagens/SwitchOff.png")
        onOff = Label(interface, image = switchOff, bg = cor_preto)
        onOff.place(x = 1235, y = 60)

        euforico_amarelo = PhotoImage(file = "imagens/euforico.png")
        feliz_amarelo = PhotoImage(file = "imagens/feliz.png")
        entediado_amarelo = PhotoImage(file = "imagens/entediado.png")
        ansioso_amarelo = PhotoImage(file = "imagens/ansioso.png")
        raivoso_amarelo = PhotoImage(file = "imagens/raivoso.png")
        triste_amarelo = PhotoImage(file = "imagens/triste.png")
        
        euforico_ama = Label(interface, image = euforico_amarelo, bg = cor_preto)
        feliz_ama = Label(interface, image = feliz_amarelo, bg = cor_preto)
        entediado_ama = Label(interface, image = entediado_amarelo, bg = cor_preto)
        ansioso_ama = Label(interface, image = ansioso_amarelo, bg = cor_preto)
        raivoso_ama = Label(interface, image = raivoso_amarelo, bg = cor_preto)
        triste_ama = Label(interface, image = triste_amarelo, bg = cor_preto)

        
        
        
        def pisca_seta():
            global sel
            global seta_pisca
            while sel != 'A':
                seta_pisca.place(x = 450, y = 550)
                time.sleep(1)
                seta_pisca.place(x = 10000, y = 430)
                time.sleep(1)

        background(pisca_seta)
        

        while True:
            #------------------CONFIGURACOES LARANJA-----------------------------------


            laranja = PhotoImage(file = "imagens/glaranja.png")
            laranja1 = PhotoImage(file = "imagens/glaranja1.png")
            laranja2 = PhotoImage(file = "imagens/glaranja2.png")
            laranja3 = PhotoImage(file = "imagens/glaranja3.png")

            laranja_lb = Label(interface, image = laranja, bg = cor_preto)
            laranja_lb.place(x = 185, y = 154)
            
            #---------------------CONFICURACOES VERDE----------------------------------------------------


            verde = PhotoImage(file = "imagens/gverde.png")
            verde1 = PhotoImage(file = "imagens/gverde1.png")
            verde2 = PhotoImage(file = "imagens/gverde2.png")
            verde3 = PhotoImage(file = "imagens/gverde3.png")

            verde_lb = Label(interface, image = verde, bg = cor_preto)
            verde_lb.place(x = 360, y = 154)


            #-------------------------CONFIGURACOES ROXO-------------------------------------------


            rosa = PhotoImage(file = "imagens/grosa.png")
            rosa1 = PhotoImage(file = "imagens/grosa1.png")
            rosa2 = PhotoImage(file = "imagens/grosa2.png")
            rosa3 = PhotoImage(file = "imagens/grosa3.png")

            rosa_lb = Label(interface, image = rosa, bg = cor_preto)
            rosa_lb.place(x = 535, y = 154)


            #---------------------CONFIGURACOES AMARELO---------------------------------------------


            amarelo = PhotoImage(file = "imagens/gamarelo.png")
            amarelo1 = PhotoImage(file = "imagens/gamarelo1.png")
            amarelo2 = PhotoImage(file = "imagens/gamarelo2.png")
            amarelo3 = PhotoImage(file = "imagens/gamarelo3.png")

            amarelo_lb = Label(interface, image = amarelo, bg = cor_preto)
            amarelo_lb.place(x = 710, y = 154)


            #------------------COFIGURACOES VERMELHO----------------------------------------------------


            vermelho = PhotoImage(file = "imagens/gvermelho.png")
            vermelho1 = PhotoImage(file = "imagens/gvermelho1.png")
            vermelho2 = PhotoImage(file = "imagens/gvermelho2.png")
            vermelho3 = PhotoImage(file = "imagens/gvermelho3.png")

            vermelho_lb = Label(interface, image = vermelho, bg = cor_preto)
            vermelho_lb.place(x = 885, y = 154)


            #------------------CONFIGURACOES AZUL------------------------------------------


            azul = PhotoImage(file = "imagens/gazul.png")
            azul1 = PhotoImage(file = "imagens/gazul1.png")
            azul2 = PhotoImage(file = "imagens/gazul2.png")
            azul3 = PhotoImage(file = "imagens/gazul3.png")

            azul_lb = Label(interface, image = azul, bg = cor_preto)
            azul_lb.place(x = 1063, y = 154)

            seta2 = PhotoImage(file = "imagens/Setinha.png")
            seta_lb = Label(interface, image = seta2, bg = cor_preto)

            nome_usuario = Label(interface, text = 'Bem vindo {}'.format(usuario), bg = cor_preto, fg = 'white', font = "Minecraft 20")
            nome_usuario.place(x = 535, y = 92)




            #----------------FIM DE IMAGENS----------------------------------------

            data = open('arquivos/data.txt', 'r')#-----LE-SE O ARQUIVO QUE CONTEM A INFORMAÇAO DO ARDUINO(POTENCIOMETROS PARA POSICAO E CLICK DE BOTAO)
            for i in data:
                info = i.split(',')
            print(info)
            x = int(info[1])
            y = int(info[2])
            sel = info[0]
            data.close()
            cria_legenda() #---ATUALIZA A LEGENDA TODAS AS VEZES QUE ESTA FUNÇAO É CHAMADA
                #----------PASSANDO PELO LARANJA-------------------------------
#x = 1 a 59
#y = 7 a 25

            if y == 8 or y == 11 or y == 14 or y == 17 or y == 20 or y == 23:
                while x == 1 or x == 7 or x == 13 or x == 19 or x == 25 or x == 31 or x == 37 or x == 43 or x == 49 or x == 55:
                    verde_lb["image"] = verde
                    vermelho_lb["image"] = vermelho
                    rosa_lb["image"] = rosa
                    amarelo_lb["image"] = amarelo
                    azul_lb["image"] = azul
                    seta2_pisca.place(x = 450, y = 550)
                    seta_lb.place(x = 135, y = 339)
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    print(info)
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])  
                    laranja_lb["image"] = laranja1
                    if x != 1 and x != 7 and x != 13 and x != 19 and x != 25 and x != 31 and x != 37 and x != 43 and x != 49 and x != 55:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        euforico_ama.place(x = 174, y = 328)
                        time.sleep(1)
                        funclaranja()
                        break
                    time.sleep(0.3)            
                    laranja_lb["image"] = laranja2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 1 and x != 7 and x != 13 and x != 19 and x != 25 and x != 31 and x != 37 and x != 43 and x != 49 and x != 55:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        euforico_ama.place(x = 174, y = 328)
                        time.sleep(1)
                        funclaranja()
                        break
                    time.sleep(0.3)            
                    laranja_lb["image"] = laranja3
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 1 and x != 7 and x != 13 and x != 19 and x != 25 and x != 31 and x != 37 and x != 43 and x != 49 and x != 55:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        euforico_ama.place(x = 174, y = 328)
                        time.sleep(1)
                        funclaranja()
                        break
                    time.sleep(0.3)
                    laranja_lb["image"] = laranja2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 1 and x != 7 and x != 13 and x != 19 and x != 25 and x != 31 and x != 37 and x != 43 and x != 49 and x != 55:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    time.sleep(0.3)
                    laranja_lb["image"] = laranja1
                    if sel == "A":
                        euforico_ama.place(x = 174, y = 328)
                        time.sleep(1)
                        funclaranja()
                        break
                if sel == "A":
                    break


        #----------------PASSANDO PELO VERDE-------------------------


                while x == 2 or x == 8 or x == 14 or x == 20 or x == 26 or x == 32 or x == 38 or x == 44 or x == 50 or x == 56:
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    print(info)
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])  
                    data.close()
                    amarelo_lb["image"] = amarelo
                    vermelho_lb["image"] = vermelho
                    rosa_lb["image"] = rosa
                    laranja_lb["image"] = laranja
                    azul_lb["image"] = azul
                    verde_lb["image"] = verde1
                    seta2_pisca.place(x = 450, y = 550)
                    if x != 2 and x != 8 and x != 14 and x != 20 and x != 26 and x != 32 and x != 38 and x != 44 and x != 50 and x != 56:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        feliz_ama.place(x = 354, y = 329)
                        time.sleep(1)
                        funcverde()
                        break
                    seta_lb.place(x = 318, y = 339)
                    time.sleep(0.3)            
                    verde_lb["image"] = verde2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 2 and x != 8 and x != 14 and x != 20 and x != 26 and x != 32 and x != 38 and x != 44 and x != 50 and x != 56:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        feliz_ama.place(x = 354, y = 329)
                        time.sleep(1)
                        funcverde()
                        break
                    time.sleep(0.3)            
                    verde_lb["image"] = verde3
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 2 and x != 8 and x != 14 and x != 20 and x != 26 and x != 32 and x != 38 and x != 44 and x != 50 and x != 56:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        feliz_ama.place(x = 354, y = 329)
                        time.sleep(1)
                        funcverde()
                        break
                    time.sleep(0.3)
                    verde_lb["image"] = verde2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 2 and x != 8 and x != 14 and x != 20 and x != 26 and x != 32 and x != 38 and x != 44 and x != 50 and x != 56:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    time.sleep(0.3)
                    verde_lb["image"] = verde1
                    if sel == "A":
                        feliz_ama.place(x = 354, y = 329)
                        time.sleep(1)
                        funcverde()
                        break
                if sel == "A":
                    break


        #-----------------PASSANDO PELO ROXO-----------------------------


                while x == 3 or x == 9 or x == 15 or x == 21 or x == 27 or x == 33 or x == 39 or x == 45 or x == 51 or x == 57:
                    verde_lb["image"] = verde
                    vermelho_lb["image"] = vermelho
                    amarelo_lb["image"] = amarelo
                    laranja_lb["image"] = laranja
                    azul_lb["image"] = azul
                    seta2_pisca.place(x = 450, y = 550)
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    print(info)
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])  
                    data.close()
                    rosa_lb["image"] = rosa1
                    if x != 3 and x != 9 and x != 15 and x != 21 and x != 27 and x != 33 and x != 39 and x != 45 and x != 51 and x != 57:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        entediado_ama.place(x = 528, y = 328)
                        time.sleep(1)
                        funcrosa()
                        break
                    seta_lb.place(x = 497, y = 339)
                    time.sleep(0.3)            
                    rosa_lb["image"] = rosa2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 3 and x != 9 and x != 15 and x != 21 and x != 27 and x != 33 and x != 39 and x != 45 and x != 51 and x != 57:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        entediado_ama.place(x = 528, y = 328)
                        time.sleep(1)
                        funcrosa()
                        break
                    time.sleep(0.3)            
                    rosa_lb["image"] = rosa3
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 3 and x != 9 and x != 15 and x != 21 and x != 27 and x != 33 and x != 39 and x != 45 and x != 51 and x != 57:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        entediado_ama.place(x = 528, y = 328)
                        time.sleep(1)
                        funcrosa()
                        break
                    time.sleep(0.3)
                    rosa_lb["image"] = rosa2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 3 and x != 9 and x != 15 and x != 21 and x != 27 and x != 33 and x != 39 and x != 45 and x != 51 and x != 57:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    time.sleep(0.3)
                    rosa_lb["image"] = rosa1
                    if sel == "A":
                        entediado_ama.place(x = 528, y = 328)
                        time.sleep(1)
                        funcrosa()
                        break
                if sel == "A":
                    break


        #-----------------PASSANDO PELO AMARELO---------------------


                while x == 4 or x == 10 or x == 16 or x == 22 or x == 28 or x == 34 or x == 40 or x == 46 or x == 52 or x == 58:
                    verde_lb["image"] = verde
                    vermelho_lb["image"] = vermelho
                    rosa_lb["image"] = rosa
                    laranja_lb["image"] = laranja
                    azul_lb["image"] = azul
                    seta2_pisca.place(x = 450, y = 550)
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    print(info)
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()  
                    amarelo_lb["image"] = amarelo1
                    if x != 4 and x != 10 and x != 16 and x != 22 and x != 28 and x != 34 and x != 40 and x != 46 and x != 52 and x != 58:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        ansioso_ama.place(x = 700, y = 328)
                        time.sleep(1)
                        funcamarelo()
                        break
                    seta_lb.place(x = 672, y = 339)
                    time.sleep(0.3)            
                    amarelo_lb["image"] = amarelo2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 4 and x != 10 and x != 16 and x != 22 and x != 28 and x != 34 and x != 40 and x != 46 and x != 52 and x != 58:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        ansioso_ama.place(x = 700, y = 328)
                        time.sleep(1)
                        funcamarelo()
                        break
                    time.sleep(0.3)            
                    amarelo_lb["image"] = amarelo3
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 4 and x != 10 and x != 16 and x != 22 and x != 28 and x != 34 and x != 40 and x != 46 and x != 52 and x != 58:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        ansioso_ama.place(x = 700, y = 328)
                        time.sleep(1)
                        funcamarelo()
                        break
                    time.sleep(0.3)
                    amarelo_lb["image"] = amarelo2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 4 and x != 10 and x != 16 and x != 22 and x != 28 and x != 34 and x != 40 and x != 46 and x != 52 and x != 58:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    time.sleep(0.3)
                    amarelo_lb["image"] = amarelo1
                    if sel == "A":
                        ansioso_ama.place(x = 700, y = 328)
                        time.sleep(1)
                        funcamarelo()
                        break
                if sel == "A":
                    break


        #-----------------PASSANDO PELO VERMELHO-------------------------------


                while x == 5 or x == 11 or x == 17 or x == 23 or x == 29 or x == 35 or x == 41 or x == 47 or x == 53 or x == 59:
                    verde_lb["image"] = verde
                    amarelo_lb["image"] = amarelo
                    rosa_lb["image"] = rosa
                    laranja_lb["image"] = laranja
                    azul_lb["image"] = azul
                    seta2_pisca.place(x = 450, y = 550)
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    print(info)
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])  
                    data.close()
                    vermelho_lb["image"] = vermelho1
                    seta_lb.place(x = 850, y = 339)
                    if x != 5 and x != 11 and x != 17 and x != 23 and x != 29 and x != 35 and x != 41 and x != 47 and x != 53 and x != 59:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        raivoso_ama.place(x = 882, y = 328)
                        time.sleep(1)
                        funcvermelho()
                        break
                    time.sleep(0.3)            
                    vermelho_lb["image"] = vermelho2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 5 and x != 11 and x != 17 and x != 23 and x != 29 and x != 35 and x != 41 and x != 47 and x != 53 and x != 59:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        raivoso_ama.place(x = 882, y = 328)
                        time.sleep(1)
                        funcvermelho()
                        break
                    time.sleep(0.3)
                    vermelho_lb["image"] = vermelho3
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 5 and x != 11 and x != 17 and x != 23 and x != 29 and x != 35 and x != 41 and x != 47 and x != 53 and x != 59:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        raivoso_ama.place(x = 882, y = 328)
                        time.sleep(1)
                        funcvermelho()
                        break
                    time.sleep(0.3)
                    vermelho_lb["image"] = vermelho2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 5 and x != 11 and x != 17 and x != 23 and x != 29 and x != 35 and x != 41 and x != 47 and x != 53 and x != 59:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    time.sleep(0.3)
                    vermelho_lb["image"] = vermelho1
                    if sel == "A":
                        raivoso_ama.place(x = 882, y = 328)
                        time.sleep(1)
                        funcvermelho()
                        break
                if sel == "A":
                    break


        #--------------PASSANDO PELO AZUL-------------------------------

                while x == 6 or x == 12 or x == 18 or x == 24 or x == 30 or x == 36 or x == 42 or x == 48 or x == 54 or x == 60:
                    verde_lb["image"] = verde
                    vermelho_lb["image"] = vermelho
                    rosa_lb["image"] = rosa
                    laranja_lb["image"] = laranja
                    amarelo_lb["image"] = amarelo
                    seta2_pisca.place(x = 450, y = 550)
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    azul_lb["image"] = azul1
                    seta_lb.place(x = 1025, y = 339)
                    if x != 6 and x != 12 and x != 18 and x != 24 and x != 30 and x != 36 and x != 42 and x != 48 and x != 54 and x != 60:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        triste_ama.place(x = 1059, y = 328)
                        time.sleep(1)
                        funcazul()
                        break
                    time.sleep(0.3)            
                    azul_lb["image"] = azul2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 6 and x != 12 and x != 18 and x != 24 and x != 30 and x != 36 and x != 42 and x != 48 and x != 54 and x != 60:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        triste_ama.place(x = 1059, y = 328)
                        time.sleep(1)
                        funcazul()
                        break
                    time.sleep(0.3)            
                    azul_lb["image"] = azul3
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 6 and x != 12 and x != 18 and x != 24 and x != 30 and x != 36 and x != 42 and x != 48 and x != 54 and x != 60:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    if sel == "A":
                        triste_ama.place(x = 1059, y = 328)
                        time.sleep(1)
                        funcazul()
                        break
                    time.sleep(0.3)
                    azul_lb["image"] = azul2
                    data = open('arquivos/data.txt', 'r')
                    for i in data:
                        info = i.split(',')
                    sel = info[0]
                    x = int(info[1])
                    y = int(info[2])
                    data.close()
                    if x != 6 and x != 12 and x != 18 and x != 24 and x != 30 and x != 36 and x != 42 and x != 48 and x != 54 and x != 60:
                        break
                    if y != 8 and y != 11 and y != 14 and y != 17 and y != 20 and y != 23:
                        break
                    time.sleep(0.3)
                    azul_lb["image"] = azul1
                    if sel == "A":
                        triste_ama.place(x = 1059, y = 328)
                        time.sleep(1)
                        funcazul()
                        break
                if sel == "A":
                    break


    #---------------CONFIGURAÇÃO BOTAO DALTONICO----------

            while y == 7 or y == 10 or y == 13 or y == 16 or y == 19 or y == 22 or y == 25:
                verde_lb["image"] = verde
                vermelho_lb["image"] = vermelho
                rosa_lb["image"] = rosa
                laranja_lb["image"] = laranja
                azul_lb["image"] = azul
                seta2_pisca.place(x = 450, y = 550)
                data = open('arquivos/data.txt', 'r')
                seta_lb.place(x = 1052, y = 53)
                for i in data:
                    info = i.split(',')
                print(info)
                sel = info[0]
                x = int(info[1])
                y = int(info[2])
                if sel == 'A':
                    if dalt_ativado == 0:
                        funcdaltonico()
                    elif dalt_ativado == 1:
                        funcdaltonico1()
            if sel == "A":
                break

    #---------------CONFIGURAÇÃO BOTAO REGRAS----------

            while y == 9 or y == 12 or y == 15 or y == 18 or y == 21 or y == 24 or y == 27:
                verde_lb["image"] = verde
                vermelho_lb["image"] = vermelho
                rosa_lb["image"] = rosa
                laranja_lb["image"] = laranja
                azul_lb["image"] = azul
                seta2_pisca.place(x = 4500, y = 550)
                data = open('arquivos/data.txt', 'r')
                seta_lb.place(x = 3540, y = 600)
                for i in data:
                    info = i.split(',')
                print(info)
                sel = info[0]
                x = int(info[1])
                y = int(info[2])
                if sel == 'A':
                    abre_instru()
                    time.sleep(1)
            if sel == "A":
                break


    background(selecionador)


    #----------------------FUNÇÃO ABRIR PAGINA DO MOSAICO-------------------------------


    def abre_janela():
        root = Toplevel()
        root.title("HUMORSAICO")
        root.geometry("+0+0")
        
        #-------- VARIAVEIS QUE SERÃO USADAS----------
        
        global completo
        global completo_arquivo
        global linhas
        global cor_braco
        global cor_amarelo
        global cor_vermelho
        global cor_azul
        global cor_laranja
        global cor_verde
        global n_verde
        global n_vermelho
        global n_roxo
        global n_amarelo
        global n_laranja
        global n_azul
        global rfid
        global biblioteca
        global score

        root["bg"] = cor_preto

        with open("arquivos/banco_dados_global.json") as aaa:
            biblioteca = json.load(aaa)
        score = scoreboard(rfid, biblioteca)

        coraCheio_lb = [1, 2, 3]
        j = 0
        n = 1
        coluna = 0
        balde1 = PhotoImage(file = "imagens/baldes1.png")
        balde2 = PhotoImage(file = "imagens/baldes2.png")
        balde3 = PhotoImage(file = "imagens/baldes3.png")
        cora_vazio = PhotoImage(file = "imagens/balde-vazio.png")
        legen = PhotoImage(file = "imagens/legenda.png")
        top = PhotoImage(file = "imagens/top.png")

        
        for i in range (len(completo)):#--------AQUI É IMPRESSO O NOSSO MOSAICO, LINHA A LINHA <------ ESTE PRIMEIRO FOR AUMENTA +1 NA VARIAVEL "i" PARA CADA LINHA GERADA
            for j in range(len(completo[i])):
                if completo[i][j] == "0":#--------------------PARA CADA IF, ELIF É GERADA UMA LABEL DE UMA CERTA COR COM TAMANHO JA DEFINIDO E LOCALIZAÇÃO LINHA "i" E COLUNA "coluna" ONDE
                    completo[i][j] = Label(root, width = 2, height = 1, bg = cor_preto)#------------COLUNA É UMA VARIAVEL QUE ESTA SENDO SOMADA A CADA REPETIÇAO DO WHILE ELA ZERA QUANDO O /N
                    completo[i][j].grid(row = i, column = j)#-------------------------É ENCONTRADO E ASSIM QUEBRA O LOOP DO WHILE E PARTINDO PARA A GERAÇAO DA SEGUNDA LINHA DO MOSAICO
                elif completo[i][j] == "1":
                    completo[i][j] = Label(root, width = 2, height = 1, bg = cor_cinza)
                    completo[i][j].grid(row = i, column = j)
                elif completo[i][j] == "2":
                    completo[i][j] = Label(root, width = 2, height = 1, bg = cor_azul)
                    completo[i][j].grid(row = i, column = j)
                elif completo[i][j] == "3":
                    completo[i][j] = Label(root, width = 2, height = 1, bg = cor_vermelho)#----------CADA ELIF REPRESENTA UMA LABEL DE DIFERENTES CORES, PARA CADA NUMERO ENCONTRADO NO ARQUIVO UMA
                    completo[i][j].grid(row = i, column = j)#-----------------------LABEL DIFERENTE SERA CRIADA, ASSIM FORMANDO O MOSAICO COM DIFERENTES CORES
                elif completo[i][j] == "4":
                    completo[i][j] = Label(root, width = 2, height = 1, bg = cor_amarelo)
                    completo[i][j].grid(row = i, column = j)
                elif completo[i][j] == "5":
                    completo[i][j] = Label(root, width = 2, height = 1, bg = cor_verde)
                    completo[i][j].grid(row = i, column = j)
                elif completo[i][j] == "6":
                    completo[i][j] = Label(root, width = 2, height = 1, bg = cor_rosa)
                    completo[i][j].grid(row = i, column = j)
                elif completo[i][j] == "7":
                    completo[i][j] = Label(root, width = 2, height = 1, bg = cor_braco)
                    completo[i][j].grid(row = i, column = j)
                elif completo[i][j] == "8":
                    completo[i][j] = Label(root, width = 2, height = 1, bg = cor_laranja)
                    completo[i][j].grid(row = i, column = j)


        abre_completo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for i in range(15):
            abre_completo[i] = Label(root, width = 2, height = 1, bg = cor_preto)
            abre_completo[i].grid(row = 50 + i, column = 90)


#------------------IMAGENS DE FUNDO-----------------------------------------------------------

        highscore = Label(root, image = top, bg = cor_preto)
        highscore.place(x=0,y=0)

        legenda = Label(root, image = legen, bg = cor_preto)
        legenda.place(x=0, y=500)
        
        coraCheio_lb[0] = Label(root, image = balde1, bg = cor_preto)
        coraCheio_lb[0].place(x = 1280, y = 40)

        coraCheio_lb[1] = Label(root, image = balde2, bg = cor_preto)
        coraCheio_lb[1].place(x = 1210, y = 40)

        coraCheio_lb[2] = Label(root, image = balde3, bg = cor_preto)
        coraCheio_lb[2].place(x = 1150, y = 40)

#------------------------------PARTE DO MASCOTE---------------------------------------------------------------------

        interacoes_img = PhotoImage(file = "imagens/btn_interacoes.png")
        interacoes_lb = Label(root, image = interacoes_img, bg = cor_preto)
        interacoes_lb.place(x = 920, y = 545)

        amor_amarelo = PhotoImage(file = "imagens/amor_amarelo.png") 
        comer_amarelo = PhotoImage(file = "imagens/comer_amarelo.png") 
        passinho_amarelo = PhotoImage(file = "imagens/passinho_amarelo.png") 

        amor_amarelo_lb = Label(root, image = amor_amarelo, bg = cor_preto)
        comer_amarelo_lb = Label(root, image = comer_amarelo, bg = cor_preto)
        passinho_amarelo_lb = Label(root, image = passinho_amarelo, bg = cor_preto)

        cursor_img = PhotoImage(file = "imagens/setinha2.png")
        cursor_lb = Label(root, image = cursor_img, bg = cor_preto)


#-----------------------------MASCOTE CRESCENDO-------------------------------------------------

        ovo_img = PhotoImage(file = "imagens/cama_crescendo/ovo.png")
        a1_img = PhotoImage(file = "imagens/cama_crescendo/a(1).png")
        a2_img = PhotoImage(file = "imagens/cama_crescendo/a(2).png")
        a3_img = PhotoImage(file = "imagens/cama_crescendo/a(3).png")
        a4_img = PhotoImage(file = "imagens/cama_crescendo/a(4).png")
        a5_img = PhotoImage(file = "imagens/cama_crescendo/a(5).png")
        a6_img = PhotoImage(file = "imagens/cama_crescendo/a(6).png")
        b1_img = PhotoImage(file = "imagens/cama_crescendo/b(1).png")
        b2_img = PhotoImage(file = "imagens/cama_crescendo/b(2).png")
        b3_img = PhotoImage(file = "imagens/cama_crescendo/b(3).png")
        b4_img = PhotoImage(file = "imagens/cama_crescendo/b(4).png")
        b5_img = PhotoImage(file = "imagens/cama_crescendo/b(5).png")
        b6_img = PhotoImage(file = "imagens/cama_crescendo/b(6).png")
        c1_img = PhotoImage(file = "imagens/cama_crescendo/c(1).png")
        c2_img = PhotoImage(file = "imagens/cama_crescendo/c(2).png")
        c3_img = PhotoImage(file = "imagens/cama_crescendo/c(3).png")
        c4_img = PhotoImage(file = "imagens/cama_crescendo/c(4).png")
        c5_img = PhotoImage(file = "imagens/cama_crescendo/c(5).png")
        c6_img = PhotoImage(file = "imagens/cama_crescendo/c(6).png")

        camaleao = Label(root, image = ovo_img, bg = cor_preto)
        
        camaleao.place(x = 1110, y = 490)



#---------------------------INTERACAO PASSINHO--------------------------------------------------

        camale = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
        camale[0] = PhotoImage(file = "imagens/passinho/1.png")
        camale[1] = PhotoImage(file = "imagens/passinho/2.png")
        camale[2] = PhotoImage(file = "imagens/passinho/3.png")
        camale[3] = PhotoImage(file = "imagens/passinho/4.png")
        camale[4] = PhotoImage(file = "imagens/passinho/5.png")
        camale[5] = PhotoImage(file = "imagens/passinho/6.png")
        camale[6] = PhotoImage(file = "imagens/passinho/7.png")
        camale[7] = PhotoImage(file = "imagens/passinho/8.png")
        camale[8] = PhotoImage(file = "imagens/passinho/9.png")
        camale[9] = PhotoImage(file = "imagens/passinho/10.png")
        camale[10] = PhotoImage(file = "imagens/passinho/11.png")
        camale[11] = PhotoImage(file = "imagens/passinho/12.png")
        camale[12] = PhotoImage(file = "imagens/passinho/13.png")
        camale[13] = PhotoImage(file = "imagens/passinho/14.png")
        camale[14] = PhotoImage(file = "imagens/passinho/15.png")
        camale[15] = PhotoImage(file = "imagens/passinho/16.png")
        camale[16] = PhotoImage(file = "imagens/passinho/17.png")
        camale[17] = PhotoImage(file = "imagens/passinho/18.png")
        camale[18] = PhotoImage(file = "imagens/passinho/19.png")
        camale[19] = PhotoImage(file = "imagens/passinho/20.png")
        camale[20] = PhotoImage(file = "imagens/passinho/21.png")
        camale[21] = PhotoImage(file = "imagens/passinho/22.png")
        camale[22] = PhotoImage(file = "imagens/passinho/23.png")
        camale[23] = PhotoImage(file = "imagens/passinho/24.png")
        camale[24] = PhotoImage(file = "imagens/passinho/25.png")
        camale[25] = PhotoImage(file = "imagens/passinho/26.png")
        camale[26] = PhotoImage(file = "imagens/passinho/27.png")
        camale[27] = PhotoImage(file = "imagens/passinho/28.png")
        camale[28] = PhotoImage(file = "imagens/passinho/29.png")
        camale[29] = PhotoImage(file = "imagens/passinho/30.png")
        camale[30] = PhotoImage(file = "imagens/passinho/31.png")
        camale[31] = PhotoImage(file = "imagens/passinho/32.png")
        camale[32] = PhotoImage(file = "imagens/passinho/33.png")
        camale[33] = PhotoImage(file = "imagens/passinho/34.png")
        passin = Label(root, image = camale[0], bg = cor_preto)



        def passinho():
            camaleao.place(x = 1110, y = 4900)
            passin.place(x = 1150, y = 450)
            for j in range(2):
                for i in range(34):
                    passin["image"] = camale[i]
                    if i < 29:
                        time.sleep(0.1)
                    else:
                        time.sleep(0.2)
            passin.place(x = 11500, y = 450)
            camaleao.place(x = 1110, y = 490)



#--------------------CAMALEAO COMENDO-----------------------------------------------


        cama_come = [0,1,2,3,4,5,6,7,8,9,10]
        cama_come[0] = PhotoImage(file = "imagens/cama_come/1.png")
        cama_come[1] = PhotoImage(file = "imagens/cama_come/2.png")
        cama_come[2] = PhotoImage(file = "imagens/cama_come/3.png")
        cama_come[3] = PhotoImage(file = "imagens/cama_come/4.png")
        cama_come[4] = PhotoImage(file = "imagens/cama_come/5.png")
        cama_come[5] = PhotoImage(file = "imagens/cama_come/6.png")
        cama_come[6] = PhotoImage(file = "imagens/cama_come/7.png")
        cama_come[7] = PhotoImage(file = "imagens/cama_come/8.png")
        cama_come[8] = PhotoImage(file = "imagens/cama_come/9.png")
        cama_come[9] = PhotoImage(file = "imagens/cama_come/10.png")
        cama_come[10] = PhotoImage(file = "imagens/cama_come/11.png")

        camal_come = Label(root, image = cama_come[0], bg = cor_preto)

        def comer_grande():
            camaleao.place(x = 1110, y = 4900)
            camal_come.place(x = 1150, y = 485)
            for j in range(3):
                for i in range(11):
                    camal_come["image"] = cama_come[i]
                    time.sleep(0.2)
            camal_come.place(x = 1110, y = 49000)
            camaleao.place(x = 1110, y = 490)


        cama_comeM = [0,1,2,3,4,5,6,7]
        cama_comeM[0] = PhotoImage(file = "imagens/cama_comeM/1.png")
        cama_comeM[1] = PhotoImage(file = "imagens/cama_comeM/2.png")
        cama_comeM[2] = PhotoImage(file = "imagens/cama_comeM/3.png")
        cama_comeM[3] = PhotoImage(file = "imagens/cama_comeM/4.png")
        cama_comeM[4] = PhotoImage(file = "imagens/cama_comeM/5.png")
        cama_comeM[5] = PhotoImage(file = "imagens/cama_comeM/6.png")
        cama_comeM[6] = PhotoImage(file = "imagens/cama_comeM/7.png")
        cama_comeM[7] = PhotoImage(file = "imagens/cama_comeM/8.png")

        camal_comeM = Label(root, image = cama_comeM[0], bg = cor_preto)

        def comer_medio():
            camaleao.place(x = 1110, y = 4900)
            camal_comeM.place(x = 1150, y = 485)
            for j in range(3):
                for i in range(11):
                    camal_comeM["image"] = cama_come[i]
                    time.sleep(0.2)
            camal_comeM.place(x = 1110, y = 49000)
            camaleao.place(x = 1110, y = 490)




#-----------CAMALEAO AMOR--------------------------------------


        cama_amor = [0,1,2,3,4,5,6,7,8]
        cama_amor[0] = PhotoImage(file = "imagens/cama_amor/1.png")
        cama_amor[1] = PhotoImage(file = "imagens/cama_amor/2.png")
        cama_amor[2] = PhotoImage(file = "imagens/cama_amor/3.png")
        cama_amor[3] = PhotoImage(file = "imagens/cama_amor/4.png")
        cama_amor[4] = PhotoImage(file = "imagens/cama_amor/5.png")
        cama_amor[5] = PhotoImage(file = "imagens/cama_amor/6.png")
        cama_amor[6] = PhotoImage(file = "imagens/cama_amor/7.png")
        cama_amor[7] = PhotoImage(file = "imagens/cama_amor/8.png")
        cama_amor[8] = PhotoImage(file = "imagens/cama_amor/9.png")

        camal_amor = Label(root, image = cama_amor[0], bg = cor_preto)

        def amor_grande():
            camaleao.place(x = 1110, y = 4900)
            camal_amor.place(x = 1150, y = 485)
            for j in range(3):
                for i in range(9):
                    camal_amor["image"] = cama_amor[i]
                    time.sleep(0.2)
            camal_amor.place(x = 1110, y = 49000)
            camaleao.place(x = 1110, y = 490)


        cama_amorM = [0,1,2,3,4,5,6,7,8]
        cama_amorM[0] = PhotoImage(file = "imagens/cama_amorM/1.png")
        cama_amorM[1] = PhotoImage(file = "imagens/cama_amorM/2.png")
        cama_amorM[2] = PhotoImage(file = "imagens/cama_amorM/3.png")
        cama_amorM[3] = PhotoImage(file = "imagens/cama_amorM/4.png")
        cama_amorM[4] = PhotoImage(file = "imagens/cama_amorM/5.png")
        cama_amorM[5] = PhotoImage(file = "imagens/cama_amorM/6.png")
        cama_amorM[6] = PhotoImage(file = "imagens/cama_amorM/7.png")
        cama_amorM[7] = PhotoImage(file = "imagens/cama_amorM/8.png")
        cama_amorM[8] = PhotoImage(file = "imagens/cama_amorM/9.png")

        camal_amorM = Label(root, image = cama_amor[0], bg = cor_preto)

        def amor_medio():
            camaleao.place(x = 1110, y = 4900)
            camal_amorM.place(x = 1150, y = 485)
            for j in range(3):
                for i in range(9):
                    camal_amorM["image"] = cama_amorM[i]
                    time.sleep(0.2)
            camal_amorM.place(x = 1110, y = 49000)
            camaleao.place(x = 1110, y = 490)


        cama_amorP = [0,1,2,3,4,5,6,7,8]
        cama_amorP[0] = PhotoImage(file = "imagens/cama_amorP/1.png")
        cama_amorP[1] = PhotoImage(file = "imagens/cama_amorP/2.png")
        cama_amorP[2] = PhotoImage(file = "imagens/cama_amorP/3.png")
        cama_amorP[3] = PhotoImage(file = "imagens/cama_amorP/4.png")
        cama_amorP[4] = PhotoImage(file = "imagens/cama_amorP/5.png")
        cama_amorP[5] = PhotoImage(file = "imagens/cama_amorP/6.png")
        cama_amorP[6] = PhotoImage(file = "imagens/cama_amorP/7.png")
        cama_amorP[7] = PhotoImage(file = "imagens/cama_amorP/8.png")
        cama_amorP[8] = PhotoImage(file = "imagens/cama_amorP/9.png")

        camal_amorP = Label(root, image = cama_amorP[0], bg = cor_preto)

        def amor_peque():
            camaleao.place(x = 1110, y = 4900)
            camal_amorP.place(x = 1150, y = 485)
            for j in range(3):
                for i in range(9):
                    camal_amorP["image"] = cama_amorP[i]
                    time.sleep(0.2)
            camal_amorP.place(x = 1110, y = 49000)
            camaleao.place(x = 1110, y = 490)




        def soma_score():#------SOMA +1 NO SCOREBOARD INSTANTANEO E SALVA NO ARQUIVO
            global rfid
            global biblioteca
            global score
            print (rfid, score)
            print(biblioteca[rfid]["score"])
            biblioteca[rfid]["score"] = biblioteca[rfid]["score"] + 1
            print(biblioteca)

            with open ('arquivos/banco_dados_global.json', 'w') as total:
                json.dump(biblioteca, total)
            numero_score["text"] = scoreboard(rfid, biblioteca)

        def topboard():
            global biblioteca
            global rfid
            rank = 1
            for i in biblioteca:
                if biblioteca[rfid]["score"] < biblioteca[i]["score"]:
                    rank += 1
            biblioteca[rfid]["top"] = rank
            with open ('arquivos/banco_dados_global.json', 'w') as total:
                json.dump(biblioteca, total)

            return rank



        def frases():
            lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            lista[0] = "Tumbar: A paciencia de Jo foi inspirada em Domingos"
            lista[1] = "Tumbar: Ja incensaram o CESAR de pipoca hoje?"
            lista[2] = "Tumbar: Meu planeta é CESAR Skol"
            lista[3] = "Tumbar: Noelle perfeita!"
            lista[4] = "Tumbar: Dave Corno!"
            lista[5] = "Tumbar: Dudu Corno!"
            lista[6] = "Tumbar: Tenorio Corno!"
            lista[7] = "Tumbar: Cala a boca Camila!"
            lista[8] = "Tumbar: Para de comer Duane!"
            lista[9] = "Tumbar: Ketinho!"
            lista[10] = "Tumbar: Di boa po"
            lista[11] = "Tumbar: Ei Dave, tu comprou essa bolsa aonde?"
            lista[12] = "Tumbar: Gerson"
            lista[13] = "Tumbar: Hey @Everyone"
            lista[14] = "Tumbar: Dai a Cesar o que de Cesar"
            lista[15] = "Tumbar: Rei do Arduino"

            frase_mascote = random.choice(lista)
            return(frase_mascote)


        def obrigado():
            pagina_obg = Toplevel()
            pagina_obg.title("HUMORSAICO")
            pagina_obg.geometry("+0+0")

            camaObg_img = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
            camaObg_img[0] = PhotoImage(file = "imagens/cama_obg/1.png")
            camaObg_img[1] = PhotoImage(file = "imagens/cama_obg/2.png")
            camaObg_img[2] = PhotoImage(file = "imagens/cama_obg/3.png")
            camaObg_img[3] = PhotoImage(file = "imagens/cama_obg/4.png")
            camaObg_img[4] = PhotoImage(file = "imagens/cama_obg/5.png")
            camaObg_img[5] = PhotoImage(file = "imagens/cama_obg/6.png")
            camaObg_img[6] = PhotoImage(file = "imagens/cama_obg/7.png")
            camaObg_img[7] = PhotoImage(file = "imagens/cama_obg/8.png")
            camaObg_img[8] = PhotoImage(file = "imagens/cama_obg/9.png")
            camaObg_img[9] = PhotoImage(file = "imagens/cama_obg/10.png")
            camaObg_img[10] = PhotoImage(file = "imagens/cama_obg/11.png")
            camaObg_img[11] = PhotoImage(file = "imagens/cama_obg/12.png")
            camaObg_img[12] = PhotoImage(file = "imagens/cama_obg/13.png")
            camaObg_img[13] = PhotoImage(file = "imagens/cama_obg/14.png")
            camaObg_img[14] = PhotoImage(file = "imagens/cama_obg/15.png")
            camaObg_img[15] = PhotoImage(file = "imagens/cama_obg/16.png")
            camaObg_img[16] = PhotoImage(file = "imagens/cama_obg/17.png")


            imagem_fundo_obrigado = PhotoImage(file = "imagens/obrigado.png")
            imagem_fundo_obg_lb = Label(pagina_obg, image = imagem_fundo_obrigado, bg = cor_preto)
            imagem_fundo_obg_lb.pack()

            camaObg_lb = Label(pagina_obg, image = camaObg_img[0], bg = cor_preto)
            camaObg_lb.place(x = 600,y = 450)


            for j in range(3):
                for i in range(17):
                    camaObg_lb["image"] = camaObg_img[i]
                    time.sleep(0.3)

            pagina_obg.destroy()



#--------------------NUMERO DE REPORTS----------------------------------------------------------------

        total_reports = n_laranja + n_verde + n_roxo + n_amarelo + n_vermelho + n_azul

        faltando = Label(root, text = "EXP: "+str(total_reports), fg = cor_braco, bg = cor_preto, font = "Minecraft 20")
        faltando.place(x = 920, y = 490)


    #------------------UTILIZANDO NUMERO DE REPORTS PARA FAZER A LEGENDA-------------------------------

        numero_verde = Label(root, width = 2, height = 1, bg = "black", fg = "white", text = str(n_verde), font = "Minecraft 20")
        numero_verde.place(x=7, y = 605)

        numero_amarelo = Label(root, width = 2, height = 1, bg = "black", fg = "white", text = str(n_amarelo), font = "Minecraft 20")
        numero_amarelo.place(x = 230, y = 560)

        numero_vermelho = Label(root, width = 2, height = 1, bg = "black", fg = "white", text = str(n_vermelho), font = "Minecraft 20")
        numero_vermelho.place(x = 230, y = 605)

        numero_azul = Label(root, width = 2, height = 1, bg = "black", fg = "white", text = str(n_azul), font = "Minecraft 20")
        numero_azul.place(x = 230, y = 654)

        numero_roxo = Label(root, width = 2, height = 1, bg = "black", fg = "white", text = str(n_roxo), font = "Minecraft 20")
        numero_roxo.place(x = 7, y = 654)

        numero_laranja = Label(root, width = 2, height = 1,bg = "black", fg = "white", text = str(n_laranja), font = "Minecraft 20")
        numero_laranja.place(x = 7, y = 560)

        numero_score = Label(root, bg = "black", fg = "white", text = str(score), font = "Minecraft 25")
        numero_score.place(x = 735, y = 61)

        numero_top = Label(root, width = 8, bg = cor_preto, fg = cor_braco, text = str(topboard()), font = "Minecraft 25")
        numero_top.place(x = 510, y = 61)


        frase_masco = [0, 1, 2]

        frase_masco[0] = Label(root, bg = cor_preto, fg = cor_braco, text = "", font = "Minecraft 20")
        frase_masco[0].place(x = 420, y = 650)

        frase_masco[1] = Label(root, bg = cor_preto, fg = cor_braco, text = "", font = "Minecraft 20")
        frase_masco[1].place(x = 420, y = 680)

        frase_masco[2] = Label(root, bg = cor_preto, fg = cor_braco, text = "", font = "Minecraft 20")
        frase_masco[2].place(x = 420, y = 710)


        frase_ola = Label(root, bg = cor_preto, fg = cor_braco, text = "Ola!\n Meu nome é TUMBAR!", font = "Minecraft 20")
        frase_ola.place(x = 1190, y = 440)

    #----------FIM DA LEGENDA--------------------------------------------------------------------------------------



        def set_cor(x, y):#-----------SETANDO COR NA POSIÇÃO PEDIDA
            l_aux = 0
            global cor_aux
            global cor
            global completo
            global completo_arquivo
            global pintou
            global cont
            for i in range (len(completo_arquivo)):#-----------A POSIÇÃO É ENCONTRADA UTILIZANDO O ARQUIVO EM FORMA DE STRING
                if l_aux == y:
                    break
                if completo_arquivo[i] == "\n":#-------PRIMEIRO É ENCONTRADO A LINHA PEDIDA, DEPOIS É SOMADO O NUMERO DA COLUNA A SER ADICIONADO
                    l_aux += 1
            if cor_aux == cor_cinza:#---------SO SERA PINTADO OS QUADRADOS DE COR LARANJA
                if cor == "V" :  
                    completo_arquivo[i+x] = "3"#----ARQUIVO DE TEXTO É ALTERADO PARA A COR PEDIDA
                    completo[y][x]["bg"] = cor_vermelho#---------COR DE FUNDO DA LABEL É MUDADO, PRA SER MOSTRADO INSTANTANEAMENTE
                    cor_aux = cor_vermelho#--------------COR AUXILIAR VIRA A COR QUE FOI PEDIDA, PARA QUANDO O QUADRADO PRETO SAIR DE POSIÇAO NAO PERDER A COR PINTADA
                    time.sleep(0.3)
                    coraCheio_lb[cont]["image"] = cora_vazio
                    frase_masco[cont]["text"] = frases()
                    cont += 1
                    soma_score()
                    if cont == 3:
                        funcdaltonico1()
                        info_arquivo()
                        pintou = 0
                        background(obrigado)
                        background(selecionador_1)
                        interface.destroy()
                        root.destroy()
                        time.sleep(1)
                        cont = 0
                elif cor == "A":
                    completo_arquivo[i+x] = "2"#------------ISSO VALE PARA TODAS AS CORES....
                    completo[y][x]["bg"] = cor_azul
                    cor_aux = cor_azul
                    time.sleep(0.3)
                    coraCheio_lb[cont]["image"] = cora_vazio
                    frase_masco[cont]["text"] = frases()
                    cont += 1
                    soma_score()
                    if cont == 3:
                        funcdaltonico1()
                        info_arquivo()
                        pintou = 0
                        background(obrigado)
                        background(selecionador_1)
                        interface.destroy()
                        root.destroy()
                        time.sleep(1)
                        cont = 0
                elif cor == "Ve":
                    completo_arquivo[i+x] = "5"
                    completo[y][x]["bg"] = cor_verde
                    cor_aux = cor_verde
                    time.sleep(0.3)
                    coraCheio_lb[cont]["image"] = cora_vazio
                    frase_masco[cont]["text"] = frases()
                    cont += 1
                    soma_score()
                    if cont == 3:#-----APOS PINTAR 3 CORES.....
                        funcdaltonico1()
                        info_arquivo()#---MOSAICO VIRA STRING
                        pintou = 0#----PINTOU = 0 PARA PARAR A FUNÇÃO WALK
                        background(obrigado)
                        background(selecionador_1)#----FUNÇÃO DE SELECIONAR INTERFACE ATIVA NOVAMENTE
                        interface.destroy()
                        root.destroy()
                        time.sleep(1)
                        cont = 0
                elif cor == "Am":
                    completo_arquivo[i+x] = "4"
                    completo[y][x]["bg"] = cor_amarelo
                    cor_aux = cor_amarelo
                    time.sleep(0.3)
                    coraCheio_lb[cont]["image"] = cora_vazio
                    frase_masco[cont]["text"] = frases()
                    cont += 1
                    soma_score()
                    if cont == 3:
                        funcdaltonico1()
                        info_arquivo()
                        pintou = 0
                        background(obrigado)
                        background(selecionador_1)
                        interface.destroy()
                        root.destroy()
                        time.sleep(1)
                        cont = 0
                elif cor == "R":
                    completo_arquivo[i+x] = "6"
                    completo[y][x]["bg"] = cor_rosa
                    cor_aux = cor_rosa
                    time.sleep(0.3)
                    coraCheio_lb[cont]["image"] = cora_vazio
                    frase_masco[cont]["text"] = frases()
                    cont += 1
                    soma_score()
                    if cont == 3:
                        funcdaltonico1()
                        info_arquivo()
                        pintou = 0
                        background(obrigado)
                        background(selecionador_1)
                        interface.destroy()
                        root.destroy()
                        time.sleep(1)
                        cont = 0
                elif cor == "La":
                    completo_arquivo[i+x] = "8"
                    completo[y][x]["bg"] = cor_laranja
                    cor_aux = cor_laranja
                    time.sleep(0.3)
                    coraCheio_lb[cont]["image"] = cora_vazio
                    frase_masco[cont]["text"] = frases()
                    cont += 1
                    soma_score()
                    if cont == 3:
                        funcdaltonico1()
                        info_arquivo()
                        pintou = 0
                        background(obrigado)
                        background(selecionador_1)
                        interface.destroy()
                        root.destroy()
                        time.sleep(1)
                        cont = 0
                texto = open('arquivos/logo2.txt', 'w')#------APOS SER MODIFICADA A COR NA POSIÇAO PEDIDA, UM NOVO ARQUIVO É GERADO COM A COR JA SALVA
                texto.writelines(completo_arquivo)
                texto.close()
        


        def walk_bt(xt, yt):
            l_aux = 1
            global cor_aux
            global completo
            global completo_arquivo
            for i in range (len(completo_arquivo)):#-----------SETANDO COR NA POSIÇÃO PEDIDA
                if l_aux == yt:
                    break
                if completo_arquivo[i] == "\n":#-------PRIMEIRO É ENCONTRADO A LINHA PEDIDA, APOS SER ENCONTRADA A LINHA É SOMADO O NUMERO DA COLUNA A SER ADICIONADO
                    l_aux += 1
            if completo[yt][xt]["bg"] != cor_preto:#---------CASO A POSIÇAO DO PONTO PRETO NAO SEJA BRANCO ELE PODE ANDAR NORMALMENTE
                cor_aux = completo[yt][xt]["bg"]
                completo[yt][xt]["bg"] = cor_braco
            else:#------------------------SE O PONTO PRETO FOR PARA A POSIÇAO BRANCA ELE COMEÇA A DEIXAR RASTROS BRANCOS QUE DA A IMPRESSAO QUE NAO ESTA ANDANDO NO BRANCO
                cor_aux = cor_preto#---------ALEM DE NAO PINTAR OS PONTOS DE PRETO
        
        def anterior(x, y, cor):
            global x_aux
            global y_aux
            global completo
            if cor != cor_braco:
                completo[y][x]["bg"] = cor
                
        def verifica_cor(x, y):#------ESTA FUNCAO FOI CRIADA PARA MESMO QUE O PONTO PRETO NAO ESTEJA ANDANDO, ELE VERIFIQUE A COR
            global cor_aux#-----E QUANDO ENCONTRAR UMA COR POSSIVEL DE ANDAR ELE ATUALIZE AUTOMATICAMENTE
            global completo
            cor_aux = completo[y][x]["bg"]
        
        
        def atualizar():#----ESTA FUNCAO É A QUE FAZ O PROGRAMA FUNCIONAR, DENTRO DELA ESTAO TODAS AS FUNCOES QUE PRECISAM SER VERIFICADAS O TEMPO INTEIRO
            global pintou
            pintou = 1 #------IRA QUEBRAR O LOOP APENAS QUANDO A FUNÇAO SET_COR FOR PROPRIAMENTE EXECUTADA
            global cont
            
            coraCheio_lb[0]["image"] = balde1
            coraCheio_lb[1]["image"] = balde2
            coraCheio_lb[2]["image"] = balde3            

            highscore["image"] = top
            legenda["image"] = legen
            interacoes_lb["image"] = interacoes_img
            amor_amarelo_lb["image"] = amor_amarelo
            comer_amarelo_lb["image"] = comer_amarelo
            passinho_amarelo_lb["image"] = passinho_amarelo
            cursor_lb["image"] = cursor_img

#----------------------------------------VERIFICANDO CAMALEAO E COR----------------------------
            total_reports = n_laranja + n_verde + n_roxo + n_amarelo + n_vermelho + n_azul

            if n_laranja >= n_verde and n_laranja >= n_roxo and n_laranja >= n_amarelo and n_laranja >= n_vermelho and n_laranja >= n_azul:
                if total_reports < 40:
                    camaleao["image"] = ovo_img
                    faltando["text"] = faltando["text"]+"/40"
                elif total_reports >= 40 and total_reports < 80:
                    camaleao["image"] = a2_img
                    faltando["text"] = faltando["text"]+"/80"
                elif total_reports >= 80 and total_reports < 120:
                    camaleao["image"] = b2_img
                    faltando["text"] = faltando["text"]+"/120"
                elif total_reports >= 120:
                    camaleao["image"] = c2_img
                    faltando["text"] = "EXP: "+str(total_reports)

            elif n_verde >= n_laranja and n_verde >= n_roxo and n_verde >= n_amarelo and n_verde >= n_vermelho and n_verde >= n_azul:
                if total_reports < 40:
                    camaleao["image"] = ovo_img
                    faltando["text"] = faltando["text"]+"/40"
                elif total_reports >= 40 and total_reports < 80:
                    camaleao["image"] = a4_img
                    faltando["text"] = faltando["text"]+"/80"
                elif total_reports >= 80 and total_reports < 120:
                    camaleao["image"] = b4_img
                    faltando["text"] = faltando["text"]+"/120"
                elif total_reports >= 120:
                    camaleao["image"] = c4_img
                    faltando["text"] = "EXP: "+str(total_reports)

            elif n_roxo >= n_verde and n_roxo >= n_laranja and n_roxo >= n_amarelo and n_roxo >= n_vermelho and n_roxo >= n_azul:
                if total_reports < 40:
                    camaleao["image"] = ovo_img
                    faltando["text"] = faltando["text"]+"/40"
                elif total_reports >= 40 and total_reports < 80:
                    camaleao["image"] = a6_img
                    faltando["text"] = faltando["text"]+"/80"
                elif total_reports >= 80 and total_reports < 120:
                    camaleao["image"] = b6_img
                    faltando["text"] = faltando["text"]+"/80"
                elif total_reports >= 120:
                    camaleao["image"] = c6_img
                    faltando["text"] = "EXP: "+str(total_reports)

            elif n_amarelo >= n_verde and n_amarelo >= n_roxo and n_amarelo >= n_laranja and n_amarelo >= n_vermelho and n_amarelo >= n_azul:
                if total_reports < 40:
                    camaleao["image"] = ovo_img
                    faltando["text"] = faltando["text"]+"/40"
                elif total_reports >= 40 and total_reports < 80:
                    camaleao["image"] = a3_img
                    faltando["text"] = faltando["text"]+"/80"
                elif total_reports >= 80 and total_reports < 120:
                    camaleao["image"] = b3_img
                    faltando["text"] = faltando["text"]+"/120"
                elif total_reports >= 120:
                    camaleao["image"] = c3_img
                    faltando["text"] = "EXP: "+str(total_reports)

            elif n_vermelho >= n_verde and n_vermelho >= n_roxo and n_vermelho >= n_amarelo and n_vermelho >= n_laranja and n_vermelho >= n_azul:
                if total_reports < 40:
                    camaleao["image"] = ovo_img
                    faltando["text"] = faltando["text"]+"/40"
                elif total_reports >= 40 and total_reports < 80:
                    camaleao["image"] = a1_img
                    faltando["text"] = faltando["text"]+"/80"
                elif total_reports >= 80 and total_reports < 120:
                    camaleao["image"] = b1_img
                    faltando["text"] = faltando["text"]+"/120"
                elif total_reports >= 120:
                    camaleao["image"] = c1_img
                    faltando["text"] = "EXP: "+str(total_reports)

            elif n_azul >= n_verde and n_azul >= n_roxo and n_azul >= n_amarelo and n_azul >= n_vermelho and n_azul >= n_laranja:
                if total_reports < 40:
                    camaleao["image"] = ovo_img
                    faltando["text"] = faltando["text"]+"/40"
                elif total_reports >= 40 and total_reports < 80:
                    camaleao["image"] = a5_img
                    faltando["text"] = faltando["text"]+"/80"
                elif total_reports >= 80 and total_reports < 120:
                    camaleao["image"] = b5_img
                    faltando["text"] = faltando["text"]+"/120"
                elif total_reports >= 120:
                    camaleao["image"] = c5_img
                    faltando["text"] = "EXP: "+str(total_reports)

#--------------------------------------INICIANDO FUNCOES NORMAIS---------------------------------

            while pintou == 1:#-----A CADA 0.05s ESTA FUNCAO É EXECUTADA DESCOBRINDO ASSIM O QUE O USUARIO ESTA FAZENDO E MOSTRANDO ESTE RESULTADO NA TELA
                global x
                global y
                global x_aux
                global y_aux
                global cor_aux
        
                data = open('arquivos/data.txt', 'r')#-----LE-SE O ARQUIVO QUE CONTEM A INFORMAÇAO DO ARDUINO(POTENCIOMETROS PARA POSICAO E CLICK DE BOTAO)
                for i in data:
                    info = i.split(',')
                print(info)
        
                x_aux = x
                y_aux = y
                cor = info[0]
                x = int(info[1])
                y = int(info[2])
                data.close()
                if y <= 21 and y_aux <= 21:
                    cursor_lb.place(x = 100, y = 5000)
                    if cor_aux != cor_preto:#----QUANDO A COR AUXILIAR É DIFERENTE DE BRANCO, AS FUNCOES ANDAR E PINDAR SAO EXECUTADAS NORMALMENTE
                        if cor == 'w':#----SE A INFORMAÇAO CHEGADA DO ARDUINO FOIR 'w'(walk) A FUNÇAO ANDAR É EXECUTADA(ELA ACONTECE EM DUAS ETAPAS)
                            anterior(x_aux,y_aux,cor_aux)#----A FUNÇÃO ANTERIOR SERVE PARA PREENCHER O QUADRADO QUE DEIXARA DE SER PRETO COM A COR ANTERIOR
                            walk_bt(x,y)#------------A FUNÇAO WALK PREENCHE A NOVA POCISAO COM A COR PRETA E SALVA A COR ANTERIOR, PARA CASO O USUARIO ANDE NOVAMENTE
                        else:
                            anterior(x_aux,y_aux,cor_aux)
                            set_cor(x,y)
                    else:#--------------------CASO CONTRARIO ACONTECE UMA VERIFICAÇAO DE COR, ATE UMA COR VALIDA SER ENCONTRADA
                        verifica_cor(x, y)
                else:
                    if y == 23:
                        cursor_lb.place(x = 897, y = 554)
                        if y_aux <= 21:
                            anterior(x_aux,y_aux,cor_aux)

                        if cor == 'A' and total_reports >= 40 and total_reports <= 80:        
                            amor_amarelo_lb.place(x = 919, y = 545)
                            frase_masco[cont]["text"] = frases()
                            amor_peque()
                            coraCheio_lb[cont]["image"] = cora_vazio
                            cont += 1
                            if cont == 3:
                                funcdaltonico1()
                                info_arquivo()
                                pintou = 0
                                background(obrigado)
                                background(selecionador_1)
                                interface.destroy()
                                root.destroy()
                                time.sleep(1)
                                cont = 0
                            amor_amarelo_lb.place(x = 920, y = 5450)

                        if cor == 'A' and total_reports >= 80 and total_reports <= 120:        
                            amor_amarelo_lb.place(x = 919, y = 545)
                            frase_masco[cont]["text"] = frases()
                            amor_medio()
                            coraCheio_lb[cont]["image"] = cora_vazio
                            cont += 1
                            if cont == 3:
                                funcdaltonico1()
                                info_arquivo()
                                pintou = 0
                                background(obrigado)
                                background(selecionador_1)
                                interface.destroy()
                                root.destroy()
                                time.sleep(1)
                                cont = 0
                            amor_amarelo_lb.place(x = 920, y = 5450)


                        if cor == 'A' and total_reports >= 120:        
                            amor_amarelo_lb.place(x = 919, y = 545)
                            frase_masco[cont]["text"] = frases()
                            amor_grande()
                            coraCheio_lb[cont]["image"] = cora_vazio
                            cont += 1
                            if cont == 3:
                                funcdaltonico1()
                                info_arquivo()
                                pintou = 0
                                background(obrigado)
                                background(selecionador_1)
                                interface.destroy()
                                root.destroy()
                                time.sleep(1)
                                cont = 0
                            amor_amarelo_lb.place(x = 920, y = 5450)


                        elif cor == 'A' and total_reports < 40:
                            frase_masco[cont]["text"] = "Primeiro eu preciso crescer!"
                        y_aux = 21
                    elif y == 24:
                        cursor_lb.place(x = 897, y = 609)
                        if y_aux <= 21:
                            anterior(x_aux,y_aux,cor_aux)
                        if cor == 'A' and total_reports >= 80 and total_reports < 120:
                            comer_amarelo_lb.place(x = 920, y = 598)
                            frase_masco[cont]["text"] = frases()
                            comer_medio()
                            coraCheio_lb[cont]["image"] = cora_vazio
                            cont += 1
                            if cont == 3:
                                funcdaltonico1()
                                info_arquivo()
                                pintou = 0
                                background(obrigado)
                                background(selecionador_1)
                                interface.destroy()
                                root.destroy()
                                time.sleep(1)
                                cont = 0
                            comer_amarelo_lb.place(x = 920, y = 6000)
                        elif cor == 'A' and total_reports >= 120:
                            comer_amarelo_lb.place(x = 920, y = 598)
                            frase_masco[cont]["text"] = frases()
                            comer_grande()
                            coraCheio_lb[cont]["image"] = cora_vazio
                            cont += 1
                            if cont == 3:
                                funcdaltonico1()
                                info_arquivo()
                                pintou = 0
                                background(obrigado)
                                background(selecionador_1)
                                interface.destroy()
                                root.destroy()
                                time.sleep(1)
                                cont = 0
                            comer_amarelo_lb.place(x = 920, y = 6000)
                        elif cor == 'A' and total_reports < 80:
                            frase_masco[cont]["text"] = "Primeiro eu preciso crescer!"
                        y_aux = 21


                    elif y == 25:
                        cursor_lb.place(x = 897, y = 664)
                        if y_aux <= 21:
                            anterior(x_aux,y_aux,cor_aux)
                        if cor == 'A' and total_reports > 120:
                            passinho_amarelo_lb.place(x = 920, y = 651)
                            frase_masco[cont]["text"] = frases()
                            passinho()
                            coraCheio_lb[cont]["image"] = cora_vazio
                            cont += 1
                            if cont == 3:
                                funcdaltonico1()
                                info_arquivo()
                                pintou = 0
                                background(obrigado)
                                background(selecionador_1)
                                interface.destroy()
                                root.destroy()
                                time.sleep(1)
                                cont = 0
                            passinho_amarelo_lb.place(x = 920, y = 6550)
                        elif cor == 'A' and total_reports < 120:
                            frase_masco[cont]["text"] = "Primeiro eu preciso crescer!"
                        y_aux = 21
                time.sleep(0.3)
            
        background(atualizar)

#--------------ABRE INTERFACE INICIAL--------------------------

parte1 = Tk()
parte1.geometry("+0+0")
parte1.title("HUMORSAICO")
parte1["bg"] = cor_preto

interface1_im = PhotoImage(file = "imagens/interface.png")
interface1 = Label(parte1, image = interface1_im, bg = cor_preto)
interface1.place(x = 0, y = 0)

abre_completo_baixo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for i in range(112):
    abre_completo_baixo[i] = Label(parte1, width = 2, height = 1, bg = cor_preto)
    abre_completo_baixo[i].grid(row = 50 + i, column = 90)

abre_completo_lado = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 1, 1, 1,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 1, 1, 1,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 1, 1, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 1, 1, 1,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 1, 1, 1,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 1, 1, 1]
for i in range(138):
    abre_completo_lado[i] = Label(parte1, width = 2, height = 1, bg = cor_preto)
    abre_completo_lado[i].grid(row = 50, column = i)



frase = PhotoImage(file = 'imagens/frase.png')
frase_pisca = Label(parte1, image = frase, bg = cor_preto)

def pisca_frase():
    while True:
        frase_pisca.place(x = 540, y = 525)
        time.sleep(1)
        frase_pisca.place(x = 10000, y = 525)
        time.sleep(1)

def selecionador_1():
    global usuario
    global rfid
    global dados
    with open ('arquivos/banco_dados.json') as todos_dados:
        dados = json.load(todos_dados)
    registrado = 0
    usuario = "Anonimo"
    rfid = "0"
    while True:
        data = open('arquivos/data.txt', 'r')
        for i in data:
            info = i.split(',')
        print(info)
        sel = info[0]
        rfid = info[1]
        for i in dados:
            if i == rfid:
                usuario = dados[i]['nome'].split(" ")
                usuario = usuario[0]+" "+usuario[-1]
                registrado = 1
        if registrado == 0:
            usuario = "Anonimo"
            rfid = "0"

        if sel == 'R':
            abre_parte2()
            break
        elif sel == 'A':
            usuario = "Anonimo"
            rfid = "0"
            time.sleep(2)
            abre_parte2()
            break
        time.sleep(0.5)

background(selecionador_1)
background(pisca_frase)

parte1.mainloop()
