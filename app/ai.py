import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"

def gerar_resposta(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openrouter/cinematica",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return "Erro ao conectar com a IA."
