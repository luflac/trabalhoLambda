import json

def lambda_handler(event, context):
    nome = event.get("queryStringParameters", {}).get("nome", "usuário")
    mensagem = f"Olá, {nome}! Seja bem-vindo(a) à nossa API Lambda!"

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            "mensagem": mensagem
        }, ensure_ascii=False)  # isso garante que acentuação venha correta
    }
