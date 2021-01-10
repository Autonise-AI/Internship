class Student:
    # attributes/fields
    name = None
    age = None
    marks = None

    # constructor
    def __init__(self, n, a, m):
        self.name = n
        self.age = a
        self.marks = m

    # method
    def greet(self):
        print("hello, ", self.name)


def main():
    # instances of the class
    s1 = Student("alice", 20, 95)
    s2 = Student("bob", 19, 80)
    s1.greet()
    s2.greet()


if __name__ == "__main__":
    main()
