# gandalf.contrived.name

## Welcome to Java Land

### The basic premise:

- A consumer that forwards messages from RabbitMQ to JS frontends via [server sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) (SSE)
- Will expose SSE interface via http://gandalf.contrived.name/events

### Deployment

- Build the WAR
- Deploy it to a Tomcat server running on gandalf.contrived.name
- Hope it works

Steps:

```
mvn package # generate the WAR with Maven
docker build -t inbrewj/tomcat-gandalf .
docker run --network host -p 8080:8080 inbrewj/tomcat-gandalf
docker push inbrewj/tomcat-gandalf
```

It will then start on:

- http://localhost:8080/gandalf/

Ideally, ofc, it would start on just localhost:8080. I should probably learn how to configure Tomcat properly. It's probably something to do with a context.xml somewhere.

### What needs to happen after that:

- Security
- Any security
- That is, something in the ../auth directory
  - There should at least be a damn plan in there
- Unit tests
- CI/CD
