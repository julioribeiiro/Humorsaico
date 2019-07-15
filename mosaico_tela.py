from tkinter import *
import json
import time
import threading

root = Tk()
root.title("HUMORSAICO")
root.geometry("+0+0")
root["bg"] = "black"

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


def background(func):#---------ESTA FUNÇAO PERMITE A EXECUÇAO DE UMA FUNÇAO(NO CASO A ATUALIZAR) NO BACKGROUND DO TKINTER
    th = threading.Thread(target = func)
    th.start()


def info_arquivo():#-------TRANSFORMA A VARIAVEL DE LABELS EM ARQUIVO, PARA PODER REABRIR A PAGINA DEPOIS DE PINTADA
    global completo
    completo = []
    texto = open("arquivos/logo2.txt", "r")
    for i in texto:#----------PEGANDO LINHA A LINHA DO ARQUIVO
        completo.append(list(i))
    texto.close()

info_arquivo()


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

cria_legenda()

j = 0
n = 1
coluna = 0
legen = PhotoImage(file = "imagens/legenda.png")
top = PhotoImage(file = "imagens/top.png")




#------------------IMAGENS DE FUNDO-----------------------------------------------------------
legenda = Label(root, image = legen, bg = cor_preto)
legenda.place(x=0, y=500)

#------------------------------PARTE DO MASCOTE---------------------------------------------------------------------

interacoes_img = PhotoImage(file = "imagens/btn_interacoes.png")
interacoes_lb = Label(root, image = interacoes_img, bg = cor_preto)
interacoes_lb.place(x = 920, y = 545)

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


def atualiza_mosaico():
    global completo

    while True:
        info_arquivo()
        cria_legenda()

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

        #--------------------NUMERO DE REPORTS----------------------------------------------------------------

        total_reports = n_laranja + n_verde + n_roxo + n_amarelo + n_vermelho + n_azul

        faltando = Label(root, text = "EXP: "+str(total_reports), fg = cor_braco, bg = cor_preto, font = "Minecraft 20")
        faltando.place(x = 1070, y = 490)

        numero_score = Label(root, bg = "black", fg = "white", text = "00000", font = "Minecraft 25")
        numero_score.place(x = 735, y = 61)

        numero_top = Label(root, width = 8, bg = cor_preto, fg = cor_braco, text = "0", font = "Minecraft 25")
        numero_top.place(x = 510, y = 61)

        frase_masco = Label(root, bg = cor_preto, fg = cor_braco, text = "Ola!\n Meu nome é TUMBAR!", font = "Minecraft 20")
        frase_masco.place(x = 1200, y = 460)


        
        highscore = Label(root, image = top, bg = cor_preto)
        highscore.place(x=0,y=0)

        coraCheio_lb = [1, 2, 3]
        cora_cheio = PhotoImage(file = "imagens/coraCheio.png")
        cora_vazio = PhotoImage(file = "imagens/coraVazio.png")

        coraCheio_lb[0] = Label(root, image = cora_cheio, bg = cor_preto)
        coraCheio_lb[0].place(x = 1270, y = 40)

        coraCheio_lb[1] = Label(root, image = cora_cheio, bg = cor_preto)
        coraCheio_lb[1].place(x = 1210, y = 40)

        coraCheio_lb[2] = Label(root, image = cora_cheio, bg = cor_preto)
        coraCheio_lb[2].place(x = 1150, y = 40)



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


        #----------------------------------------VERIFICANDO CAMALEAO E COR----------------------------

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

        print("Atualizou")
        time.sleep(10)

background(atualiza_mosaico)


root.mainloop()
