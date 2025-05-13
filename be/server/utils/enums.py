from django.db import models


class Topic(models.TextChoices):
    FICTION = "FIC", "Fiction"
    NONFICTION = "NON", "Non-Fiction"
    SCIENCE = "SCI", "Science"
    HISTORY = "HIS", "History"
    TECHNOLOGY = "TECH", "Technology"
    PHILOSOPHY = "PHI", "Philosophy"
    ART = "ART", "Art"
    MUSIC = "MUS", "Music"
    BIOGRAPHY = "BIO", "Biography"
    SELF_HELP = "SH", "Self-Help"
    BUSINESS = "BUS", "Business"
    RELIGION = "REL", "Religion"
    HEALTH = "HEA", "Health"
    EDUCATION = "EDU", "Education"
    TRAVEL = "TRV", "Travel"
    COOKING = "CKG", "Cooking"
    SPORTS = "SPT", "Sports"
    POETRY = "POE", "Poetry"
    COMICS = "COM", "Comics"
    CHILDREN = "CHD", "Children"

    @classmethod
    def bit_position(cls, code: str) -> int:
        topic_codes = [t.value for t in cls]
        return topic_codes.index(code)


class EventTopic(models.TextChoices):
    LITERATURE = "LIT", "Literature & Author Talks"
    HISTORY = "HIS", "History & Archives"
    SCIENCE = "SCI", "Science & Nature"
    ART = "ART", "Art Exhibitions & Workshops"
    MUSIC = "MUS", "Music & Performance"
    TECHNOLOGY = "TEC", "Technology & Innovation"
    EDUCATION = "EDU", "Education & Learning Skills"
    WRITING = "WRIT", "Creative Writing"
    CHILDREN = "CHD", "Children’s Programs"
    YOUTH = "YTH", "Youth & Teen Engagement"
    CULTURE = "CUL", "Cultural Heritage"
    COMMUNITY = "COM", "Community & Social Issues"
    ENVIRONMENT = "ENV", "Environment & Sustainability"
    HEALTH = "HLTH", "Health & Wellness"
    DIGITAL = "DIG", "Digital Literacy"
    FILM = "FILM", "Film Screenings & Analysis"
    PHILOSOPHY = "PHI", "Philosophy & Ethics"
    BUSINESS = "BIZ", "Business & Career Development"
    DIY = "DIY", "DIY, Crafts & Makerspaces"
    LANGUAGE = "LANG", "Language & Literacy"

    @classmethod
    def bit_position(cls, code: str) -> int:
        return [t.value for t in cls].index(code)
