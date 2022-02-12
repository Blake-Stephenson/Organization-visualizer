# @Author: Blake Stephenson
# @Date: 2022-2-11

class Diagram():
    allNums = []
    boxes = [[]]
    labels = []

    def __init__(self, containers, nums):
        self.allNums = nums
        self.boxes = [[]] * containers
        self.labels = self.get_prime(containers)
        self.addNums()


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

    def get_prime(self, n: int):
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