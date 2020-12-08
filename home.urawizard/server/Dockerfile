FROM tomcat:9.0.40-jdk11-adoptopenjdk-hotspot
LABEL maintainer="jason@urawizard.com"
ADD context.xml /usr/local/tomcat/conf

# Add the build
ADD ./target/gandalf.war /usr/local/tomcat/webapps/

EXPOSE 8080
CMD ["catalina.sh", "run"]