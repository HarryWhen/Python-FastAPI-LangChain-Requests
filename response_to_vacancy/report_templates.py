from enum import StrEnum, auto
from json import dumps

from .data_access import get_vacancy_raw_data


def prepare_cover_letter():
    pass


def make_response():
    pass


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
    print(
        dumps(
            {
                "is_remote": is_remote,
                "location": location,
                "reliability": reliability,
                "skills_match": skills_match,
                "work_tasks": work_tasks,
                "chances_of_offer": chances_of_offer,
                "advices": advices,
                "vacancy": get_vacancy_raw_data(),
            }
        )
    )
