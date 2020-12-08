mvn package # generate the WAR with Maven
docker build -t inbrewj/tomcat-gandalf .
docker push inbrewj/tomcat-gandalf