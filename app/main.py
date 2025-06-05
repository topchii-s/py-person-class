class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    person_list = [Person(p["name"], p["age"]) for p in people_data]

    for p in people_data:
        person_instance = Person.people[p["name"]]
        spouse_name = p.get("wife") or p.get("husband")
        if spouse_name:
            attr = "wife" if "wife" in p else "husband"
            setattr(person_instance, attr, Person.people[spouse_name])

    return person_list
