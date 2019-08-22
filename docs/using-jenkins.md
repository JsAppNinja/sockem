# Using jenkins
* Once docker-compose up has finished and Jenkins is up and running, 
  go to ```localhost:8080```
## Initial set up
* When first accessing Jenkins, you will be asked for the initial admin password
* The password was output into the terminal when the container was first built
* It can also be accessed by using the command below
* Git Bash on Windows
 ```winpty docker exec sockem-boppem_jenkins_1 cat //var//jenkins_home//secrets//initialAdminPassword```
* Others 
```docker exec sockem-boppem_jenkins_1 cat /var/jenkins_home/secrets/initialAdminPassword```
* When you're in, install suggested plugins and when it's finished, create a login, continue with default settings
 and you're done!