# Kafka Client

API criada para publicar eventos no kafka no formato json ou avro.

Foi criado um módulo publicação no formato json (producer.py), um módulo para publicar no formato avro (avro_producer.py) e um módulo consumidor para ser plugado no tópico (consumer.py).

A aplicação está conteinerizada. Seus módulos podem ser subidos separadamente, executando os scripts em shell que constam na raiz do projeto.

## Stack

  Tecnologia           |  Versão       |
-----------------------|---------------|
  python               | 3
  flask                | 2.3.2
  confluent-kafka      | 2.1.1
  confluent-kafka[avro]| 2.1.1

## Dependências

* docker
* docker-compose
* curl

## Instalação

Necessário alterar o arquivo config.ini com as configurações do broker e tópico que deseja publicar/consumir os eventos.

Caso deseje publicar eventos em um tópico avro, atualize o arquivo schema.avsc com o schema do tópico que deseja publicar.

Para subir as dependências (kafka-broker, schema-registry, etc) execute o comando:

```docker-compose up -d```

Para subida do producer json, execute o script run-producer.sh.

Para subida do producer avro, execute o script run-avro-producer.sh.

Para subida do consumer, execute o script run-consumer.sh.

Os módulos producer.py e avro_producer.py usam a mesma porta que é usada pela api, por isso não suba as duas no mesmo momento, para não haver conflito de bind na porta 5000.

## Execução

Para publicar os eventos, deverá ser chamado a api /produce, enviando o payload do evento que deseja publicar. Ex:

```curl -X POST -H "Content-Type: application/json" http://localhost:5000/produce -d '{"test":"blah"}'```

É possível realizar as chamadas usando o recurso de envio do payload com o valor carregado de um arquivo. Assim você pode incluir o payload no arquivo sample.json e executar o comando:

```curl -X POST -H "Content-Type: application/json" http://localhost:5000/produce -d @sample.json```