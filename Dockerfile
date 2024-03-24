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

