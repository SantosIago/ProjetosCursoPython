v = float(input('Quantos metros: '))
cm = v * 100
mm = v * 1000
km = v * 0.001
hm = v * 0.01
dam = v * 0.1
dm = v * 10

print('Valor {} metros em centimetro: {}cm.'.format(v, cm))
print('Valor {} metros em milimetro: {}mm.'.format(v, mm))
print('Valor {} metros em quilômetro: {}km.'.format(v, km))
print('Valor {} metros em Hectômetro: {}hm.'.format(v, hm))
print('Valor {} metros em Decâmetro: {}dam.'.format(v, dam))
print('Valor {} em decimetro: {}dm.'.format(v, dm))
