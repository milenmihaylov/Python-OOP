from project.teacher import Teacher

if __name__ == '__main__':
    math_teacher = Teacher()
    print(math_teacher.sleep())
    print(math_teacher.get_fired())

    print(Teacher.mro())