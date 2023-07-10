import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog

class Chat:
    def __init__(self) -> None:
        HOST = 'localhost'
        PORT = 8000
            # criando o cliente
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # conectando o cliente ao servidor
        client.connect((HOST, PORT))

        self.janela_carregada = False
        self.ativo = True
        self.nome = simpledialog.askstring('Nome', 'Digite seu nome!', parent=login)
        self.sala = simpledialog.askstring('Sala', 'Digite a sala em que quer entrar!', parent=login)


    
chat = Chat()
