# Kafka Client

API's criadas para fazer publicações no kafka, no formato json ou avro.

Foi criado um módulo para publicação em tópicos no formato json (producer.py), um módulo para publicar eventos no formato avro (avro_producer.py) e um módulo para carregar um consumidor que pode ser plugado no tópico (consumer.py).

A aplicação está dockerizada. Seus módulos podem ser subidos separadamente, usando os scripties shell incluídos na raiz do projeto.

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

Necessário alterar o arquivo configure.ini com as configurações do broker e tópico que deseja publicar/consumir eventos.

Caso deseje publicar eventos em um tópico avro, atualize o arquivo schema.avsc com o schema do tópico que deseja publicar.

Para subir as dependências (kafka-broker, schema-registry, etc) execute o comando:

```docker-compose up -d'```

Para subida do producer-json, execute o script run-producer.sh.

Para subida do producer-avro, execute o script run-avro-producer.sh.

Para subida do consumer, execute o script run-consumer.sh.

Os módulos producer.py e avro_producer.py usam a mesma porta exposta para chamada da api de publicação de eventos, por isso não devem ser subidas no mesmo momento, para não haver conflito de bind na porta 5000.

## Execução

Para publicar os eventos, deverá ser chamado a api /produce, enviando o payload do evento que deseja publicar. Ex:

```curl -X POST -H "Content-Type: application/json" http://localhost:5000/produce -d '{"test":"blah"}'```

É possível enviar o payload usando o recurso de leitura de arquivo do curl. Assim você pode incluir o payload do evento no arquivo sample.json e executar o comando:

```curl -X POST -H "Content-Type: application/json" http://localhost:5000/produce -d @sample.json```