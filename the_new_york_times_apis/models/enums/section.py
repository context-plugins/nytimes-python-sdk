from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Section(str, Enum):
    ARTS = "arts"
    AUTOMOBILES = "automobiles"
    BOOKS_REVIEW = "books/review"
    BUSINESS = "business"
    FASHION = "fashion"
    FOOD = "food"
    HEALTH = "health"
    HOME = "home"
    INSIDER = "insider"
    MAGAZINE = "magazine"
    MOVIES = "movies"
    NYREGION = "nyregion"
    OBITUARIES = "obituaries"
    OPINION = "opinion"
    POLITICS = "politics"
    REALESTATE = "realestate"
    SCIENCE = "science"
    SPORTS = "sports"
    SUNDAYREVIEW = "sundayreview"
    TECHNOLOGY = "technology"
    THEATER = "theater"
    T_MAGAZINE = "t-magazine"
    TRAVEL = "travel"
    UPSHOT = "upshot"
    US = "us"
    WORLD = "world"

    __str__ = str.__str__


SectionOrStr: TypeAlias = Annotated[Section | str, open_enum_validator(Section)]
