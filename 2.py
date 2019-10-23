def informaCategoria(idade):
    idade=int(idade)
	if idade in range(0,2):
		categoria = 'Bebê'
	elif idade in range(2,13):
		categoria = 'Criança'
	elif idade in range(13,20):
		categoria = 'Adolescente'
	elif idade in range(20,61):
		categoria = 'Adulto'
	elif idade in range(61,80):
		categoria = 'Adulto'
	elif idade >= 80:
		categoria = 'Longevo'
	else:
		categoria = 'Idade inválida!'
	return categoria
