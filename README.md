# FILE RETRIEVAL SYSTEM

Diagnosis backend challenge

## Getting Started

Clone repository to your local and navigate into the folder

```bash
git clone https://github.com/horlali/file-retrieval-system
cd file-retrieval-system/
```

## Setup Local Environment

Install the required dependencies

```bash
pip install -r requirements.txt

```

## Make Scripts Executable

```bash
chmod +x scripts/*
```

## Running Servers

In the root of the repository `:~/file-retrieval-system` run the scripts below

```bash
./scripts/run-server.sh
```

whiles the server is running open another terminal and run the client script

```bash
./scripts/run-client.sh
```

## Sample Request and Application Docs

Once the application is up and running, visit <http://127.0.0.1:8501/> or <http://localhost:8501> or in your browser

You should see a Swagger Documentation Page like this

![Alt text](files/home.png)
