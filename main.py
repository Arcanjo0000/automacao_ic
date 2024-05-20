import tkinter as tk
import customtkinter as ctk
from classe.tabela import Tabela
from script.pegando_caminho_tabelas import pergunta
from script.lendo_json import ler_caminhos, ler_estrutura
from script.abrindo_tabelas import acessando_os_caminhos, acessando_tabelas
from script.tratamento_de_dados import pegando_arquivos_com_dados

def confirmar(janela):
    fechar_janela(janela)
    pegando_arquivos_com_dados()

def fechar_janela(janela):
    janela.destroy()

def encerrar(janela):
    fechar_janela(janela)
    print("encerrando")
    exit()

def continuar():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTk()
    janela.geometry("780x480")
    janela.title("deseja comtinuar?")
    
    ctk.CTkButton(janela, "Sim", command=lambda:confirmar(janela))
    ctk.CTkButton(janela, "Não", command=lambda:encerrar(janela))

    janela.mainloop()



def main():
    pergunta()    
    caminhos = ler_caminhos()
    estrutura = ler_estrutura()
    Tabela.setTabela(caminhos, estrutura)
    caminhos_utilizaveis = acessando_os_caminhos()
    acessando_tabelas(caminhos_utilizaveis)
    
    


if __name__ == "__main__":
    main()