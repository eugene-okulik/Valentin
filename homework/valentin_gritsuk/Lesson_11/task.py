class Book:
    material_of_page = 'бумага'
    text_is_in = True

    def __init__(self, title, author, page_counts, isbn, is_reserved):
        self.title = title
        self.author = author
        self.page_counts = page_counts
        self.isbn = isbn
        self.is_reserved = is_reserved

    def about_me(self):
        text = (f'Название: {self.title}, Автор: {self.author}, страниц: {self.page_counts}, '
                f'материал: {self.material_of_page}{", зарезервирована" if self.is_reserved else ""}')
        return text


class SchoolTextbook(Book):

    def __init__(self, title, author, page_counts, isbn, is_reserved, subject, class_grade, tasks_are_in):
        super().__init__(title, author, page_counts, isbn, is_reserved)
        self.subject = subject
        self.class_grade = class_grade
        self.tasks_are_in = tasks_are_in

    def about_me_print(self):
        text = (super().about_me().replace(', зарезервирована','').
                replace(f'материал: {self.material_of_page}', ''))
        text  += f'предмет: {self.subject}, класс: {self.class_grade}{", зарезервирована" if self.is_reserved else ""}'
        print(text)


first_book = Book('Кот в сапогах', 'Андерсен', 26, 123124124, False)
second_book =  Book('Идиот', 'Достоевский', 245, 4214123, False)
third_book = Book('Война и мир', 'Толстой', 3253342434, 42342, False)
fourth_book = Book('Алые паруса', 'Грин', 54, 2341234, False)
fifth_book = Book('Журавлиный крик', 'Быков', 62, 978985, False)
first_book.is_reserved = True
print(first_book.about_me())
print(second_book.about_me())
print(third_book.about_me())
print(fourth_book.about_me())
print(fifth_book.about_me())

math_book = SchoolTextbook('Алгебра', 'Герасимов', '43', '13-4124-124',
                           False, 'Математика', '10', True)
english_book = SchoolTextbook('Язык', 'Петичкин', '21', '123542-124',
                           False, 'Русский', '5', True)
russ_book = SchoolTextbook('Язык', 'Калинин', '64', '53-41432-122',
                           False, 'Английский', '11', True)
math_book.is_reserved = True
math_book.about_me_print()
english_book.about_me_print()
russ_book.about_me_print()
