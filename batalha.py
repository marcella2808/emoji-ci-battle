import random

def heroi_vs_vilao():
    heroi = random.randint(50, 100)
    vilao = random.randint(50, 100)
    vencedor = "heroi" if heroi >= vilao else "vilao"
    print(f"💥 Herói: {heroi} 🆚 Vilão: {vilao} 👉 Vencedor: {vencedor}")
    return vencedor
