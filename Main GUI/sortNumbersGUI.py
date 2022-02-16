# @Author: Blake Stephenson
# @Date: 2022-1-29

import turtle
from tkinter import *
from diagram import DData as Data
from diagram import DVenn as Venn
import tools



def main():
    root = Tk()
    root.title("Venn Prime")
    # Dimentions of window
    x = 600
    y = 600
    root.geometry(f"{x}x{y}")

    canvas= Canvas(root, width=x, height=y-80)
    canvas.place(x=0, y=80)
    t = turtle.RawTurtle(canvas)
    t.hideturtle()

    # show heading
    heading = Label(root, text="Enter Data separated by spaces")
    heading.place(x=0, y=0, width=x, height=20)
    # show data input box
    get_data = Entry(root, width=80)
    get_data.place(x=0, y=20, width=x, height=20)
    # show display box
    data_box = Label(root, text="")
    data_box.place(x=0, y=40, width=x, height=20)

    def two_groups(text_label):
        nums = []
        try:
            data = get_data.get().strip(" ").split(" ")
            nums = [int(num) for num in data]
        except:
            pass

        diagram = Data.DData(2, nums, t)
        text_label['text'] = "Data: ", str(diagram.getLabeledData())
        venn_diag = Venn.DVenn(diagram)
        venn_diag.show()

    def three_groups(text_label):
        data = []
        try:
            data = [int(num) for num in get_data.get().strip(" ").split(" ")]
        except:
            pass

        diagram = Data.DData(3, data, t)
        text_label['text'] = "Data: ", str(diagram.getLabeledData())
        venn_diag = Venn.DVenn(diagram)
        venn_diag.show()

    def four_groups(text_label):
        data = []
        try:
            data = [int(num) for num in get_data.get().strip(" ").split(" ")]
        except:
            pass

        diagram = Data.DData(4, data, t)
        text_label['text'] = "Data: ", str(diagram.getLabeledData())

    button2 = Button(root, text="Two Groups", command=lambda: two_groups(data_box))
    button3 = Button(root, text="Three Groups", command=lambda: three_groups(data_box))
    button4 = Button(root, text="Four Groups", command=lambda: four_groups(data_box))

    button2.place(x=0, y=60, width=x / 3, height=20)
    button3.place(x=x / 3, y=60, width=x / 3, height=20)
    button4.place(x=x * 2 / 3, y=60, width=x / 3, height=20)

    root.mainloop()


if __name__ == '__main__':
    main()
