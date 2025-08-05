from json import dump, load
from operator import itemgetter
from pathlib import Path
from typing import Any, Iterator

from hh_api import get_vacancies

DATA_PATH: Path = Path(__file__).parent / ".past_vacancies.json"


vacancies: Iterator[dict[str, Any]] = get_vacancies()
with DATA_PATH.open("r") as data:
    used_vacancies: set[dict[str, Any]] = load(data)

current_vacancy: dict[str, Any] = next(vacancies)
current_employer: dict[str, Any] = {}


def update_data(vacancy) -> None:
    pass


def load_next_data() -> None:
    vacancy = next(vacancies)
    while current_vacancy in used_vacancies:
        vacancy = next(vacancies)
    update_data(vacancy)


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
    if wf := [
        *data["work_format"],
        *data["working_hours"],
        *data["work_schedule_by_days"],
    ]:
        rep.append(f"Возможно работать {", ".join(map(itemgetter("name"), wf))}.")
    rep.append(f"{data["employment_form"]["name"]} занятость.")
    return " ".join(rep)


def get_employer_raw_data() -> dict[str, Any]:
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


def get_extended_employer_raw_data() -> dict[str, Any]:
    return current_employer


def get_extended_employer_meta_data() -> str:
    data = get_extended_employer_raw_data()
    rep = []
    rep.append(get_employer_meta_data())
    return " ".join(rep)
