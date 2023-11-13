# _*_ Cod 0612 _28_
"""
Creado em 11 de setembro, as 16:25 

@autor: José Anderson
"""

import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
import datetime as dt

lista_tipos = ["Caderno","Lápis","Caneta", "Borracha","Apontador", "Folha de ofício", "Cartolina", "Grampiador", "Grampo" ]
lista_codigos = []

janela = tk.Tk()

#Criação da função

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str,descricao,tipo,quant,data_criacao))

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )

entry_descricao = tk.Entry()
entry_descricao.grid(row=2,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)

label_tipo_unidade = tk.Label(text="Produtos")
label_tipo_unidade.grid(row=3, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

label_quant =  tk.Label(text="Preço")
label_quant.grid(row=4, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )

entry_quant =  tk.Entry()
entry_quant.grid(row=4, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_Lote =  tk.Label(text="Lote")
label_Lote.grid(row=7, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )

entry_Lote =  tk.Entry()
entry_Lote.grid(row=7, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

botao_cadastrar_produto = tk.Button(text="Cadastrar Produto", command=inserir_codigo)
botao_cadastrar_produto.grid(row=5,column=0,padx = 10, pady=10,sticky='nswe', columnspan =4)
#-----------------------------------------------------------------------------
#Atualizar Produto
#-----------------------------------------------------------------------------     
botao_atualizar_produto = tk.Button(text="Atualizar Produto", command=inserir_codigo)
botao_atualizar_produto.grid(row=6,column=0,padx = 10, pady=10,sticky='nswe', columnspan =5)
#-----------------------------------------------------------------------------
#Excluir Produto
#-----------------------------------------------------------------------------  
botao_excluir_produto = tk.Button(text="Excluir Produto", command=inserir_codigo)
botao_excluir_produto.grid(row=8,column=0,padx = 10, pady=10,sticky='nswe', columnspan =6)
print('Produto Excluído com Sucesso!')   
print('Não foi possível fazer a exclusão do produto.')
#-----------------------------------------------------------------------------
#Limpar Tela
#----------------------------------------------------------------------------- 
botao_limpar_produto = tk.Button(text="Limpar", command=inserir_codigo)
botao_limpar_produto.grid(row=9,column=0,padx = 10, pady=10,sticky='nswe', columnspan =7)
print('Campos Limpos!')
#-----------------------------------------------------------------------------
#Título da Janela
#-----------------------------------------------------------------------------
janela.title('Ferramenta de cadastro de materiais')
janela['bg'] = "blue"
janela.geometry("390x410+10+10")
janela.mainloop()

print(lista_codigos)
