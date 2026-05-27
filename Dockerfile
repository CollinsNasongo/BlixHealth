FROM apache/airflow:3.2.1

USER root

RUN apt-get update && \
    apt-get install -y curl gnupg2 unixodbc unixodbc-dev && \
    curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
    > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y \
        msodbcsql18 \
        mssql-tools18 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="$PATH:/opt/mssql-tools18/bin"

USER airflow

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt