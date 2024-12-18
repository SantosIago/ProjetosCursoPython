preço = float(input('O preço do produto é de: R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
