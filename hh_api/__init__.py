import functools

from . import hh_requests

MAX_DEPTH = 2000


def get_vacancies(
    per_page=100,
    text="Python",
    experience=("noExperience", "between1And3"),
    excluded_text="1С,DevOps,Scientist,QA",
):
    partial_vacancies = functools.partial(
        functools.partial,
        hh_requests.get_request,
        "vacancies",
        text=text,
        experience=experience,
        excluded_text=excluded_text,
    )
    get_vacancies = partial_vacancies(
        order_by="relevance",
        no_magic=True,
    )
    get_statistics = partial_vacancies(
        per_page=0,
        clusters=True,
    )

    match get_statistics().json():
        case {"found": found}:
            depth = min(MAX_DEPTH, found)
        case _:
            raise ValueError()

    vacancies = []
    for page in range((depth + per_page - 1) // per_page):
        match get_vacancies(page=page, per_page=per_page).json():
            case {"items": items}:
                vacancies.extend(items)
            case _:
                raise ValueError()

    return vacancies
