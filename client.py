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
        
        login = Tk()
        login.withdraw()

        self.janela_carregada = False
        self.ativo = True
        self.nome = simpledialog.askstring('Nome', 'Digite seu nome!', parent=login)
        self.sala = simpledialog.askstring('Sala', 'Digite a sala em que quer entrar!', parent=login)
        self.janela()

        thread = threading.Thread(target=self.conecta)
        thread.start()

    def janela(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title('Chat')
            
        self.caixa_texto = Text(self.root, font=16)
        self.caixa_texto.place(relx=0.05, rely=0.01, width=700, height=600)
        
        self.envia_mensagem = Entry(self.root)
        self.envia_mensagem.place(relx=0.05, rely=0.8, width=600,height=20)
        
        self.btn_enviar = Button(self.root, text='Enviar', command=self.enviar_mensagem)
        self.btn_enviar.place(relx=0.9, rely=0.8, width=50, height=20)
        self.root.protocol('WM_DELETE_WINDOW', self.fechar)
        
        
        self.root.mainloop()
    # fecha a janela ao client sair
    def fechar(self):
        self.root.destroy()
        self.cliet.close()
        
    def conecta(self):
        # recebe o nome do cliet e o nome da sala e a mensagem
        recebido = self.client.recv(1024)
        
        # verifica se é a sala e o nome, se não é a mensagem que esta sendo recbida
        if recebido == b'sala':
            self.client.send(self.sala.encode())
            self.client.send(self.nome.encode())
        else:
            try:
                self.caixa_texto.insert('end', recebido.decode())
            except:
                pass



    def enviar_mensagem(self):
        
        # pego o valor do campo envia_mensagem
        mensagem = self.envia_mensagem.get()
        self.client.send(mensagem.encode())
        
        
        
chat = Chat()
