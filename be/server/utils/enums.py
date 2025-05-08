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
