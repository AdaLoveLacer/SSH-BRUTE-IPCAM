
import paramiko

# Configurações
host = "IP_DA_CAMERA"  # Substitua pelo IP da sua câmera
port = 22

# Lista de usuários e senhas comuns para câmeras white-label chinesas
credentials = [
    ("admin", "admin"),
    ("admin", "12345"),
    ("admin", "123456"),
    ("admin", ""),
    ("root", "root"),
    ("root", "12345"),
    ("root", "123456"),
    ("root", ""),
    ("user", "user"),
    ("user", "12345"),
    ("user", "123456"),
    ("user", ""),
    ("guest", "guest"),
    ("guest", "12345"),
    ("guest", ""),
]

def try_ssh_login(host, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=username, password=password, timeout=5)
        client.close()
        return True
    except Exception:
        return False

for username, password in credentials:
    print(f"Tentando {username}:{password!r}...")
    if try_ssh_login(host, port, username, password):
        print(f"SUCESSO! Credencial encontrada: {username}:{password!r}")
        break
else:
    print("Nenhuma credencial funcionou.")
