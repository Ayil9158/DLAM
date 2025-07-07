class CharacterInformation:
    def __init__(self, name, age, sponsor, exclu_at, exclu_at_grade, skills, stigmas, stats, evaluation):
        self.name = name
        self.age = age
        self.sponsor = sponsor
        self.exclu_at = exclu_at
        self.exclu_at_grade = exclu_at_grade
        self.skills = skills
        self.stigmas = stigmas
        self.stats = stats
        self.evaluation = evaluation

# CHARACTER: LEE HYUNSUNG
lee_hyunsung = CharacterInformation(
    name="LEE HYUNSUNG",
    age="28",
    sponsor="MASTER OF STEEL",
    exclu_at="SOLDIER WHO TURNED A BLINK EYE TO INJUSTICE",
    exclu_at_grade="ORDINARY",
    skills=[
        ("BAYONET", 2),
        ("CAMOUFLAGE", 2),
        ("PATIENCE", 2)
    ],
    stigmas=[
        ("GREAT MOUNTAIN PUSH", 1)
    ],
    stats=[
        ("PHYSIQUE", 8),
        ("STRENGTH", 8),
        ("AGILITY", 7),
        ("MAGIC POWER", 5)
    ],
    evaluation=(
        "THE OVERALL STATS ARE PRETTY GOOD.\n"
        "DESPITE TURNING AWAY FROM INJUSTICE, HE WAS CHOSEN BY A CONSTELLATION.\n"
        "THIS WILL BE ANOTHER OPPORTUNITY FOR HIM."
    )
)

# 👤 Personaje: KIM NAMWOON
kim_namwoon = CharacterInformation(
    name="KIM NAMWOON",
    age="19",
    sponsor="N/A",
    exclu_at="EDGY TEEN",
    exclu_at_grade="ORDINARY",
    skills=[
        ("ABNORMAL ADAPTIVITY", 3),
        ("KNIFE FIGHTING", 1),
        ("DARK SIDE", 1)
    ],
    stigmas=[],  # N/A
    stats=[
        ("PHYSIQUE", 3),
        ("STRENGTH", 4),
        ("AGILITY", 6),
        ("MAGIC POWER", 4)
    ],
    evaluation=(
        "AN EDGY TEENAGER WHO HAS TURNED TO THE DARK SIDE DUE TO A TRIGGER.\n"
        "BEST NOT TO GET INVOLVED WITH HIM."
    )
)