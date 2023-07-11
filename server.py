import socket
import threading

HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

    # função para enviar a mensagem dentro da sala para todos os cliente conectados
def broadcast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        
        i.send(mensagem)

    # função para receber a mensagem do client e enviar na sala
def enviar_mensagem(nome, sala, client):
    while True:
        mensagem = client.recv(1024)
        mensagem = f'{nome}: {mensagem.decode()}\n'
        broadcast(sala, mensagem)


    # quando client conectar tenho essas informações <socket.socket fd=424, family=2, type=1, proto=0, laddr=('127.0.0.1', 4444), raddr=('127.0.0.1', 59857)>
while True:
    client, addr = server.accept()

    client.send(b'sala')
    sala = client.recv(1024).decode()
    nome = client.recv(1024).decode()
    
    if sala not in salas.keys():
        salas[sala] = []

    salas[sala].append(client)
    print(f'{nome} se conectou na sala {sala}! INFO {addr}')
    broadcast(sala, f'{nome} se conectou na sala!\n')

    thread = threading.Thread(target=enviar_mensagem, args=(nome, sala, client))
    thread.start()