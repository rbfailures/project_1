from GUI import *


def GPA(grades):
    gradepoints = []
    average = 0.0
    for grade in grades:
        if grade >= 90:
            gradepoints.append(4.0)
        elif 90 < grade >= 80:
            gradepoints.append(3.0)
        elif 80 < grade >= 70:
            gradepoints.append(2.0)
        elif 70 < grade >= 60:
            gradepoints.append(1.0)
        elif grade < 60:
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
