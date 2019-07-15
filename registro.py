import json



while True:
  print("Passe seu cartao no leitor de RFID")
  arquivo = open("arquivos/data.txt", "r")

  for i in arquivo:
    info = i.split(',')
  if info[0] == 'R':
    rfid = info[1]
    break    

print("\n"*40)
matricula = input("Digite a sua matricula: ")
nome = input("Digite o seu nome completo: ")
nome2 = nome.lower().split(" ")
email = ""
for i in nome2:
  email += i[0]
email += "@cesar.school"


ano_atual = 20191
ano_matri = matricula[0:5]
curso = matricula[6]
key_periodo = ano_atual - int(ano_matri)
periodo=1
cursot=""
j=0

if key_periodo%10 == 0:
  for i in range(0,40,10):
    j += 2
    if key_periodo == i:
      periodo = j-1

else:
  for i in range(0,50,10):
    j += 2
    if key_periodo == i +1 or key_periodo == i+9:
      periodo = j

if curso == "1":
  cursot = "CC"
elif curso == "2":
  cursot = "Design"


print("Nome: ", nome)
print("Email: ", email)
print("Curso: ", cursot)
print("Periodo: ", periodo)
print("Matricula: ", matricula)

corrige = input("Deseja corrigir seu email? (s/n): ")
if corrige == 's':
  email = input("Digite seu email(sem o @cesar.school): ")+"@cesar.school"

  print("Nome: ", nome)
  print("Email: ", email)
  print("Curso: ", cursot)
  print("Periodo: ", periodo)
  print("Matricula: ", matricula)  

#-----------------------------------------------------------------------

with open ('arquivos/banco_dados.json') as aaa:
  biblioteca = json.load(aaa)


biblioteca[rfid] = {"nome": nome, "email": email, "curso": curso, "periodo": periodo, "matricula": matricula, "score": 0, "top": 0, "humor": {"euforico": 0, "feliz": 0, "entediado": 0, "ansioso": 0, "raivoso": 0, "triste": 0}}


with open("arquivos/banco_dados.json", 'w') as aa:
  json.dump(biblioteca, aa)

  #------------------------------------------------------------------------

with open ("arquivos/banco_dados_global.json") as bbb:
  biblio = json.load(bbb)


biblio[rfid] = {"nome": nome, "email": email, "curso": curso, "periodo": periodo, "matricula": matricula, "score": 0, "top": 0, "humor": {"euforico": 0, "feliz": 0, "entediado": 0, "ansioso": 0, "raivoso": 0, "triste": 0}}
 
with open("arquivos/banco_dados_global.json", 'w') as aaaa:
  json.dump(biblio, aaaa)


#------------------------------------------------------------------------------
with open ("arquivos/banco_dados_branco.json") as ccc:
  bibli = json.load(ccc)

bibli[rfid] = {"nome": nome, "email": email, "curso": curso, "periodo": periodo, "matricula": matricula, "score": 0, "top": 0, "humor": {"euforico": 0, "feliz": 0, "entediado": 0, "ansioso": 0, "raivoso": 0, "triste": 0}}
 

with open("arquivos/banco_dados_branco.json", 'w') as a:
  json.dump(bibli, a)

print("Registro bem sucedido!!")








  
  
  
  