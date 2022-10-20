from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def index():
    candidates = utils.get_candidates_all()
    return render_template('list.html', candidates=candidates)

@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate_by_pk(pk)
    if not candidate:
        return "Не найдено"
    return render_template('candidate.html', candidate=candidate)

@app.route("/candidate/<skill>")
def get_candidates_by_skills(skill):
    candidates = utils.get_candidates_by_skill(skill)
    candidates_count = len(candidates)
    return render_template('skills.html'
                           , candidates=candidates
                           , candidates_count=candidates_count
                           , skill=skill
                           )

@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    candidates_count = len(candidates)
    return render_template('search.html'
                           , candidates=candidates
                           , candidates_count=candidates_count
                           )


app.run(debug=True)