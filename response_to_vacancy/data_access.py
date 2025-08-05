from json import dumps, loads
from operator import itemgetter
from pathlib import Path
from typing import Any, Iterator

from hh_api import get_vacancies

DATA_PATH: Path = Path(__file__).parent / ".used_vacancies.json"
if not DATA_PATH.exists():
    DATA_PATH.touch(0o600)
    DATA_PATH.write_text(dumps({}))


used_vacancies: dict[str, str] = loads(DATA_PATH.read_bytes())
vacancies: Iterator[dict[str, Any]] = filter(
    lambda v: v["id"] not in used_vacancies,
    get_vacancies(),
)

current_vacancy: dict[str, Any] = next(vacancies)
current_employer: dict[str, Any] = {}


def load_new_data() -> None:
    global current_vacancy
    used_vacancies[current_vacancy["id"]] = current_vacancy["alternate_url"]
    current_vacancy = next(vacancies)
    DATA_PATH.write_text(dumps(used_vacancies))


def get_vacancy_raw_data() -> dict[str, Any]:
    """Возвращает актуальные сырые данные для анализа"""
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
