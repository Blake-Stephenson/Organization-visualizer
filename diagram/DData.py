# @Author: Blake Stephenson
# @Date: 2022-2-11

class DData:
    data = []
    boxes = [[]]
    labels = []


    def __init__(self, containers, nums, t):
        self.data = nums
        self.boxes = [[]] * containers
        self.labels = self.get_prime(containers)
        self.addNums()
        self.t = t

    def addNums(self):
        for j in range(len(self.labels)):
            label = self.labels[j]
            group = []
            for num in self.data:
                if num % label == 0:
                    # if i not in self.boxes[j]:
                    group.append(num)
            self.boxes[j] = group

    def getLabeledData(self):
        labeledData = []
        for i in self.data:
            label = ""
            for j in self.labels:
                if i % j == 0:
                    label += str(j)
            labeledData.append((i, label))
        return labeledData

    def getData(self):
        return self.data

    def getBoxes(self):
        return self.boxes

    def getLabels(self):
        return self.labels

    def getT(self):
        return self.t

    def get_prime(self, n: int):
        """returns first n primes"""

        nums = []
        index = 1
        while len(nums) < n+1:
            prime = True
            for i in range(2, int(index ** 0.5) + 1):
                if i != index and index % i == 0:
                    prime = False
                    break
            if prime and index not in nums:
                nums.append(index)
            index += 1

        return nums[1:]