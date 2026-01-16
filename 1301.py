import os
import random
from faker import Faker
import file_operations

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
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

def main():
    fake = Faker("ru_RU")
    template_path = "charsheet.svg"

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, 11):
        name = fake.first_name()
        last_name = fake.last_name()
        job = fake.job()
        town = fake.city()
        strength = random.randint(3, 18)
        agility = random.randint(3, 18)
        endurance = random.randint(3, 18)
        intelligence = random.randint(3, 18)
        luck = random.randint(3, 18)

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
            "strength": strength,
            "agility": agility,
            "endurance": endurance,
            "intelligence": intelligence,
            "luck": luck,
            "skill_1": random_skills[0],
            "skill_2": random_skills[1],
            "skill_3": random_skills[2]
        }

        output_path = f"{output_dir}/charsheet-{i}.svg"
        file_operations.render_template(template_path, output_path, context)


if __name__ == "__main__":
    main()