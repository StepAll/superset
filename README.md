# superset

## Deploy superset on VM with Docker file

[quick start Superset](https://medium.com/towards-data-engineering/quick-setup-configure-superset-with-docker-a5cca3992b28)



`docker build -t superset_app . `

`docker compose up`

_Init Superset:_  
```bash
docker exec -it superset_app superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email solegn@gmail.com \
              --password admin &&
docker exec -it superset_app superset db upgrade &&
docker exec -it superset_app superset init
```

## Connection string for SQL SERVER
`mssql+pyodbc://USERNAME:PASSWORD@77.223.102.193:13788/levelgroup-ru?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes`


[Connect to Googleshhet](https://preset.io/blog/2020-06-01-connect-superset-google-sheets/)
