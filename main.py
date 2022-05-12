from GUI import *


def GPA(grades):
    gradepoints = []
    average = 0.0
    for grade in grades:
        if grade >= 93:
            gradepoints.append(4.0)
        elif 93 > grade >= 90:
            gradepoints.append(3.7)
        elif 90 > grade >= 87:
            gradepoints.append(3.3)
        elif 87 > grade >= 83:
            gradepoints.append(3.0)
        elif 83 > grade >= 80:
            gradepoints.append(2.7)
        elif 80 > grade >= 77:
            gradepoints.append(2.3)
        elif 77 > grade >= 73:
            gradepoints.append(2.0)
        elif 73 > grade >= 70:
            gradepoints.append(1.7)
        elif 70 > grade >= 67:
            gradepoints.append(1.3)
        elif 67 > grade >= 63:
            gradepoints.append(1.0)
        elif 63 > grade >= 60:
            gradepoints.append(0.7)
        elif 60 > grade:
            gradepoints.append(0.0)
    for point in gradepoints:
        average += point
    average = average / len(grades)
    return average


def main() -> None:
    window = Tk()
    window.title('GPA Calculator')
    window.geometry('350x280')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
