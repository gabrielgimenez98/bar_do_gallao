apresent = """

|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
|                                                                |
|                     Bar do Gallao                              | 
|                                                                |
|________________________________________________________________|
|                Para fazer um drink fraco:                      |
|                                                                |
|                                                                |
|                                                                |
|________________________________________________________________|
|                Para fazer um drink suave:                      |
|                                                                |
|                                                                |
|                                                                |
|________________________________________________________________|
|                Para fazer um drink forte:                      |
|                                                                |
|                                                                |
|                                                                | 
|________________________________________________________________|
|                Para fazer um drink fraco:                      |
|                                                                |
|                                                                |
|                                                                |
|________________________________________________________________|
|                Para fazer um drink fraco:                      |
|                                                                |
|                                                                |
|                                                                |
|________________________________________________________________|
|                                                                |
|                                                                |
|                                                                |
|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|


"""

#funcoes para calcular pertinencia
def pertinencia_coca_fraco(qtd):
    pass

def pertinencia_coca_suave(qtd):
    pass

def pertinencia_coca_forte(qtd):
    pass

def pertinencia_pepsi_fraco(qtd):
    pass

def pertinencia_pepsi_suave(qtd):
    pass

def pertinencia_pepsi_forte(qtd):
    pass

def pertinencia_rum_fraco(qtd):
    pass

def pertinencia_rum_suave(qtd):
    pass

def pertinencia_rum_forte(qtd):
    pass

def pertinencia_gelo(qtd):
    pass


#menu foda
print(apresent)

# lista de opcao dos refrigerantes
refri_lst = ['Coca-Cola','Pepsi-Cola','outro']

op_refri = int(input("""
Qual refrigerante tu quer usar, bro?

1 - Coca-Cola

2 - Pepsi-Cola

3 - Outro
\n
"""))

cola = gelo = rum = -1
#inputs dos dados
while cola < 0 or cola > 100:
    cola = float(input(f'quantos ml de {refri_lst[op_refri-1]} vai ter no drink?\n'))

while gelo < 0 or gelo > 100:
    gelo = float(input(f'quantos ml de gelo vai ter no drink?\n'))

while rum < 0 or rum > 100:
    rum = float(input(f'quantos ml de rum vai ter no drink?\n'))