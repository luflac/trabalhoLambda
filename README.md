# 🟧 AWS Lambda - Mensagem Personalizada

Este projeto contém uma função Lambda escrita em **Python**, que retorna uma saudação personalizada com base no parâmetro `nome` recebido pela URL. A função está integrada ao **API Gateway**, tornando-a acessível via requisição HTTP pública.

---

## 📌 Objetivo

Demonstrar o uso de AWS Lambda em conjunto com API Gateway para retornar uma mensagem customizada com base em parâmetros de entrada, utilizando boas práticas de documentação e versionamento via GitHub.

---


## ▶️ Como executar

1. Acesse o endpoint da API com um nome via query string e substitua "SeuNome" pelo seu nome!
   
https://ky4lo2f9m3.execute-api.us-east-2.amazonaws.com/prod/mensagem?nome=SeuNome

2. O resultado será um JSON com a saudação personalizada.

3. Pode ser testado via navegador, curl, Postman ou integrado a outra aplicação.



### 📤 Saída esperada

```json
{
  "mensagem": "Olá, "SeuNome"! Seja bem-vindo(a) à nossa API Lambda!"
}
```

---

## 🐞 Como depurar a função

- Acesse a aba **Monitoramento** na função Lambda  
- Clique em **Ver logs no CloudWatch**  
- Veja o conteúdo do `event` e eventuais erros  
- Você pode adicionar `print(event)` no código para inspecionar os dados de entrada
