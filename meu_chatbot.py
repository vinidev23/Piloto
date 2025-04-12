import openai
from dotenv import load_dotenv
import os

# Carrega o arquivo .env
load_dotenv()

# Define sua chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Verifica se a chave foi carregada corretamente
if not openai.api_key:
    print("Erro: A chave da API não foi encontrada ou está inválida.")
    exit()

# Loop para interação com o usuário
while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Chat encerrado")
        break

    try:
        resposta = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Modelo que será usado
            messages=[
                {"role": "user", "content": pergunta}  # Adiciona a mensagem do usuário
            ]
        )

        # Exibe a resposta do modelo
        print("ChatGPT:", resposta['choices'][0]['message']['content'])

    except Exception as e:
        print("Ocorreu um erro:", e)
