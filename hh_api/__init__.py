from functools import partial

from .hh_requests import request_vacancies, request_vacancies_statistics

MAX_DEPTH = 2000


def get_vacancies(
    per_page=100,
    text="Python",
    experience=("noExperience", "between1And3"),
    excluded_text="1С,DevOps,Scientist,QA",
):
    partial_rv = partial(
        partial,
        text=text,
        experience=experience,
        excluded_text=excluded_text,
    )
    r_vacancies = partial_rv(request_vacancies)
    r_statistics = partial_rv(request_vacancies_statistics)

    match r_statistics():
        case {"found": found}:
            depth = min(MAX_DEPTH, found)
        case _:
            raise ValueError()

    vacancies = []
    for page in range((depth + per_page - 1) // per_page):
        match r_vacancies(page=page, per_page=per_page):
            case {"items": items}:
                vacancies.extend(items)
            case _:
                raise ValueError()

    return vacancies
