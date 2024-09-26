import urllib.request
import ssl

url = "http://www.pudim.com.br"

# Cria um contexto SSL que ignora a verificação de certificado
context = ssl._create_unverified_context()

try:
    response = urllib.request.urlopen(url, context=context)
except urllib.error.URLError as e:
    print(f"Erro ao tentar acessar o site Pudim: {e.reason}")
    print(f"O site Pudim retornou o código de status {response.status}.")
else:
    print("O site Pudim está acessível!")
