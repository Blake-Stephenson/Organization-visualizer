# @Author: Blake Stephenson
# @Date: 2022-1-28

def getNums():
    """ask for ints from terminal and returns them as int array"""

    nums = []
    line = input("Type numbers seperated by spaces: ")
    line = line.strip(" ").split(" ")
    for i in line:
        try:
            nums.append(int(i))
        except ValueError:
            print("only input integers")
            return getNums()
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


def getPrime(n: int):
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


class diagram():
    allNums = []
    boxes = [[]]
    labels = []

    def __init__(self, containers):
        self.boxes = [[]] * containers
        self.labels = getPrime(containers)

    def addNums(self, nums):
        self.allNums = nums
        for j in range(len(self.labels)):
            label = self.labels[j]
            group = []
            for num in nums:
                if num % label == 0:
                    #if i not in self.boxes[j]:
                    group.append(num)
            self.boxes[j]=group

    def getLabeledData(self):
        labeledData = []
        for i in self.allNums:
            label=""
            for j in self.labels:
                if i%j==0:
                    label+=str(j)
            labeledData.append((i,label))
        return labeledData

    def getData(self):
        return self.allNums

    def getBoxes(self):
        return self.boxes

    def getGroups(self):
        return self.labels

def main():
    # get nums and groups
    nums = getNums()
    groups = getGroups()



    # group must be > 1

    diagram1 = diagram(groups)
    diagram1.addNums(nums)

    data = diagram1.getBoxes()
    labels = diagram1.getGroups()

    for i in range(len(data)):
        print(labels[i], data[i])

    print(diagram1.getLabeledData())



if __name__ == '__main__':
    main()
