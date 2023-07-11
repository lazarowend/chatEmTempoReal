import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog

class Chat:
    def __init__(self) -> None:
        HOST = '127.0.0.1'
        PORT = 8000
            # criando o cliente
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # conectando o cliente ao servidor
        self.client.connect((HOST, PORT))
        
        login = Tk()
        login.withdraw()

        self.janela_carregada = False
        self.ativo = True
        
        self.nome = simpledialog.askstring('Nome', 'Digite seu nome!', parent=login)
        self.sala = simpledialog.askstring('Sala', 'Digite a sala em que quer entrar!', parent=login)
        
        thread = threading.Thread(target=self.conecta)
        thread.start()
        
        self.janela()


    def janela(self):
        self.root = Tk()
        self.root.geometry("300x500")
        self.root.title('Chat')
            
        self.caixa_texto = Text(self.root, font=16)
        self.caixa_texto.place(relx=0.025, rely=0.01, width=280, height=400, bordermode='outside')
        
        self.envia_mensagem = Entry(self.root, font=16)
        self.envia_mensagem.place(relx=0.025, rely=0.9, width=220, height=20)
        
        self.btn_enviar = Button(self.root, text='Enviar', command=self.enviar_mensagem, font=16)
        self.btn_enviar.place(relx=0.8, rely=0.9, width=50, height=20)
        self.root.protocol('WM_DELETE_WINDOW', self.fechar)
        
        
        self.root.mainloop()
        
        
    # fecha a janela ao client sair
    def fechar(self):
        self.root.destroy()
        self.client.close()
        
    def conecta(self):
        while True:
        # recebe o nome do client e o nome da sala e a mensagem
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
        self.envia_mensagem.delete(0, END)
        
        
chat = Chat()
