import os

# Caminho onde as pastas serão criadas
caminho = r"Q:\TI\Notas Fiscais - Fornecedores\Neocode\2024"

# Lista com os nomes dos meses
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Junho", "Agosto", "Setembro", "Outubro",
         "Novembro", "Dezembro"]

# Loop para criar as pastas
for i, mes in enumerate(meses):
    nome_pasta = os.path.join(caminho, f"{i + 1} - {mes}")  # Caminho completo da pasta
    os.makedirs(nome_pasta)  # Cria a pasta
    print(f"Pasta '{nome_pasta}' criada.")
