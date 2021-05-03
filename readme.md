# devops_challenge

A API foi criada através da Django Rest Framework e possui 3 rotas, uma para os códigos de barras, outra para os atributos e outra para as informações restantes dos produtos. Esta framework foi escolhida por conter facilidades de interface para o teste da API.

```json
{
    "products": "http://127.0.0.1:8000/api/products/",
    "barcodes": "http://127.0.0.1:8000/api/barcodes/",
    "attributes": "http://127.0.0.1:8000/api/attributes/"
}
```

Um dos problemas encontrados foi a dificuldade para retornar um json completo dos produtos, incluindo os códigos de barra e os atributos aninhados. Devido ao tempo e à dificuldade como esta parte funciona, decidi trabalhar com os 3 modelos em separado.

### O método GET:

```bash
GET /api/barcodes/
GET /api/attributes/
GET /api/products/
```

O produto de id 81 pode ter as informações retornadas da seguinte forma:

Exemplo: [http://127.0.0.1:8000/api/products/81/](http://127.0.0.1:8000/api/products/81/)

O id é chave primária, e por isso este retorno é possível. Para consultar códigos de barra e atributos a melhor forma é através de filtros, que será falado mais a frente.

Para os 3 casos foi implementado modelos de paginação, busca e ordenação.

Paginação:

Exemplo: "[http://127.0.0.1:8000/api/products/?page=2](http://127.0.0.1:8000/api/products/?page=2)"

O parâmetro page recebe o número do index, ou seja, da página que será retornada. A quantidade de itens retornados sempre será de no máximo 10. Este valor foi escolhido de acordo com com a quantidade de produtos cadastrado, 50 produtos cadastrados por script.

Filtros:

Exemplos: "[http://127.0.0.1:8000/api/products/?search=Glitter](http://127.0.0.1:8000/api/products/?search=Glitter)", "[http://127.0.0.1:8000/api/barcodes/?search=0679037742087](http://127.0.0.1:8000/api/barcodes/?search=0679037742087)",

"[http://127.0.0.1:8000/api/attributes/?search=culpa](http://127.0.0.1:8000/api/attributes/?search=culpa)"

O parâmetro search recebe a string que será buscada. Não é possível filtrar por mais de um parâmetro de uma vez só, por exemplo, listar todos os produtos com nome de glitter ou milho.

Os parâmetros que podem ser utilizados nos filtros são:

- Product: title, sku
- ProductBarcode: barcode
- ProductAttribute: name

Ordenação:

Exemplo: "[http://127.0.0.1:8000/api/barcodes/?ordering=product_id](http://127.0.0.1:8000/api/barcodes/?ordering=product_id)"

Este parâmetro ordena, por ordem crescente ou decrescente, de acordo com a propriedade dada.

- Product: title, product_id
- ProductBarcode: barcode, product_id
- ProductAttribute: name, product_id

### Os métodos POST e PUT:

O formato JSON esperado é o seguinte:

{
"title": "",
"sku": "",
"description": "",
"price": null,
"created": null,
"last_updated": null
}

As datas são de preenchimento opcional, porém são geradas pela própria API caso deixadas em branco.

### O método DELETE:

 O delete pode ser feito passando o id de um produto e neste caso deletando o produto e todos seus atributos e códigos de barra.

Da mesma forma um código de barra ou um atributo pode ser deletado através do seu id único, mas sem afetar as outras propriedades do produto.

### Script com dummy data:

O script script_populate.py quando executado insere 50 produtos com todos os dados no nosso banco de dados. Ele utiliza a biblioteca Fake para gerar textos, nomes, valores... A quantidade de produtos inseridos pode ser facilmente alterada com o parâmetro passado na chamada da função na última linha.

### Validações:

- Propriedades únicas: Product(sku), Product(product_id)
- Duplas únicas:
    - ProductBarcode([product_id, barcode]) → não é possível cadastrar o mesmo código de barra mais de uma vez no mesmo produto.
    - ProductAttribute([product_id, name]) → não é possível cadastrar mais de uma propriedade com o mesmo nome para um produto.
- Máximo de caracteres definido:
    - Product(title, max=32), Product(sku, max=32), Product(description, max=1024)
    - ProductBarcode(barcode, max=32)
    - ProductAttribute(name, max=16), ProductAttribute(value, max=16)
- Null não permitido:
    - Product(title), Product(sku), Price(sku), ProductBarcode(barcode), ProductAttribute(name), ProductAttribute(value)
- Apenas números reais:
    - Product(price)
- Validações especiais:
    - ProductBarcode(barcode) pode receber apenas caracteres numéricos
    - Product(sku) pode receber apenas caracteres alfanuméricos.

Exemplo de retorno ao tentar cadastrar um produto com preço com letras:

```json
{
    "price": [
        "Um número válido é necessário."
    ]
}
```

### Testes e deploy:

Foram feitos testes manuais através da própria interface do Django, acessando o endereço http://localhost/api/. Além disso foram feitos testes utilizando Postman. Caso queira testar, a aplicação está disponível no endereço: [https://lh-devops-challenge.herokuapp.com/api/](https://lh-devops-challenge.herokuapp.com/api/)

Testes automáticos foram feitos utilizando os recursos de testes do Django. Eles se encontram na pasta produtos/test.

Devido à falta de tempo, não foi possível fazer a entrega da aplicação através de Minikube + kubectl. Comecei a tentar entender como o Kubernetes e o Docker funcionavam, mas ocorreram alguns erros e achei melhor fazer a entrega através do Heroku.

Para adicionar segurança, foi implementado um mecanismo de autenticação para acessar as views. Apenas para fins de demonstração, criei um usuário de teste para poder acessar:

usuário: teste

senha: Django.123