# 11. Создайте метод, который вычисляет возраст в годах.
import datetime


class Person:
    def __init__(self, last_name: str, first_name: str, birth_year: int) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.birth_year = birth_year

    def get_full_name(self) -> str:
        return f'ФИО: {self.first_name} {self.last_name}'

    def get_age(self) -> int:
        return int(datetime.datetime.now().year) - self.birth_year


def main():
    person = Person('Дарья', 'Федорова', 2004)
    age = person.get_age()
    print(age)


if __name__ == '__main__':
    main()