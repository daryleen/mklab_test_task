# 9. Создайте класс. Пусть в нем будут поля Фамилия, Имя, Год рождения.

class Person:
    def __init__(self, last_name: str, first_name: str, birth_year: int) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.birth_name = birth_year
