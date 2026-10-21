
Carrinho = {}
valor = 0

def adicionar_item(nome, preco, quantidade=1):
    item = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    Carrinho[nome] = item

    return item


def remover_item(nome, carrinho):
    if nome in carrinho:
        del carrinho[nome]
        return True
    else: 
        return ValueError("item não encontrado")

def listar_itens(carrinho):
    return list(carrinho.values)

def calcular_frete(valor, frete):
    if valor >= 150:
        frete = 0
        return frete
    else:
        frete = 20
        return frete

def total(frete, valor):
    valor = valor + frete
    return valor
