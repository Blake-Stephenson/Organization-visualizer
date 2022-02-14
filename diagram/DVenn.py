import turtle
from diagram import DData as Diag

class DVenn:
    boxes = [[]]
    labels = []
    size = 0

    def __init__(self, d: Diag):
        self.boxes = d.getBoxes()
        self.labels = d.getLabels()
        self.data = d.getData()
        self.size = len(self.labels)