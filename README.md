# SSH Brute & Auditoria de Câmeras IP

Este projeto reúne scripts para auditoria, automação de força bruta de credenciais e busca de vulnerabilidades em câmeras IP, especialmente modelos white-label chineses.

## Funcionalidades

- **brute.py**: Tenta acessar a câmera via SSH usando uma lista de credenciais padrão conhecidas.
- **busca_exploits.py**: Automatiza a busca por exploits públicos para o modelo/chipset da câmera, com opção de detecção automática ou manual.
- **analise_firmware.py**: Orienta e automatiza a análise de firmware da câmera para encontrar backdoors, senhas hardcoded e vulnerabilidades.
- **config_camera.py**: Centraliza as informações de IP e porta da câmera para uso compartilhado entre os scripts.

## Como usar

1. Clone ou baixe este repositório.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Edite o arquivo `config_camera.py` com o IP e porta da sua câmera.
4. Execute os scripts conforme a necessidade:
   - `brute.py` para força bruta de credenciais SSH.
   - `busca_exploits.py` para busca de vulnerabilidades públicas.
   - `analise_firmware.py` para análise de firmware (requer binwalk instalado).

## Observações
- Use apenas em equipamentos de sua propriedade.
- O script `busca_exploits.py` pode tentar detectar automaticamente o modelo/chipset da câmera via HTTP/SSH.
- O módulo `re` não precisa ser instalado, pois faz parte da biblioteca padrão do Python.

## Dependências
- paramiko
- requests

## Segurança
Esses scripts são para fins de auditoria e aprendizado. Não utilize em dispositivos de terceiros sem autorização.
