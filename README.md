# Twitter Bot

## Funcionalidades
Foi criado uma nova conta no Twitter para este bot. 
Ele verifica se alguém o mencionou em alguma postagem e comenta com uma imagem aleatória do seu storage.

Para evitar que a o mesmo tweet seja respondido mais de uma vez, o script salva em um banco de dados SQLite os ids dos tweets respondidos.

## Informações
- Todas as images estão armazenadas em um storage da [AWS](https://aws.amazon.com/pt/) S3.

## Instalação

- Crie o arquivo .env baseado no arquivo .env.example

- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
    ```
    virtualenv venv
    Linux: source venv/bin/activate
    Windows: virtualenv\virtual_1\Scripts\activate
    ```
    
- Requirements
    ```
    pip install -r requirements.txt
    ```
 
 ## Twitter dev
 Para executar o script é necessário adiquirir os tokens de acesso a sua conta do Twitter
 - Acesse a área de [apps](https://developer.twitter.com/en/apps)
 - Crie um novo App e siga os passoa para adquirir as credenciais
 - Adicione suas credenciais ao arquivo .env
 
 ## [AWS S3](https://s3.console.aws.amazon.com/s3/home)
 - Crie um nov brucket e crie uma pasta chamada **images** dentro dela. Lá deverá ter todas as imagens no formato **jpeg, jpg ou png**.
 - Crie um novo usuário na parte de acessos da AWS [IAM](https://console.aws.amazon.com/iam).
 - Insira os tokens de acesso ao arquivo .env e o nome do brucket criado.


### Execute
    python run.py
  Este script pode ser programado para rodar a cada x seg/min no servidor.