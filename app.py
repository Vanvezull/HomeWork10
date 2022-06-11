from flask import Flask
import functions

app = Flask(__name__)

@app.route("/")
def homepage():
    candidates = functions.load_candidates()
    string = ""
    for candidate in candidates:
        string += f"<p> Имя кандидата - {candidate['name']}<br/> " \
                  f"Позиция кандидата - {candidate['position']}<br/> " \
                  f"Навыки кандидата - {candidate['skills']}</p>"
    return string

@app.route("/candidates/<int:uid>")
def candidates_profile(uid):
    candidates = functions.load_candidates()
    candidate_profile = ""
    if uid > len(candidates):
        return "Error: 404 Такого кандидата нет!"
    else:
        for candidate in candidates:
            if candidate['id'] == uid:
                candidate_profile += f"<img src = {candidate['picture']} <br/>" \
                                     f"<p>Имя кандидата - {candidate['name']} <br/>" \
                                     f"Позиция кандидата - {candidate['position']}<br/> " \
                                     f"Навыки кандидата - {candidate['skills']}</p>"
                return candidate_profile

@app.route("/skills/<skill>")
def candidate_skills(skill):
    candidates = functions.load_candidates()
    candidates_skills = ""
    for candidate in candidates:
        if skill.lower() in candidate["skills"].lower():
            candidates_skills += f"<p>Имя кандидата - {candidate['name']} <br/>" \
                                     f"Позиция кандидата - {candidate['position']}<br/> " \
                                     f"Навыки кандидата - {candidate['skills']}</p>"
    return candidates_skills


app.run(debug=True)