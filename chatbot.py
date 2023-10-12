# Data Science Academy - www.datascienceacademy.com.br
# Projecto 3 - construirndo um chatbot personalizado com GPT-4 e Linguagem Python

# Import
import openai

# Chave
openai.api_key = "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"

# Função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):

    #Obtém a resposta do modelo da linguagem
    response = openai.Completion.create(

        # Modelo usado
        # Outros modelos estão disponíveis em https://platform.openai.com/account/rate-limits
        engine = "text-davinci-003",

        # Texto inicial da conversa com o chatbot.
        prompt = texto,

        # Comprimento da resposta gerada pelo modelo
        max_tokens = 150,

        # Quantas conclusões gerar para cada prompt.
        n = 5,

        # O texto retornado não conterá a sequência de parada.
        stop = None,

        # Uma medida da aleatoridade de um texto gerado pelo modelo. Seu valor está entre 0 e 1.
        # Valores próximos a 1 significam que a saida é mais aleatória, enquanto valores próximos a 0 significam que a saida é muito identificável.
        temperature = 0.8,

    )
    return response.choices[0].text.strip()

# Função principal do programa python
def main():

    print("\n Bem-vindo ao GPT-4 Chatbot do Projecto 3 do curso Gratuito da Data Science Academy!")
    print("www.datascienceacademy.com.br")
    print("(Digite 'Sair' a qualquer momento para encerrar o chat)")

    # Loop
    while True:

        # Coleta a pergunta digitada pelo usuário
        user_message = input("\nVocê: ")

        # Se a mensagem for "Sair" finaliza o programa
        if user_message.lower() == "sair":
            break
        # Coloca a mensagem digitada pelo usuário na variável python chamada gpt4_prompt.
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"

        # Obtém a resposta do modelo executando a função gera_texto().
        chatbot_response = gera_texto(gpt4_prompt)

        # Imprime a resposta do chatbot.
        print(f"\nChatbot: {chatbot_response}")

# Execução do programa (bloco main) em python
if __name__ == "__main__":
    main()