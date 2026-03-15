#Entrada dos dados de registro 💻
Marca=input("Qual a Marca do eletrodomestico: ")
Tipo=input("Qual o tipo de eletrodomestico (geladeira,fogão): ")

#Entrada dos dados de calculo 👇
Potencia=float(input("Qual a Potencia do aparelho em watts: "))
Tempo=float(input("Qual o Tempo médio de consumo em horas: "))
Custo=float(input("Qual o Valor tarifa do estado (Sp = 0.259 R$/KWh): "))

#Processamento dos dados 🔗‍️
ConsumoMensal=(Potencia*Tempo*30)/1000
Valorgasto=(ConsumoMensal*Custo)

#Resultado com informações⚡💡💲
print(f"Considerando os calculos obtidos para a marca {Marca} do tipo {Tipo}."
      f"É correto afirmar que o consumo médio de consumo estimado de {ConsumoMensal} Kwh/mês."
      f"Para o consumo calculado deve-se gastar em média {Valorgasto} R$/Kwh."
    )