class Student:
    def __init__(self, name, home):
        if not name:  # print, sys.exit or even return none is not good
            raise ValueError("No name was given")  # creating our own error :D
        if home not in ["Vila isabel", "Rio de janeiro", "Rio"]:
            raise ValueError("Invalid home")
        self.name = name
        self.home = home


def main():
    student = get_student()
    print(f"{student.name} froms {student.home}")


def get_student():
    name = input("Name: ")
    home = input("Home: ")
    try:
        return Student(name, home)
    except ValueError:
        ...


if __name__ == "__main__":
    main()