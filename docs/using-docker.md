# Using Docker

## Entering a container via CLI
* For bash on windows, use `$ winpty docker exec -it sockem-boppem_backend_1 //bin//sh`
* Otherwise try `docker exec -it <container name> /bin/bash`

### Tools
* Sometimes you might want to nuke all your docker images and containers. Copy the following script and save it as a .bat file and run it to do so

```
@echo off
FOR /f "tokens=*" %%i IN ('docker ps -aq') DO docker rm %%i
FOR /f "tokens=*" %%i IN ('docker images --format "{{.ID}}"') DO docker rmi %%i
```