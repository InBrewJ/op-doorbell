# home.urawizard Infra

By infra, I mean:

- compute for RabbitMQ in the cloud
- maybe a database that also subscribes to the queue
  - GCP has a free-forever tier of Firestore?
  - AWS has 25GB of DynamoDB which is free forever
- compute for the web server (home.urawizard.com)
- config for these things

## RabbitMQ

see: https://codeburst.io/get-started-with-rabbitmq-on-docker-4428d7f6e46b
Run with:

```
docker run --rm -it -d --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

add rules to firewall (with the right project selected):

```
gcloud compute firewall-rules create allow-5672-rabbit --allow tcp:5672
gcloud compute firewall-rules create allow-15672-rabbit --allow tcp:15672
```

## PostgreSQL

- Run it in docker (for now)
- Later on, try CloudSQL why not
- Connecting RabbitMQ to PG
  - https://area-51.blog/2017/02/11/publishing-messages-to-rabbitmq-from-postgresql/

## Web Server

- See https://github.com/InBrewJ/auto_ssl_nginx (for now)
