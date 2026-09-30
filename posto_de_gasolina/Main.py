from Combustivel import Combustivel
from Veiculo import Veiculo
from Abastecimento import Abastecimento

# ==========================================
# COMBUSTÍVEIS
# ==========================================
etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")

# ==========================================
# VEÍCULOS
# ==========================================
carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")

# ==========================================
# ABASTECIMENTOS
# ==========================================
abastecimento1 = Abastecimento(carro,etanol,50)
abastecimento2 = Abastecimento(moto,gasolina,25)
abastecimento3 = Abastecimento(van,diesel,200)

#INSTANCIANDO NOVOS VEICULOS

carro2 = Veiculo("Carro", "AAA-1111")
carro3 = Veiculo("Carro", "BBB-2222")
moto2 = Veiculo("Moto", "CCC-3333")
moto3 = Veiculo("Moto", "DDD-4444")
van2 = Veiculo("Van", "EEE-5555")


abastecimento4 = Abastecimento(carro2,etanol,100)
abastecimento5 = Abastecimento(carro3,gasolina,55)
abastecimento6 = Abastecimento(moto2,gasolina,200)
abastecimento7 = Abastecimento(moto3,etanol,160)
abastecimento8 = Abastecimento(van2,diesel,75)


# ==========================================
# LISTA DE ABASTECIMENTOS
# ==========================================
abastecimentos = [abastecimento1, abastecimento2, abastecimento3, abastecimento4]

abastecimentos.append(abastecimento4)
abastecimentos.append(abastecimento5)
abastecimentos.append(abastecimento6)
abastecimentos.append(abastecimento7)
abastecimentos.append(abastecimento8)


# ==========================================
# MOSTRANDO OS ABASTECIMENTOS
# ==========================================
print("========== ABASTECIMENTOS DO DIA ==========")

for abastecimento in abastecimentos:
    abastecimento.mostrar_abastecimento()

# ==========================================
# TOTAL DE VENDAS POR COMBUSTÍVEL
# ==========================================
total_etanol = 0
total_gasolina = 0
total_diesel = 0

for abastecimento in abastecimentos:
    if abastecimento.combustivel.nome == "Etanol":
        total_etanol += abastecimento.valor
    elif abastecimento.combustivel.nome == "Gasolina":
        total_gasolina += abastecimento.valor
    elif abastecimento.combustivel.nome == "Diesel":
        total_diesel += abastecimento.valor

# ==========================================
# TOTAL DO DIA
# ==========================================
total_dia = (total_etanol + total_gasolina + total_diesel)




#=================arrumando seu codigo >:P=============================

with open("recibo.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("========== POSTO DE GASOLINA ==========\n\n")

    for abastecimento in abastecimentos:
        arquivo.write(f"{str(abastecimento.veiculo)}\n"
                      f"Combustível: {str(abastecimento.combustivel.nome)}\n"
                      f"Valor:{str(abastecimento.valor)}\n\n")
    arquivo.write("========================================\n\n")
    for abastecimento in abastecimentos:
        if abastecimento.combustivel.nome == "Etanol":
            arquivo.write(f"Etanol: {str(total_etanol)}\n")
        elif abastecimento.combustivel.nome == "Gasolina":
            arquivo.write(f"Gasolina: {str(total_gasolina)}\n")
        elif abastecimento.combustivel.nome == "Diesel":
            arquivo.write(f"Diesel: {str(total_diesel)}\n")

    arquivo.write(f"TOTAL DO DIA: {total_dia}")





with open("recibo.txt", "a", encoding='utf-8'):
    for abastecimento in abastecimentos:
        arquivo.write(f"{str(abastecimento.veiculo)}\n"
                      f"Combustível: {str(abastecimento.combustivel.nome)}\n"
                      f"Valor:{str(abastecimento.valor)}\n\n")
    arquivo.write("========================================\n\n")
    for abastecimento in abastecimentos:
        if abastecimento.combustivel.nome == "Etanol":
            arquivo.write(f"Etanol: {str(total_etanol)}\n")
        elif abastecimento.combustivel.nome == "Gasolina":
            arquivo.write(f"Gasolina: {str(total_gasolina)}\n")
        elif abastecimento.combustivel.nome == "Diesel":
            arquivo.write(f"Diesel: {str(total_diesel)}\n")

    arquivo.write(f"TOTAL DO DIA: {total_dia}")