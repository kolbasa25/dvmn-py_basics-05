import file_operations
from faker import Faker
import random


SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]


RUNES = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠', 'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋', 'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒', 'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠', 'ф': 'ф̋̋', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋', 'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠', 'ю': 'ю̋͠', 'я': 'я̋', ' ': ' '
}


def main():

    fake = Faker("ru_RU")

    for i in range(1, 11):
        name = fake.first_name()
        last_name = fake.last_name()
        job = fake.job()
        town = fake.city()
        number_strength = random.randint(3, 18)
        number_agility = random.randint(3, 18)
        number_endurance = random.randint(3, 18)
        number_intelligence = random.randint(3, 18)
        number_luck = random.randint(3, 18)

        skills_runes = []

        for skill in SKILLS:
            new_skill = skill
            for c, r in RUNES.items():
                new_skill = new_skill.replace(c, r)
            skills_runes.append(new_skill)

        random_skills = random.sample(skills_runes, 3)

        context = {
            "first_name": name,
            "last_name": last_name,
            "job": job,
            "town": town,
            "strength": number_strength,
            "agility": number_agility,
            "endurance": number_endurance,
            "intelligence": number_intelligence,
            "luck": number_luck,
            "skill_1": random_skills[0],
            "skill_2": random_skills[1],
            "skill_3": random_skills[2]
        }

        file_operations.render_template(
            r"C:\python_scripts\src\charsheet.svg",
            "C:\\python_scripts\\output\\svg\\charsheet-{}.svg".format(i),
            context
        )


if __name__ == "__main__":
    main()