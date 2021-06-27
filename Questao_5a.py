#Aplicação para apresentar o pib do paises presentes na tabela interna do sistema em um periodo de anos

#Função que extrai os dados do arquivo externo
def extrair_dados(caminho_arquivo):
    arquivo = open(caminho_arquivo, 'r', encoding='utf8')

    conteudo = arquivo.read()

    arquivo.close()
    conteudo = conteudo.splitlines()
    rotulos = conteudo[0]
    rotulos = rotulos.split(',')
    conteudo = conteudo[1:]
    dados = []
    for elemento in conteudo:
        elemento = elemento.split(',')
        dados.append(elemento)
    return rotulos, dados

#Função que trata dos dados retirados do arquivo csv da tabela externa
def solicitar_PIB(ano, país):
    rotulos, dados = extrair_dados('Planilha.csv')
    indice_2013 = rotulos.index('2013')
    indice_2014 = rotulos.index('2014')
    indice_2015 = rotulos.index('2015')
    indice_2016 = rotulos.index('2016')
    indice_2017 = rotulos.index('2017')
    indice_2018 = rotulos.index('2018')
    indice_2019 = rotulos.index('2019')
    indice_2020 = rotulos.index('2020')
    indice_pais = rotulos.index('País')
    for elemento in dados:
        if elemento[indice_pais] == país and ano == 2020:
            print(elemento[indice_2020])
        elif elemento[indice_pais] == país and ano == 2019:
            print(elemento[indice_2019])
        elif elemento[indice_pais] == país and ano == 2018:
            print(elemento[indice_2018])
        elif elemento[indice_pais] == país and ano == 2017:
            print(elemento[indice_2017])
        elif elemento[indice_pais] == país and ano == 2016:
            print(elemento[indice_2016])
        elif elemento[indice_pais] == país and ano == 2015:
            print(elemento[indice_2015])
        elif elemento[indice_pais] == país and ano == 2014:
            print(elemento[indice_2014])
        elif elemento[indice_pais] == país and ano == 2013:
            print(elemento[indice_2013])

#Entrada do ano desejado
ano = int(input("Digite um ano entre 2013 e 2020: "))

#Verificação do ano
if ano<2013 or ano>2020:
    print("Ano inválido!")
    exit()

#Entrada do pais desejado
país = str(input("Digite um país:"))

solicitar_PIB(ano, país)



#Onde a função que trata os dados vindos da tabela e imprime o pib condizente