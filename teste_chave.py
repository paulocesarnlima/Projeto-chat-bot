import os

# Recupere o valor da variável de ambiente
ChaveOpenai = os.getenv("OpenaiKey")

# Verifique se a variável de ambiente foi definida
if ChaveOpenai is not None:
    print(f"O valor da variável de ambiente OpenaiKey é: {ChaveOpenai}")
else:
    print("A variável de ambiente OpenaiKey não está definida.")
    
 

for var, valor in os.environ.items():
    print(f"{var}: {valor}")