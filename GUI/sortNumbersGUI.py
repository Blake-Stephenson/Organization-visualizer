# @Author: Blake Stephenson
# @Date: 2022-1-29

from tkinter import *


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


def get_prime(n: int):
    """returns first n primes"""

    nums = []
    index = 1
    while len(nums) < n:
        prime = True
        for i in range(2, int(index ** 0.5) + 1):
            if i != index and index % i == 0:
                prime = False
                break
        if prime and index not in nums:
            nums.append(index)
        index += 1

    return nums


class Diagram():
    allNums = []
    boxes = [[]]
    labels = []

    def __init__(self, containers, nums):
        self.allNums = nums
        self.addNums()
        self.boxes = [[]] * containers
        self.labels = get_prime(containers)

    def addNums(self):
        for j in range(len(self.labels)):
            label = self.labels[j]
            group = []
            for num in self.allNums:
                if num % label == 0:
                    # if i not in self.boxes[j]:
                    group.append(num)
            self.boxes[j] = group

    def getLabeledData(self):
        labeledData = []
        for i in self.allNums:
            label = ""
            for j in self.labels:
                if i % j == 0:
                    label += str(j)
            labeledData.append((i, label))
        return labeledData

    def getData(self):
        return self.allNums

    def getBoxes(self):
        return self.boxes

    def getGroups(self):
        return self.labels


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

        diagram = Diagram(2,nums)
        text_label['text'] = "Data: " ,str(diagram.getLabeledData())


    def three_groups(text_label):
        data = []
        try:
            data = [int(num) for num in get_data.get().strip(" ").split(" ")]
        except:
            pass

        diagram = Diagram(3, data)
        text_label['text'] = "Data: " ,str(diagram.getLabeledData())

    def four_groups(text_label):
        data = []
        try:
            data = [int(num) for num in get_data.get().strip(" ").split(" ")]
        except:
            pass

        diagram = Diagram(4, data)
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
