# Getting started

## .gitignore
* Create a file called ```.gitignore``` in the project directory and past everything from this link

```https://github.com/github/gitignore/blob/master/Python.gitignore```

## Using Docker
### Installation
https://hub.docker.com/editions/community/docker-ce-desktop-windows
https://hub.docker.com/editions/community/docker-ce-desktop-mac

### Running the app
* Now, the app and everything else you might need for development can be started with one simple 
  command line code in the project directory!
  
```docker-compose up```

* The frontend React app will be live on ```localhost:3000```
* The backend Django app will be live on ```localhost:8000```
* The PostgreSQL database will be live on ```localhost:5432```
* The Jenkins server will be live on ```localhost:8080```
* The pgAdmin server will be live on ```localhost:5555```

### Closing the app 
* The app can be stopped with CTRL + C (Or whatever appropriate command on your OS) then just run the code 
  below to stop and remove the other containers if desired

```docker-compose down```
