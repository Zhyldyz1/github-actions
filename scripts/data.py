import json
data = {
    "key": "value",
    "status": "processed"
}
with open("python-data.json", "w") as f:
    json.dump(data, f)
