class Node(object):
    def __init__(self, data):
        super(Node, self).__init__(data)
        self.data = data


class LinkedList(object):
    def __init__(self, ):
        super(LinkedList, self).__init__()
        self.headd = None
        self.size = 0

    # O(1)
    def InsertAtStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size(self):
        return self.size
