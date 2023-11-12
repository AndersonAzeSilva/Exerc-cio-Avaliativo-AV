# _*_ Cod 0612 _28_
"""
Creado em 11 de setembro, as 16:25 

@autor: José Anderson
"""

import tkinter as tk
from tkinter import ttk
import crud.py as crud.py

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()  

        #-----Componentes do Sistema--------------------------

        self.lbID=tk.Label(win, text='ID do Produto:')
        self.lblLote=tk.Label(win, text='Lote')
        self.lblNome=tk.Label(win, text='Nome do Produto')
        self.lblPreco=tk.Label(win, text='Preço')
        
        self.txtID=tk.Entry(bd=3)
        self.txtLote=tk.Entry()
        self.txtNome=tk.Entry()
        self.txtPreco=tk.Entry()    

        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)     

        #----- Componente TreeView --------------------------------------------

        self.dadosColunas = ("ID", "Nome", "Lote", "Preço")            
                
        self.treeProdutos = ttk.Treeview(win, 
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)        
        self.verscrlbar.pack(side ='right', fill ='x')
                                
        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        
        self.treeProdutos.heading("ID", text="ID")
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("Lote", text="Lote")
        self.treeProdutos.heading("Preço", text="Preço")        

        self.treeProdutos.column("ID",minwidth=0,width=75)
        self.treeProdutos.column("Nome",minwidth=0,width=75)
        self.treeProdutos.column("Lote",minwidth=0,width=75)
        self.treeProdutos.column("Preço",minwidth=0,width=75)

        self.treeProdutos.pack(padx=10, pady=10)
        
        self.treeProdutos.bind("<<TreeviewSelect>>", 
                               self.apresentarRegistrosSelecionados)                  
        #---------------------------------------------------------------------        
        #posicionamento dos componentes na janela
        #---------------------------------------------------------------------                
        self.lblNome.place(x=100, y=50)
        self.txtNome.place(x=250, y=50)

        self.lbID.place(x=100, y=100)
        self.txtID.place(x=250, y=80)

        self.lblLote.place(x=100, y=80)
        self.txtLote.place(x=250, y=110)
        
        self.lblPreco.place(x=100, y=140)
        self.txtPreco.place(x=250, y=140)
               
        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)
                   
        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=605, y=300, height=225)        
        self.carregarDadosIniciais()
#-----------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeProdutos.selection():  
            item = self.treeProdutos.item(selection)  
            ID,Lote,nome,preco = item["values"][0:3]  
            self.txtID.insert(0, ID)
            self.txtLote.insert(0, Lote)  
            self.txtNome.insert(0, nome)  
            self.txtPreco.insert(0, preco)  
#-----------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0          
          registros=self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              ID=item[0]
              Lote=item[11]
              nome=item[2]
              preco=item[3]
              print("ID = ", ID)
              print("Lote = ", Lote)
              print("Nome = ", nome)
              print("Preço  = ", preco, "\n")
                        
              self.treeProdutos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(ID,
                                           nome,
                                           Lote,
                                           preco))                        
              self.iid = self.iid + 1
              self.id = self.id + 1
          print('Dados da Base')        
        except:
          print('Ainda não existem dados para carregar')            
#-----------------------------------------------------------------------------
#LerDados da Tela
#-----------------------------------------------------------------------------           
    def fLerCampos(self):
        try:
          print("************ dados dsponíveis ***********") 
          id = int(self.txtid.get())
          print('id', id)
          nome=self.txtNome.get()
          print('nome', nome)
          preco=float(self.txtPreco.get())          
          print('preco', preco)
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return id, nome, preco
#-----------------------------------------------------------------------------
#Cadastrar Produto
#-----------------------------------------------------------------------------           
    def fCadastrarProduto(self):
        try:
          print("************ dados dsponíveis ***********") 
          codigo, nome, preco= self.fLerCampos()                    
          self.objBD.inserirDados(codigo, nome, preco)                    
          self.treeProdutos.insert('', 'end',
                                iid=self.iid,                                   
                                values=(codigo,
                                        nome,
                                        preco))                        
          self.iid = self.iid + 1
          self.id = self.id + 1
          self.fLimparTela()
          print('Produto Cadastrado com Sucesso!')        
        except:
          print('Não foi possível fazer o cadastro.')
#-----------------------------------------------------------------------------
#Atualizar Produto
#-----------------------------------------------------------------------------           
    def fAtualizarProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          codigo, nome, preco= self.fLerCampos()
          self.objBD.atualizarDados(codigo, nome, preco)          
          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) 
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('Produto Atualizado com Sucesso!')        
        except:
          print('Não foi possível fazer a atualização.')
#-----------------------------------------------------------------------------
#Excluir Produto
#-----------------------------------------------------------------------------                  
    def fExcluirProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          codigo, nome, preco= self.fLerCampos()
          self.objBD.excluirDados(codigo)          
          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) 
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('Produto Excluído com Sucesso!')        
        except:
          print('Não foi possível fazer a exclusão do produto.')
#-----------------------------------------------------------------------------
#Limpar Tela
#-----------------------------------------------------------------------------                 
    def fLimparTela(self):
        try:
          print("************ dados dsponíveis ***********")        
          self.txtCodigo.delete(0, tk.END)
          self.txtNome.delete(0, tk.END)
          self.txtPreco.delete(0, tk.END)
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')
#-----------------------------------------------------------------------------
#Programa Principal
#-----------------------------------------------------------------------------          
janela=tk.Tk()
principal=PrincipalBD(janela)
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela['bg'] = "blue"
janela.geometry("720x600+10+10")
janela.mainloop()
#-----------------------------------------------------------------------------