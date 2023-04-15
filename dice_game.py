import random

def joga_dados():
	soma_dados = random.randint(1,6) + random.randint(1,6)
	return soma_dados

def main():
	jogador1= input('Digite o nome do jogador 1:\n')
	jogador2= input('Digite o nome do jogador 2:\n')

	jogada1 = joga_dados()
	jogada2 = joga_dados()

	if jogada1 > jogada2:
		print('O {}, com {} pontos, venceu! o {} que teve {} pontos.'.format(jogador1,jogada1, jogador2, jogada2))
	elif jogada2 > jogada1:
		print('O {}, com {} pontos, venceu! o {} que teve {} pontos.'.format(jogador2,jogada2, jogador1, jogada1))
	else:
		print('O {}, teve {} pontos, e o {} que teve {} pontos. Empate!!!!'.format(jogador1,jogada1, jogador2, jogada2))

main()