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
## Steps to run:

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
-------------------------------------------------------------------------------