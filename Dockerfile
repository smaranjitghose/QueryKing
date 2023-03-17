FROM python:3.9.16-slim-bullseye
EXPOSE 8080
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8501"]