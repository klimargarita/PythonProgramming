import json

def task() -> float:

    with open('input.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        scores = [entry.get("score", 0) * entry.get("weight", 0) for entry in data]
        total_sum = sum(scores)
    return round(total_sum, 3)

print(task())
