### Como usar a API

1. instale o arquivo requirements para instalar as bibliotecas necessarias python
2. O codigo foi escrito em python usando framework flask
3. é necessario que se tenha instalado algum software para testar as rotas(particularmente recomendo o insomnia)
4. para fazer os calculos e gravar no banco de dados firebase os dados use a rota /calculate usando o metodo post

![resposta da API rota Calculate](https://i.imgur.com/3dTmttZ.png)
- essa é a forma que se deve encaminhar os dados para a api na rota calculate
`{
 "sold_at": "30/09/2021",
 "document": "48061017881",
 "total": 300,
 "name": "joseph",
 "type_cashback": "A",
 "value": 150,
 "qty": 2
}`