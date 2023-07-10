import socket

HOST = 'localhost'
PORT = 4444

    # criando o cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # conectando o cliente ao servidor
client.connect((HOST, PORT))

mensadem_do_servidor = client.recv(1024)
if mensadem_do_servidor == b'sala':
    client.send(b'jogos') # sala
    client.send(b'lazaro') # nome do client