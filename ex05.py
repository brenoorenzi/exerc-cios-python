# 5. O cardápio de uma lanchonete é o seguinte:
# Especificação      Código  Preço
# Cachorro Quente    100     R$ 1,20
# Bauru Simples      101     R$ 1,30
# Bauru com ovo      102     R$ 1,50
# Hambúrguer         103     R$ 1,20
# Cheeseburguer      104     R$ 1,30
# Refrigerante       105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

def lanchonete_pedido():

    cardapio = {
        100: {"pedidos": "Cachorro Quente", "preco": 1.20},
        101: {"pedidos": "Bauru Simples", "preco": 1.30},
        102: {"pedidos": "Bauru com ovo", "preco": 1.50},
        103: {"pedidos": "Hambúrguer", "preco": 1.20},
        104: {"pedidos": "Cheeseburguer", "preco": 1.30},
        105: {"pedidos": "Refrigerante", "preco": 1.00}
    }
    
    pedido_total = 0
    print("Cardápio da Lanchonete")
    for codigo, info in cardapio.items():
        print(f"{codigo} - {info['pedidos']}: R$ {info['preco']:.2f}")
    print("Para encerrar o pedido, digite 'fim' no código do item.")
    
    while True:
        try:

            codigo_input = input("Digite o código do item: ").lower()
            if codigo_input == 'fim':
                break
            
            codigo = int(codigo_input)
            if codigo not in cardapio:
                print("Código de item inválido.")
                continue

            quantidade = int(input(f"Digite quantos itens deseja de '{cardapio[codigo]['pedidos']}': "))
            if quantidade <= 0:
                print("A quantidade deve ser um número positivo.")
                continue

           
            valor_item = cardapio[codigo]["preco"] * quantidade
            pedido_total += valor_item
            
            print(f"Subtotal para {quantidade}x {cardapio[codigo]['pedidos']}: R$ {valor_item:.2f}")

        except ValueError:
            print("Este pedido não existe. digite um codigo valido")

    print(" Pedido Finalizado")
    print(f"Valor total a ser pago: R$ {pedido_total:.2f}") 


lanchonete_pedido()
