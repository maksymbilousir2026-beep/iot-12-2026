class Student:
    def __init__(self, student_id=0, last_name="", first_name="", grades=None):
        self._student_id = student_id
        self._last_name = last_name
        self._first_name = first_name
        self._grades = list(grades) if grades else []

    def __del__(self):
        print(f"[Деструктор] Студента {self._last_name} {self._first_name} видалено з пам'яті")

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def grades(self):
        return list(self._grades)

    @grades.setter
    def grades(self, value):
        self._grades = list(value)

    def add_grade(self, grade):
        if not 0 <= grade <= 100:
            raise ValueError("Оцінка має бути в межах від 0 до 100")
        self._grades.append(grade)

    def average(self):
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    def show(self):
        grades = ", ".join(map(str, self._grades)) if self._grades else "немає"
        print(f"ID: {self._student_id:<4} {self._last_name} {self._first_name:<10} "
              f"Оцінки: [{grades}]  Середній бал: {self.average():.2f}")



class Group:
    def __init__(self, name="", students=None):
        self._name = name
        self._students = list(students) if students else []

    def __del__(self):
        print(f"[Деструктор] Групу {self._name} видалено з пам'яті")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def students(self):
        return list(self._students)

    def __len__(self):
        return len(self._students)

    def add_student(self, student):
        if any(s.student_id == student.student_id for s in self._students):
            print(f"Студент з ID {student.student_id} уже є в групі")
            return False
        self._students.append(student)
        return True

    def remove_student(self, student_id):
        for s in self._students:
            if s.student_id == student_id:
                self._students.remove(s)
                print(f"Студента {s.last_name} {s.first_name} видалено з групи")
                return True
        print(f"Студента з ID {student_id} не знайдено")
        return False

    def find_student(self, student_id):
        for s in self._students:
            if s.student_id == student_id:
                return s
        return None

    def show_student_rating(self, student_id):
        student = self.find_student(student_id)
        if student is None:
            print(f"Студента з ID {student_id} не знайдено")
            return
        ranked = sorted(self._students, key=lambda s: s.average(), reverse=True)
        place = ranked.index(student) + 1
        print(f"Студент {student.last_name} {student.first_name}: "
              f"{place} місце з {len(ranked)}, середній бал {student.average():.2f}")

    def show(self):
        print(f"\nГрупа {self._name} (студентів: {len(self._students)})")
        for s in self._students:
            s.show()

    def show_rating(self):
        print(f"\nРейтинг групи {self._name}:")
        ranked = sorted(self._students, key=lambda s: s.average(), reverse=True)
        for place, s in enumerate(ranked, 1):
            print(f"{place}. {s.last_name} {s.first_name} — {s.average():.2f}")


def main():
    s1 = Student(1, "Заяць", "Олег", [90, 85, 95])
    s2 = Student(2, "Кіцану", "Павло", [70, 75, 80])
    s3 = Student(3, "Драпак", "Роман")
    s3.add_grade(100)
    s3.add_grade(92)
    s3.add_grade(88)

    group = Group("IP-12")
    for s in (s1, s2, s3):
        group.add_student(s)

    group.show()
    group.show_rating()

    print("\n--- Видалення студента з ID 2 ---")
    group.remove_student(2)
    del s2

    group.show()
    group.show_rating()

    group.show_student_rating(3)
    group.show_student_rating(99)

    print("\n--- Доступ до полів ---")
    print("Прізвище першого студента:", s1.last_name)
    s1.last_name = "Заяць"
    s1.show()

    print("\n--- Завершення програми ---")


if __name__ == "__main__":
    main()