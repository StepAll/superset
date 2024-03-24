FROM apache/superset

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-transport-https \
    gpg-agent \
    unixodbc \ 
    build-essential \
    curl \
    software-properties-common \
    procps

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

RUN rm -rf /etc/apt/sources.list.d/* \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip3 install -r requirements.txt


COPY superset_config.py /app/

# docker build -t superset_img . 

# docker compose up

# docker exec -it superset_app superset fab create-admin \
#               --username admin \
#               --firstname Superset \
#               --lastname Admin \
#               --email admin@superset.com \
#               --password admin &&
# docker exec -it superset_app superset db upgrade &&
# docker exec -it superset_app superset init

# mssql+pyodbc://o.stepanov:,mw(>fwbW2>pU%%@77.223.102.193:13788/levelgroup-ru?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes
# mssql+pyodbc://o.stepanov:,mw(>fwbW2>pU%%@77.223.102.193:13788/uuniversity?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes