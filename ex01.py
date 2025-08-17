 #1. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Alcool:
#• até 20 litros: desconto de 3% por litro
#• acima de 20 litros: desconto de 5% por litro
#Gasolina:
#• até 20 litros: desconto de 4% por litro
#da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
#sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def calcular_valor_pagar():
    preco_gasolina = 2.50
    preco_alcool = 1.90
    
    tipo_combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ").upper()
    litros = float(input("Digite a quantidade de litros: "))
    
    valor_total_bruto = 0
    valor_desconto = 0
    
    if tipo_combustivel == "A":
        valor_total_bruto = litros * preco_alcool
        if litros <= 20:
            desconto_percentual = 0.03
        else:
            desconto_percentual = 0.05
        
        valor_desconto = valor_total_bruto * desconto_percentual
    
    elif tipo_combustivel == "G":
        valor_total_bruto = litros * preco_gasolina
        if litros <= 20:
            desconto_percentual = 0.04
        else:
            desconto_percentual = 0.06
        
        valor_desconto = valor_total_bruto * desconto_percentual
        
    else:
        print("Tipo de combustível inválido. Por favor, digite 'A' ou 'G'.")
        return

    valor_a_pagar = valor_total_bruto - valor_desconto
    
    print("-" * 30)
    print("Detalhes da compra:")
    print(f"Tipo de combustível: {'Álcool' if tipo_combustivel == 'A' else 'Gasolina'}")
    print(f"Quantidade de litros: {litros:.2f} L")
    print(f"Valor total bruto: R$ {valor_total_bruto:.2f}")
    print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")
    print("-" * 30)

calcular_valor_pagar()
