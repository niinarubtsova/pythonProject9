import json

# `load_candidates_from_json(path)` – возвращает список всех кандидатов
# `get_candidate(candidate_id)` – возвращает одного кандидата по его id
# `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
# `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку

def load_candidates():
    with open("candidates.json", "r", encoding="utf=8") as file:
        return json.load(file)


def get_candidates_all():
    return load_candidates()


def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return None


def get_candidates_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            candidates.append(candidate)
    return candidates


def get_candidates_by_name(name):
    candidates = []
    for candidate in load_candidates():
        if name in candidate['name']:
            candidates.append(candidate)
    return candidates
