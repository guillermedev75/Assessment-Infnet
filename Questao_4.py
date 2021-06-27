#Aplicação para demostrar um grafico dos redimentos de um investimento

#Função que tem o objetivo de calcular os dados recebidos
def montante(inicial,rendimento,aporte,periodos, eixo_x, eixo_y):
    
    #Laço que calcula os remdimentos com base nos dados passados pelo individuo
    for n in range(1,periodos+1):
        novo_valor = round((inicial+(rendimento*inicial)/100) + aporte)
        inicial = novo_valor
        eixo_x.append(novo_valor)
        eixo_y.append(n)
        print(f"\nApós {n} períodos, o montante será de R${round(novo_valor)}.")

#Onde é importada a biblioteca que gera os graficos
import matplotlib.pyplot as plt
from Questao_4 import montante

#Função que gera os graficos com base nos dados gerados pela função "montante"
def grafico(eixo_x,eixo_y):
    x = eixo_x
    y = eixo_y
    plt.plot(x, y)
    plt.show()
    exit()

#Entrda dos dados do individuo
inicial = float(input("Informe o valor inicial: "))
rendimento = float(input("Informe o rendimento (%): "))
aporte = float(input("Informe o aporte a cada período:\nR$"))
periodos = int(input("Informe o total de períodos: "))

#Reset dos graficos
eixo_x = []
eixo_y = []

#Onde são chamadas as funções
montante(inicial, rendimento,aporte, periodos, eixo_x, eixo_y)
grafico(eixo_x, eixo_y)