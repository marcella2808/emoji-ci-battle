from batalha import heroi_vs_vilao

def test_heroi_ganha():
    vitorias = [heroi_vs_vilao() for _ in range(5)]
    assert "heroi" in vitorias, "Nenhum herói venceu! O build está corrompido!"
