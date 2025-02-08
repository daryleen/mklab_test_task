# 10. Создайте метод, который выводит ФИО.

class Person:
    def __init__(self, last_name: str, first_name: str, birth_year: int) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.birth_name = birth_year

    def get_full_name(self) -> str:
        return f'ФИО: {self.first_name} {self.last_name}'


def main():
    person = Person('Дарья', 'Федорова', 2004)
    fullname = person.get_full_name()
    print(fullname)


if __name__ == '__main__':
    main()
