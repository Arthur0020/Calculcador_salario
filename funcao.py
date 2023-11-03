import openpyxl

#função valor * aulas
def valor_aulas(a, b):
    resultado1 = a * b
    return resultado1

#função vale transporte
def vale_transporte(c, d):
    resultado2 = c + d
    return resultado2

#função desconto
def descontos(e, f):
    resultado3 = e - f
    return resultado3

#função salário líquido total
def salario_total(g, h):
    resultado4 = g + h
    return resultado4

#função opção inválida
def opcao_invalida():
    print('Opção inválida, tente novamente')

#criando a planilha para a inserção dos dados
book = openpyxl.Workbook()
book.create_sheet('Salários')
Pagina_salarios = book['Salários']
Pagina_salarios.append(['Professor' , 'Valor aula' , 'nº aulas-1' , 'Salário bruto-1' , 'Vale transporte-1', 'Descontos-1' , 'Salário líquido-1' , '//', 'valor aula' , 'nº aulas-2' , 'Salário bruto-2' , 'Vale transporte-2', 'Descontos-2' , 'Salário líquido-2' , 'Salário total'])

#função principal
def funcao_principal():
    #Declaração das variáveis
    prof01 = 'Beatriz'
    prof02 = 'Cláudia'
    prof03 = 'Cláudio'
    prof05 = 'Fernando'
    prof06 = 'Luciana Dini'
    prof04 = 'Fernanda'
    prof07 = 'Michele'
    prof08 = 'Magali'
    prof09 = 'Tatiane Mística'
    prof10 = 'Tatiany Ribeiro'
    prof11 = 'Rodrigo'
    prof12 = 'Bruno Estagiário'
    prof13 = 'Lara Estagiária'
    prof14 = 'Vitor Estagiário'




    #Menu de escolha
    escolha = int(input('''
Escolha o colaborador de acordo com o número do identificador:
--------------------------------------------------------------
[1] Beatriz
[2] Cláudia
[3] Cláudio
[4] Fernanda
[5] Fernando
[6] Luciana Dini
[7] Michele
[8] Magali
[9] Tatiane Mística
[10] Tatiany Ribeiro
[11] Rodrigo
[12] Bruno Estagiário
[13] Lara Estagiária
[14] Vitor Estagiário

>:'''))

#Loop de verificação
    while True:
        if escolha == 1:
            print(f'Professor(a) escolhido: {prof01}')
            professor = prof01
            break
    
        elif escolha == 2:
            print(f'Professor(a) escolhido: {prof02}')
            professor = prof02
            break

        elif escolha == 3:
            print(f'Professor(a) escolhido: {prof03}')
            professor = prof03 
            break

        elif escolha == 4:
            print(f'Professor(a) escolhido: {prof04}')
            professor = prof04
            break 

        elif escolha == 5:
            print(f'Professor(a) escolhido: {prof05}')
            professor = prof05
            break 

        elif escolha == 6:
            print(f'Professor(a) escolhido: {prof06}')
            professor = prof06
            break  

        elif escolha == 7:
            print(f'Professor(a) escolhido: {prof07}')
            professor = prof07
            break 

        elif escolha == 8:
            print(f'Professor(a) escolhido: {prof08}')
            professor = prof08
            break  

        elif escolha == 9:
            print(f'Professor(a) escolhido: {prof09}')
            professor = prof09
            break  

        elif escolha == 10:
            print(f'Professor(a) escolhido: {prof10}')
            professor = prof10
            break      

        elif escolha == 10:
            print(f'Professor(a) escolhido: {prof10}')
            professor = prof10
            break 

        elif escolha == 11:
            print(f'Professor(a) escolhido: {prof11}')
            professor = prof11
            break 

        elif escolha == 12:
            print(f'Professor(a) escolhido: {prof12}')
            professor = prof12
            break         

        elif escolha == 13:
            print(f'Professor(a) escolhido: {prof13}')
            professor = prof13
            break 

        elif escolha == 14:
            print(f'Professor(a) escolhido: {prof14}')
            professor = prof14
            break  

        else:
            print('Identificador inválido, por favor tente novamente\n')
            escolha = int(input('''
Escolha o colaborador de acordo com o número do identificador:
--------------------------------------------------------------
[1] Beatriz
[2] Cláudia
[3] Cláudio
[4] Fernanda
[5] Fernando
[6] Luciana Dini
[7] Michele
[8] Magali
[9] Tatiane Mística
[10] Tatiany Ribeiro
[11] Rodrigo
[12] Bruno Estagiário
[13] Lara Estagiária
[14] Vitor Estagiário

>:'''))
            
    #Input do valor da aula
    valor_aula = input('Digite o valor da hora aula deste professor:\n>:R$ ')
    valor_aula = valor_aula.replace(',' , '.')
    valor_aula_formatado = float(valor_aula)

    #Input do numero de aulas
    numero_aulas1 = int(input('Digite o número de aulas que este professor realizou neste mês:\n>: '))

    #Valor do salario bruto
    salario = valor_aulas(valor_aula_formatado, numero_aulas1)

    #Input do vale transporte
    valor_transporte = input('Digite o valor do vale transporte:\n>:R$ ')
    valor_transporte = valor_transporte.replace(',' , '.')
    transporte = float(valor_transporte)

    #Valor do salário bruto + vale transporte
    salario_transporte = vale_transporte(salario, transporte)

    #Input do desconto
    desconto_salario = input('Digite o valor do desconto:\n>:R$ ')
    desconto_salario = desconto_salario.replace(',' , '.')
    desconto = float(desconto_salario)

    #Valor do salário bruto + vale transporte - descontos
    salario_liquido1 = descontos(salario_transporte, desconto)

    #Valor do salário líquido 1
    salario_formatado1 = f'{salario_liquido1:.2f}'.replace('.' , ',')
    print(f'O Salário 1 do(a) professor(a) {professor} será de R${salario_formatado1}')

    #inserindo os dados na planilha
    Pagina_salarios.append([professor , valor_aula , numero_aulas1 , salario , transporte , desconto , salario_formatado1])
    book.save('Salários dos professores.xlsx')

    #Segundo menu de escolha
    escolha2 = int(input('''
Deseja cadastrar mais um valor para este professor?
---------------------------------------------------
[1] Sim
[2] Não
                     
>:'''))
    
    while True:
        if escolha2 == 1:
    
            #Input do valor da aula
            valor_aula2 = input('Digite o valor da hora aula deste professor:\n>:R$ ')
            valor_aula2 = valor_aula2.replace(',' , '.')
            valor_aula_formatado2 = float(valor_aula2)

            #Input do numero de aulas
            numero_aulas2 = int(input('Digite o número de aulas que este professor realizou neste mês:\n>: '))

            #Valor do salario bruto
            salario2 = valor_aulas(valor_aula_formatado2, numero_aulas2)

            #Input do vale transporte
            valor_transporte2 = input('Digite o valor do vale transporte:\n>:R$ ')
            valor_transporte2 = valor_transporte2.replace(',' , '.')
            transporte2 = float(valor_transporte2)

            #Valor do salário bruto + vale transporte
            salario_transporte2 = vale_transporte(salario2, transporte2)

            #Input do desconto
            desconto_salario2 = input('Digite o valor do desconto:\n>:R$ ')
            desconto_salario2 = desconto_salario2.replace(',' , '.')
            desconto2 = float(desconto_salario2)

            #Valor do salário líquido 2
            salario_liquido2 = descontos(salario_transporte2, desconto2)

            salario_formatado2 = f'{salario_liquido2:.2f}'.replace('.' , ',')
            print(f'O Salário 2 do(a) professor(a) {professor} será de R${salario_formatado2}')

            Salario_liquido_total1 = salario_total(salario_liquido1, salario_liquido2)

            #inserindo os dados na planilha
            Pagina_salarios.append([professor , valor_aula , numero_aulas1 , salario , transporte , desconto , salario_formatado1, '//', valor_aula2 , numero_aulas2 , salario2, transporte2, desconto2, salario_formatado2, Salario_liquido_total1])
            book.save('Salários dos professores.xlsx')
            break

        else:
            break


                        