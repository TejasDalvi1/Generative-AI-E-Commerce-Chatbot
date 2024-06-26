===============================================================================
# Generative-AI-E-Commerce-Chatbot
===============================================================================

## Tech stack:
        (1)Python
        (2)Langchain
        (3)Datastax Astra DB (Cassandra)
        (4)OpenAI
        (5)Flask
        (6)HTML,CSS
-------------------------------------------------------------------------------
## Steps to run in local setup:

### (1) Create Environment
```bash
conda create -n ecombot python=3.10 -y
```
```bash
conda activate ecombot/
```

### (2) Install "requirements.txt"
```bash
pip install -r requirements.txt
```

### (3) Create a `.env` file in the root directory and add your credentials:
```ini
OPENAI_API_KEY="xxxx"
ASTRA_DB_API_ENDPOINT="xxxx"
ASTRA_DB_APPLICATION_TOKEN="xxxx"
ASTRA_DB_KEYSPACE="xxxx"
```
### (4) To install local package:
```bash
python setup.py
```

### (6) Run "app.py":
```bash
# Finally run the following command
python app.py
```

### (6) Click on the link got after step (6):
```bash
open up localhost:
```
===============================================================================
## How to Deploy this app on AWS EC2:

### (1) Login into your AWS console and launch an EC2 instance
### (2) Run the following commands (Note: Do the port mapping)

```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```

```bash
git clone "Github-URL-of-Your-repository"
```
```bash
touch .env
```
```bash
vim .env
# Here add following credentials
#OPENAI_API_KEY="****"
#ASTRA_DB_API_ENDPOINT="****"
#ASTRA_DB_APPLICATION_TOKEN="****"
#ASTRA_DB_KEYSPACE="****"
```
```bash
sudo apt install python3-pip
```
```bash
sudo apt install python3-venv
```
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```
```bash
pip3 install -r requirements.txt
```
```bash
#Temporary running
python3 app.py
```
```bash
#Permanent running
nohop python3 app.py
```
-------------------------------------------------------------------------------
