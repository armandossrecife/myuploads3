# Passos para criar uma aplicação de upload e listagem de imagens usando um bucket do S3

## 1. Criando um bucket no S3, com as propriedades padrões, para armazenar imagens

Nome do bucket: my-app-image-bucket

## 2. Desabilite a opção "Bloquear Acesso Público"

## 3. Para liberar a leitura dos objetos desse bucket é preciso criar uma política

Selecione o bucket "my-app-image-bucket" -> Selecione a aba "Permissões" -> Crie um JSON com o seguinte conteúdo:

```bash
{
  "Id": "Policy1712415077164",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1712415054743",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::my-app-image-bucket/*",
      "Principal": "*"
    }
  ]
}
```

Observação: 

Segue um link para ajudar a criar políticas mais sofisticadas: 
https://awspolicygen.s3.amazonaws.com/policygen.html

## 4. Crie uma políca de acesso para permitir a interação de uma aplicação EC2 com os serviços S3 e RDS 

nome: my_app_user

acesso completo ao EC2, S3, RDS

## 5. Crie um usuário de aplicação para permitir a autenticação da aplicação com os serviços que serão usados. 

- Criar um usuário (user_app) de aplicação

Associar este usuário a política de acesso da aplicação criada no item 4. 

## 6. Na propriedade de chave de acesso do usuário criado (item 5), é preciso criar uma nova chave de acesso 
tipo: outros

Dados da chave de acesso gerada:

Chave de acesso: ?

Chave de acesso secreta: ?

Também foi baixado o arquivo.csv contendo as informações da chave de acesso

Estas informações deverão ser carregadas dinâmicamente no código via arquivo de configuração (fora do repositório do código) ou informações salvas como variáveis de ambiente do sistema operacional da instância que vai executar a aplicação.

Observação: nunca salve estas informações no repositório de código. Guarde estas informações em uma pasta local segura. 