apresent = """

|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
|                     Bar do Gallao                              |
|                                                                |
|________________________________________________________________|
|                Preço de um drink fraco:                        |
|                        R$ 15,00                                |
|                                                                |
|                                                                |
|________________________________________________________________|
|                Preço de um drink suave:                        |
|                        R$ 20,00                                |
|                                                                |
|                                                                |
|________________________________________________________________|
|                Preço de um drink forte:                        |
|                        R$ 25,00                                |
|                                                                |
|                                                                | 
|________________________________________________________________|
|Para ser considerado um drink Cuba Libre,precisa ter:           |
|Coca-Cola (50ml a 60ml) ou Pepsi-Cola (60ml a 70ml)             |
|Rum (10ml a 30ml)                                               |
|Gelo (20ml)                                                     |
|________________________________________________________________|
|          Sera cobrado R$ 30,00 caso seja feita                 |
|          uma mistura fora do padrao especificado               |
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



#menu
print(apresent)

# lista de opcao dos refrigerantes
refri_lst = ['Coca-Cola','Pepsi-Cola']

op_refri = 0
falta_cola = falta_rum = falta_gelo = False

while op_refri != 1 or op_refri != 2:
    op_refri = int(input("""
    Qual refrigerante vamos usar para fazer o drink?

    1 - Coca-Cola

    2 - Pepsi-Cola
    \n
    """))

cola = gelo = rum = -1
#inputs dos dados
while cola < 0 or cola > 100:
    cola = float(input(f'quantos ml de {refri_lst[op_refri-1]}  vai ter no drink?(entre 0 e 100ml)\n'))

while gelo < 0 or gelo > 100:
    gelo = float(input(f'quantos ml de gelo vai ter no drink?(entre 0 e 100ml)\n'))

while rum < 0 or rum > 100:
    rum = float(input(f'quantos ml de rum vai ter no drink?(entre 0 e 100ml)\n'))

#armazenando pertinencias de rum e gelo
perti_rum_forte = pertinencia_rum_forte(rum)
perti_rum_suave = pertinencia_rum_suave(rum)
perti_rum_fraco = pertinencia_rum_fraco(rum)
perti_gelo = pertinencia_gelo(gelo)



# logica de defuzzyficar caso for coca-cola
if op_refri == 1:
    
    perti_cola_forte = pertinencia_coca_forte(cola)
    perti_cola_suave = pertinencia_coca_suave(cola)
    perti_cola_fraco = pertinencia_coca_fraco(cola)

    defuzzy_suave = defuzzy([
    perti_cola_forte,perti_rum_fraco,perti_gelo],
    [perti_cola_suave,perti_rum_suave,perti_gelo],
    [perti_cola_fraco,perti_rum_forte,perti_gelo])

    defuzzy_forte = defuzzy([
    perti_cola_forte,perti_rum_suave,perti_gelo],
    [perti_cola_forte,perti_rum_forte,perti_gelo],
    [perti_cola_suave,perti_rum_forte,perti_gelo])

    defuzzy_fraco = defuzzy([
    perti_cola_fraco,perti_rum_fraco,perti_gelo],
    [perti_cola_fraco,perti_rum_suave,perti_gelo],
    [perti_cola_suave,perti_rum_fraco,perti_gelo])
    
    if not any(perti_cola_fraco,perti_cola_suave,perti_cola_forte):
        falta_cola = True

# logica de defuzzyficar caso for pepsi
else:
    
    perti_cola_forte = pertinencia_pepsi_forte(cola)
    perti_cola_suave = pertinencia_pepsi_suave(cola)
    perti_cola_fraco = pertinencia_pepsi_fraco(cola)
    
    defuzzy_suave = defuzzy([
    perti_cola_forte,perti_rum_fraco,perti_gelo],
    [perti_cola_suave,perti_rum_suave,perti_gelo],
    [perti_cola_fraco,perti_rum_forte,perti_gelo])

    defuzzy_forte = defuzzy([
    perti_cola_forte,perti_rum_suave,perti_gelo],
    [perti_cola_forte,perti_rum_forte,perti_gelo],
    [perti_cola_suave,perti_rum_forte,perti_gelo])

    defuzzy_fraco = defuzzy([
    perti_cola_fraco,perti_rum_fraco,perti_gelo],
    [perti_cola_fraco,perti_rum_suave,perti_gelo],
    [perti_cola_suave,perti_rum_fraco,perti_gelo])
    
    if not any(perti_cola_fraco,perti_cola_suave,perti_cola_forte):
        falta_cola = True
        

if not any(perti_rum_fraco, perti_rum_suave, perti_rum_forte):
    falta_rum = True
    

if perti_gelo == 0:
    falta_gelo = True   
    
print(
f"""
PERTINÊNCIAS

Pertinência de Rum Fraco {perti_rum_fraco}

Pertinência de Rum Suave {perti_rum_suave}

Pertinência de Rum Forte {perti_rum_forte}

Pertinência de Refrigerante Fraco {perti_cola_fraco}

Pertinência de Refrigerante Suave {perti_cola_fraco}

Pertinência de Refrigerante Forte {perti_cola_fraco}

Pertinência de Gelo {perti_gelo}

DEFUZZY

Defuzzy Fraco {defuzzy_fraco}

Defuzzy Suave {defuzzy_suave}

Defuzzy Forte {defuzzy_forte}


"""   
)

if any([falta_cola,falta_gelo,falta_rum]):
    print("O Drink feito nao e o Cuba Libre por que\n")
    
    if falta_cola:
        print("Refrigerante do tipo cola nao se enquadrou como fraco, suave ou forte\n")
        
    if falta_rum:
        print("Rum nao se enquadrou como fraco, suave ou forte\n")
        
    if falta_gelo:
        print("Nao tem gelo no drink\n")
    
    print("portanto o valor cobrado sera de R$ 30,00")
    
else:
    valorMaximo = max([defuzzy_forte,defuzzy_fraco,defuzzy_suave])
    
    if valorMaximo == defuzzy_fraco:
        print("O paladar determinante é fraco, deverá ser cobrado R$ 15,00.")
    
    if valorMaximo == defuzzy_suave:
        print("O paladar determinante é suave, deverá ser cobrado R$ 20,00.")
    
    if valorMaximo == defuzzy_forte:
        print("O paladar determinante é forte, deverá ser cobrado R$ 25,00")
    
    




