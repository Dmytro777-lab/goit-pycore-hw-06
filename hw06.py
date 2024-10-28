from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name: str):
        self.name = name  # Виклик сеттера для перевірки

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if value:  # Перевірка, що ім'я не порожнє
            self._name = value
        else:
            raise ValueError("Ім'я не може бути порожнім")

class Phone(Field):
    def __init__(self, phone_number: str):
        self._phone_number = None  # Тимчасове значення, щоб пройшла перша перевірка
        self.phone_number = phone_number  # Виклик сеттера для перевірки номера

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if value.isdigit() and len(value) == 10:  # Перевірка, що номер складається з 10 цифр
            self._phone_number = value
        else:
            raise ValueError("Номер телефону має містити тільки 10 цифр")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []  # Список для зберігання об'єктів Phone

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)  # Використовуємо клас Phone для створення об'єкта
        self.phones.append(phone)  # Додаємо створений об'єкт до списку

    def remove_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.phone_number == phone_number:  # Порівнюємо номери
                self.phones.remove(phone)  # Видаляємо об'єкт Phone зі списку
                return
        raise ValueError("Телефон не знайдено")  # Якщо телефон не знайдено
    
    def edit_phone(self, old_phone_number: str, new_phone_number: str):
        for phone in self.phones:
            if phone.phone_number == old_phone_number:  # Порівнюємо старий номер
                phone.phone_number = new_phone_number  # Змінюємо номер на новий
                return
        raise ValueError("Старий телефон не знайдено")  # Якщо старий номер не знайдено
    
    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.phone_number == phone_number:  # Порівнюємо номер
                return phone  # Повертаємо знайдений об'єкт Phone
        raise ValueError("Телефон не знайдено")  # Якщо номер не знайдено
    
    def __str__(self):
        return f"Contact name: {self.name.name}, phones: {'; '.join(p.phone_number for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record: Record):
        self.data[record.name.name] = record  # Використовуємо ім'я контакту як ключ

    def find(self, name: str):
        for record in self.data.values():  # Перебираємо всі записи
            if record.name.name.lower() == name.lower():  
                return record  # Повертаємо знайдений запис
        raise ValueError("Контакт не знайдено")  

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

