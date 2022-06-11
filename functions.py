import json

def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates
