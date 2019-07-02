# Using pgAdmin4
## Connecting to server
* Once the container is up using `docker-compose`, pgAdmin4 should be up on localhost:5555

## Logging in
* Login information can be found in `/pgadmin4/pgadmin-dev.env`

## Adding server / connecting to db
* Click `add new server`
* For the hostname, refer to db's `container_name` in docker-compose.yml
* The remaining information can be found in `/db/db-dev.env`
* The `maintanence db` field refers to `POSTGRES_DB` in the `db-dev.env` file