import random

from data.data import Person
from faker import Faker  # ввожу вручную   # faker - библиотека, которая позволяет генерировать данные (установка через консоль pip install faker)

faker_en = Faker('En')    # ввожу вручную


def generated_person():
    return Person (    # возвращаю класс и просто заполняю поля рандомом
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject='English'
    )


def generated_file():   # генерация файла для инпута на странице
    path = rf'D:\pythonProject\new_automation_test_UI\test{random.randint(10,100)}.txt'   #вначале rf потому что генерирую рандомный путь файла
    file = open(path, 'w')   # w - это сокращение метода по созданию и перезаписыванию файла (в open много этих методов, в описании)
    file.write(f'helloworld{random.randint(23,100)}')   #то, что пишется внутрь файла
    file.close()
    return path


