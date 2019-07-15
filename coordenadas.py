import serial
ser = serial.Serial("/dev/cu.usbmodem14501", baudrate = 9600, timeout = 1)
while 1:
    nova = ''
    teste = ser.readline().decode('ascii')
    teste_1 = teste.split(',')
    print(teste_1)
    for i in range(len(teste_1) - 1):
        nova += teste_1[i]+','
    coordenadas = open("arquivos/data.txt", "w")
    coordenadas.writelines(nova)
    print(nova)
    coordenadas.close()
