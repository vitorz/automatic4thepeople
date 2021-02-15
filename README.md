To build, run and test the tomcat/sample.war docker container, please follow these steps:

1. git clone this repository

2. go into the project folder and run the following command:
curl --output sample.war https://tomcat.apache.org/tomcat-9.0-doc/appdev/sample/sample.war

3. pip install 'docker-py>=1.7.0'

4. pip install 'docker-compose>=1.7.0'

5. run ansible-playbook against the file: ansi_tomcat_sample.yaml
