# Lista de notas dos estudantes

notas = [7.5, 8.0, 6.5, 9.0, 7.0]

 

# Função regular para calcular a média

def calcular_media(notas):

    total = sum(notas)

    media = total / len(notas)

    return media

 

# Função lambda para arredondar a média para duas casas decimais

arredondar_media = lambda media: round(media, 2)

 

# Calcular a média

media = calcular_media(notas)

media_arredondada = arredondar_media(media)

 

# Verificar se os estudantes foram aprovados

situacao = if media_arredondada >= 7 else

 

# Resultados

print("Notas dos estudantes", notas)

print("Media das notas", media_arredondada)

print("Situação do estudante", situacao)