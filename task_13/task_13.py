# 13. Создайте декоратор для метода, который выводит ФИО.
# Пусть новый метод выводит ФИО, заключенное в теги <strong>.
import datetime


def strong_decorator(func):
    def wrapper(self) -> str:
        origin = func(self)
        return f'<strong>{origin}</strong>'
    return wrapper


class Person:
    def __init__(self, last_name: str, first_name: str, birth_year: int) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.birth_year = birth_year

    @strong_decorator
    def get_full_name(self) -> str:
        return f'ФИО: {self.first_name} {self.last_name}'

    def get_age(self) -> int:
        return int(datetime.datetime.now().year) - self.birth_year


class NewPerson(Person):
    def get_age(self) -> int:
        age = (int(datetime.datetime.now().year) - self.birth_year) * 365
        return age


def main():
    person = NewPerson('Дарья', 'Федорова', 2004)
    age = person.get_full_name()
    print(age)


if __name__ == '__main__':
    main()