from enum import StrEnum, auto
from itertools import chain
from operator import itemgetter
from typing import Any

current_vacancy: dict[str, Any] = {}


def load_next_vacancy() -> None:
    pass


def get_vacancy_raw_data() -> dict[str, Any]:
    return current_vacancy


def get_vacancy_meta_data() -> str:
    data = get_vacancy_raw_data()
    rep = []
    rep.append(f'Вакансия "{data["name"]}"')
    rep.append(f"Опубликована {data["published_at"]}.")
    if data["internship"]:
        rep.append(f"Формат в виде стажировки.")
    if sr := data["salary_range"]:
        sr_cr = sr["currency"]
        rep.append("Зарплата")
        if sr_fr := sr["from"]:
            rep.append(f"от {sr_fr} {sr_cr}")
        if sr_t := sr["to"]:
            rep.append(f"до {sr_t} {sr_cr}")
        rep.append(f"{sr["mode"]["name"].lower()}.")
    if (
        (wf := data["work_format"])
        or (wh := data["working_hours"])
        or (wsbd := data["work_schedule_by_days"])
    ):
        rep.append(
            f"Возможно работать {", ".join(map(itemgetter("name"), chain(wf, wh, wsbd)))}."
        )
    rep.append(f"{data["employment_form"]["name"]} занятость.")
    return " ".join(rep)


def get_employer_raw_data():
    return get_vacancy_raw_data()["employer"]


def get_employer_meta_data() -> str:
    data = get_employer_raw_data()
    rep = []
    rep.append(f'Компания "{data["name"]}".')
    rep.append(
        "Имеет подтверждение на сайте."
        if data["trusted"]
        else "Не имеет подтверждение на сайте."
    )
    rep.append(
        "Прошла IT аккредитацию."
        if data["accredited_it_employer"]
        else "Не прошла IT аккредитацию."
    )
    return " ".join(rep)


def get_extended_employer_meta_data() -> str:
    return get_employer_meta_data()


class Reliability(StrEnum):
    ESTABLISHED_AND_PURPOSEFUL = auto()
    STABLE_BUT_DIRECTIONLESS = auto()
    YOUNG_AND_CONSTRUCTIVELY_ALIGNED = auto()
    UNFOCUSED_OR_INCONSISTENT = auto()
    OVERCONFIDENT_WITH_UNCLEAR_GROUND = auto()
    OPERATIONALLY_ERRATIC = auto()
    OPAQUE_AND_REACTIVE = auto()
    TRANSIENT_OR_SUPERFICIAL = auto()


def report_vacancy(
    is_remote: bool,
    location: str,
    reliability: Reliability,
    skills_match: float,
    work_tasks: list[str],
    chances_of_offer: float,
    advices: list[str],
) -> None:
    """Show job report vacancy.

    Collect analysis data from AI agent and show job report vacancy for
    user reading.

    Args:
        is_remote (bool): True if offer remote work, otherwise False
        location (str): location of work office
        reliability (Reliability): employer reliability
        skills_match (float): AI assessment of the match between user and
            requirements skills
        work_tasks (list[str]): tasks to do at work
        chances_of_offer (float): AI assessment of chances of getting
            an offer
        advices (list[str]): AI advices to increase chances of getting
            an offer
    """
    print("YES")
