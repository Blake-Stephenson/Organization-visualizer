# @Author: Blake Stephenson
# @Date: 2022-1-29

from tkinter import *
import Diagram as Diag
from turtle_graphics import circle_venn_2 as V2
from turtle_graphics import circle_venn_3 as V3


def get_nums():
    """ask for ints from terminal and returns them as int array"""

    nums = []
    line = input("Type numbers seperated by spaces: ")
    line = line.strip(" ").split(" ")
    for i in line:
        try:
            nums.append(int(i))
        except ValueError:
            print("only input integers")
            return get_nums()
    else:
        return nums


def getGroups() -> int:
    """asks for an int and returns it"""

    line = input("How many groups do you want: ")
    line.strip(" ")
    try:
        line = int(line)
    except ValueError:
        print("only input integers")
        return getGroups()
    else:
        return line



def main():
    root = Tk()

    heading = Label(root, text="Enter Data separated by spaces")
    heading.grid(row=0, columnspan=3)
    get_data = Entry(root, width=80)
    get_data.grid(row=1, columnspan=3)
    data_box = Label(root, text="")
    data_box.grid(row=3, columnspan=3)

    def two_groups(text_label):
        nums = []
        try:
            data = get_data.get().strip(" ").split(" ")
            nums = [int(num) for num in data]
        except:
            pass

        diagram = Diag.Diagram(2,nums)
        text_label['text'] = "Data: " ,str(diagram.getLabeledData())
        vennDiag = V2.Venn2(diagram)
        vennDiag.printD()


    def three_groups(text_label):
        data = []
        try:
            data = [int(num) for num in get_data.get().strip(" ").split(" ")]
        except:
            pass

        diagram = Diag.Diagram(3, data)
        text_label['text'] = "Data: " ,str(diagram.getLabeledData())

    def four_groups(text_label):
        data = []
        try:
            data = [int(num) for num in get_data.get().strip(" ").split(" ")]
        except:
            pass

        diagram = Diag.Diagram(4, data)
        text_label['text'] = "Data: ", str(diagram.getLabeledData())

    button2 = Button(root, text="Two Groups", padx=80, command=lambda: two_groups(data_box))
    button3 = Button(root, text="Three Groups", padx=80, command=lambda: three_groups(data_box))
    button4 = Button(root, text="Four Groups", padx=80, command=lambda: four_groups(data_box))

    button2.grid(row=2, column=0)
    button3.grid(row=2, column=1)
    button4.grid(row=2, column=2)

    root.mainloop()


if __name__ == '__main__':
    main()
