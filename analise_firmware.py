# Análise de firmware de câmera IP
# Este script orienta o uso do binwalk para extrair e analisar o firmware

import os

# Caminho para o arquivo de firmware baixado
firmware_path = "CAMINHO_PARA_O_FIRMWARE.BIN"

print("Instruções para análise de firmware:")
print("1. Instale o binwalk: pip install binwalk (ou use o instalador do site oficial)")
print(f"2. Extraia o firmware com: binwalk -e '{firmware_path}'")
print("3. Analise os arquivos extraídos em busca de senhas, scripts suspeitos ou backdoors.")
print("4. Procure por arquivos como /etc/passwd, /etc/shadow, scripts .sh e binários customizados.")

# Opcional: Executar binwalk automaticamente (requer binwalk instalado no sistema)
if os.path.exists(firmware_path):
    os.system(f"binwalk -e '{firmware_path}'")
else:
    print("Arquivo de firmware não encontrado. Atualize o caminho e tente novamente.")
