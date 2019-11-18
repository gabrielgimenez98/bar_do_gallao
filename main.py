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
    if qtd < 56 or qtd > 60:
        return 0
    elif 58 <= qtd <=60:
        return 1
    elif 56 <= qtd <= 58:
        return (qtd-56)/(58-56)
    


def pertinencia_coca_suave(qtd):
    if qtd < 52 or qtd > 58:
        return 0

    elif 54 <= qtd <= 56:
        return 1

    elif 56 <= qtd <= 58:
        return (58-qtd)/(58-56)

    elif 52 <= qtd <= 54:
        return (qtd-52)/(54-52)

def pertinencia_coca_forte(qtd):
    if qtd < 50 or qtd > 54:
        return 0
    elif 50 <= qtd < 52:
        return 1
    elif 52 <= qtd <= 54:
        return (54-qtd)/(54-52)

def pertinencia_pepsi_fraco(qtd):
    if qtd < 66 or qtd > 70:
        return 0
    elif 68 <= qtd <= 70:
        return 1
    elif 66 <= qtd <= 68:
        return (68-qtd)/(68-66)

def pertinencia_pepsi_suave(qtd):
    if qtd < 62 or qtd > 68:
        return 0
    elif 64 <= qtd <= 66:
        return 1
    elif 62 <= qtd <= 64:
        return (qtd-62)/(64-62)
    elif 66 <= qtd <= 68:
        return (68-qtd)/(68-66)

def pertinencia_pepsi_forte(qtd):
    if qtd < 60 or qtd > 64:
        return 0
    elif 60 <= qtd <= 62:
        return 1
    elif 62 <= qtd <= 64:
        return (64-qtd)/(64-62)

def pertinencia_rum_fraco(qtd):
    if qtd < 10 or qtd > 27:
        return 0
    elif 10 <= qtd <= 15:
        return 1
    elif 15 <= qtd <= 20:
        return (20-qtd)/(20-15)

def pertinencia_rum_suave(qtd):
    if qtd < 15 or qtd > 27:
        return 0
    elif 20 <= qtd <= 25:
        return 1
    elif 15 <= qtd <= 20:
        return (qtd-15)/(20-15)
    elif 25 <= qtd <= 27:
        return (27-qtd)/(27-25)

def pertinencia_rum_forte(qtd):
    if qtd < 23 or qtd > 30:
        return 0
    elif 28 <= qtd <= 30:
        return 1
    elif 23 <= qtd <= 28:
        return (qtd-23)/(28-23)

def pertinencia_gelo(qtd):
    if qtd < 20 or qtd > 20:
        return 0
    elif qtd == 20:
        return 1


def defuzzy(lst_x,lst_y,lst_z):
    return max([min(lst_x),min(lst_y),min(lst_z)])



#menu foda
print(apresent)

# lista de opcao dos refrigerantes
refri_lst = ['Coca-Cola','Pepsi-Cola']

op_refri = 0

while op_refri != 1 or op_refri != 2:
    op_refri = int(input("""
    Qual refrigerante tu quer usar, bro?

    1 - Coca-Cola

    2 - Pepsi-Cola
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


if op_refri == 1:

    defuzzy_suave = defuzzy([
    pertinencia_coca_forte(cola),pertinencia_rum_fraco(rum),pertinencia_gelo(gelo),
    pertinencia_coca_suave(cola),pertinencia_rum_suave(rum),pertinencia_gelo(gelo),
    pertinencia_coca_fraco(cola),pertinencia_rum_forte(rum),pertinencia_gelo(gelo)])

    defuzzy_forte = defuzzy([
    pertinencia_coca_forte(cola),pertinencia_rum_suave(rum),pertinencia_gelo(gelo),
    pertinencia_coca_forte(cola),pertinencia_rum_forte(rum),pertinencia_gelo(gelo),
    pertinencia_coca_suave(cola),pertinencia_rum_forte(rum),pertinencia_gelo(gelo)])

    defuzzy_fraco = defuzzy([
    pertinencia_coca_fraco(cola),pertinencia_rum_fraco(rum),pertinencia_gelo(gelo),
    pertinencia_coca_fraco(cola),pertinencia_rum_suave(rum),pertinencia_gelo(gelo),
    pertinencia_coca_suave(cola),pertinencia_rum_fraco(rum),pertinencia_gelo(gelo)])

else:
    defuzzy_suave = defuzzy([
    pertinencia_pepsi_forte(cola),pertinencia_rum_fraco(rum),pertinencia_gelo(gelo),
    pertinencia_pepsi_suave(cola),pertinencia_rum_suave(rum),pertinencia_gelo(gelo),
    pertinencia_pepsi_fraco(cola),pertinencia_rum_forte(rum),pertinencia_gelo(gelo)])

    defuzzy_forte = defuzzy([
    pertinencia_pepsi_forte(cola),pertinencia_rum_suave(rum),pertinencia_gelo(gelo),
    pertinencia_pepsi_forte(cola),pertinencia_rum_forte(rum),pertinencia_gelo(gelo),
    pertinencia_pepsi_suave(cola),pertinencia_rum_forte(rum),pertinencia_gelo(gelo)])

    defuzzy_fraco = defuzzy([
    pertinencia_pepsi_fraco(cola),pertinencia_rum_fraco(rum),pertinencia_gelo(gelo),
    pertinencia_pepsi_fraco(cola),pertinencia_rum_suave(rum),pertinencia_gelo(gelo),
    pertinencia_pepsi_suave(cola),pertinencia_rum_fraco(rum),pertinencia_gelo(gelo)])


