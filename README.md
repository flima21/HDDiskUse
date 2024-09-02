# Monitoramento de Capacidade de HD

Este projeto é um script desenvolvido em **Python** com o objetivo de monitorar a capacidade do HD de um sistema e alertar os usuários por e-mail quando a utilização exceder um limite determinado em **N%**.

## Requisitos

Para que o script funcione corretamente, é necessário configurar um arquivo `.env` na raiz do projeto com as seguintes variáveis:

- `HOST_EMAIL`: Endereço do servidor SMTP (e.g., `smtp.gmail.com`).
- `PORT_EMAIL`: Porta do servidor SMTP (e.g., `587`).
- `USER_EMAIL`: Endereço de e-mail que será usado para enviar as notificações.
- `PSWD_EMAIL`: Senha ou token de acesso do e-mail utilizado para envio.
- `PERCENTAGE_HD`: A porcentagem a ser definida

## Instruções de Uso

1. Clone este repositório para seu ambiente local.
2. Crie um arquivo `.env` na raiz do projeto e configure as variáveis conforme descrito acima.
3. Certifique-se de que todas as dependências do Python estejam instaladas. Utilize o comando abaixo para instalar as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o script como usuário **root** para garantir que todas as permissões necessárias sejam concedidas:

    ```bash
    sudo python3 src/monitoramento_hd.py
    ```

## Observações

- Este script deve ser executado com permissões de administrador para ter acesso total às informações de uso do disco.
- Certifique-se de que o servidor de e-mail e as credenciais fornecidas no arquivo `.env` estejam corretos para evitar falhas no envio das notificações.
- O projeto é compatível com Python 3.x.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

**Aviso:** Use este script por sua conta e risco. O autor não se responsabiliza por qualquer dano ou perda de dados.
