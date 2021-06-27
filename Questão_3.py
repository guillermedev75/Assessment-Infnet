#Aplicação para auxiliar no entendendimento dos gastos de moradia, transporte, e educação em relação a renda mensal do individuo.

#Função que tem como objetivo calcular todas as metricas e diagnosticar os gastos.
def diagnostico_gastos(renda_mensal,gasto_moradia,gasto_educacao,gasto_transporte):

    #Calculos necessarios para o diagnostico.
    porcentagem_moradia = (gasto_moradia * 100)/renda_mensal
    gasto_moradia = (30*renda_mensal)/100
    porcentagem_educacao = (gasto_educacao * 100)/renda_mensal
    gasto_educacao = (20*renda_mensal)/100
    porcentagem_transporte = (gasto_transporte * 100)/renda_mensal
    gasto_transporte = (15*renda_mensal)/100

    #Verificação de disgnostico junto a impressão dos dados de diagnostico.
    print("\nDiagnóstico:")
    if porcentagem_moradia <= 30 and porcentagem_educacao <= 20 and porcentagem_transporte <= 15:
        print("\nSeus gastos estão dentro da margem recomendada.")
    if porcentagem_moradia > 30:
        print(f"\nSeus gastos totais com moradia comprometem {porcentagem_moradia}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gasto_moradia}.")
    if porcentagem_moradia <= 30:
        print(f"\nSeus gastos totais com moradia comprometem {porcentagem_moradia}% de sua renda total. O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.")
    if porcentagem_educacao > 20:
        print(f"Seus gastos totais com educação comprometem {porcentagem_educacao}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gasto_educacao}.")
    if porcentagem_educacao <= 20:
        print(f"Seus gastos totais com educação comprometem {porcentagem_educacao}% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.")
    if porcentagem_transporte > 15:
        print(f"Seus gastos totais com transporte comprometem {porcentagem_transporte}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gasto_transporte}.\n")
    if porcentagem_transporte <= 15:
        print(f"Seus gastos totais com transporte comprometem {porcentagem_transporte}% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.\n")

#Entrada dos valores do individuo para que sejam tratados na função.
renda_mensal = float(input("Renda mensal total: "))
gasto_moradia = float(input("Gastos totais com moradia: "))
gasto_educacao = float(input("Gastos totais com educação: "))
gasto_transporte = float(input("Gastos totais com transporte: "))

#Chamada da função que já inclue a impressão do resultado do diagnostico.
diagnostico_gastos(renda_mensal,gasto_moradia,gasto_educacao,gasto_transporte)