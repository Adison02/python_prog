import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

OPENTDB_URL = "https://opentdb.com/api.php"

response = requests.get(OPENTDB_URL, params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]