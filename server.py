import socket
import threading

HOST = 'localhost'
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

    # função para enviar a mensagem dentro da sala para todos os cliente conectados
def broadcast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        
        print(mensagem)

    # função para receber a mensagem do client e enviar na sala
def enviar_mensagem(nome, sala, client):
    while True:
        mensagem = client.recv(1024)
        mensagem = f'{nome}: {mensagem.decode()}\n'
        broadcast(sala, mensagem)


while True:
    client, addr = server.accept()
    # quando client conectar tenho essas informações <socket.socket fd=424, family=2, type=1, proto=0, laddr=('127.0.0.1', 4444), raddr=('127.0.0.1', 59857)>

    client.send(b'sala')
    sala = client.recv(1024).decode()
    nome_client = client.recv(1024).decode()
    
    if sala not in salas.keys():
        salas[sala] = []

    salas[sala].append(client)
    print(f'{nome_client} se conectou na sala {sala}! INFO {addr}')
    broadcast(sala, (f'{nome_client} se conectou na sala!').encode())

    thread = threading.Thread(target=enviar_mensagem, args=(nome_client, sala, client))
    thread.start()