massa = float(input("Digite a massa da peça de madeira em QUILOGRAMAS: "))
largura = float(input("Digite a largura da peça de madeira em CENTÍMETROS: "))
altura = float(input("Digite a altura da peça de madeira em CENTÍMETROS: "))
profundidade = float(input("Digite a profundidade(comprimento) da peça de madeira em CENTÍMETROS: "))

volume = (largura/100) * (altura/100) * (profundidade/100)
densidadeMadeira = (massa / volume)


if densidadeMadeira < 450:
    print("Baixa densidade!", densidadeMadeira, "kg/m3")
elif 450 <= densidadeMadeira <= 750:
    print("Média densidade!", densidadeMadeira, "kg/m3")
elif densidadeMadeira > 750:
    print("Alta densidade!", densidadeMadeira, "kg/m3")
