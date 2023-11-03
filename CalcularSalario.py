from tkinter import *
import openpyxl
from funcao import valor_aulas
from funcao import vale_transporte
from funcao import descontos
from funcao import funcao_principal
from funcao import opcao_invalida


while True:
    menu = int(input('''
Digite a opção desejada:
[1] Cadastrar salário
[2] Fechar programa
        
>:'''))
    while menu != 1 and menu != 2:
        opcao_invalida()
        menu = int(input('''
Digite a opção desejada:
[1] Cadastrar salário
[2] Fechar programa
        
>:'''))
    if menu == 1:
        funcao_principal()
    else:
        break    
    
print('Abra sua planilha para vizualizar os dados')    






