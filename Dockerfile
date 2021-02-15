FROM tomcat:9.0.43-jdk15-openjdk-slim

COPY sample.war /usr/local/tomcat/webapps/

#ENTRYPOINT [ "/run.sh" ]