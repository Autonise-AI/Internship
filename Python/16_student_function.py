from student import Student


def take_input():
    lst = []
    n = int(input("give number: "))
    for i in range(n):
        name = input("give name: ")
        age = int(input("give age: "))
        marks = int(input("marks: "))
        s = Student(name, age, marks)
        lst.append(s)
    return lst


def func(x):
    return x.marks


def fill(x):
    # function to filter
    return x.marks < 50


# def map_func(x):
#     print("here")
#     x.greet()
#  map function is not very useful for this usecase


def maxStudent(lst):
    # return the object of student with max marks
    s = max(lst, key=func)
    return s


def filterStudents(lst):
    # return the list of students with marks less than 50
    # filtered = []
    # for l in lst:
    #     if l.marks < 50:
    #         filtered.append(l)

    # using inbuilt filter function
    filtered = filter(fill, lst)
    return filtered


def greetAll(x):
    # map function is not required
    # code with for loop
    for l in x:
        l.greet()


def main():
    # if u ar taking input from user
    # lst = take_input()
    lst = [Student("ben", 20, 25), Student(
        "gwen", 30, 35), Student("alice", 19, 55)]
    s = maxStudent(lst)
    # greet the winner
    s.greet()
    filtered = list(filterStudents(lst))
    # filtered is list of filtered student objects
    greetAll(filtered)


if __name__ == "__main__":
    main()
