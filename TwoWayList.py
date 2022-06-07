from Node import Node


class TwoWayList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenth = 0

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.lenth == 0:
            node = Node(item)
            self.head = node
            self.tail = node
            self.lenth = 1
            return
        node = Node(item)
        tail = self.tail
        tail.next = node
        node.prev = tail
        self.tail = node
        self.tail = node
        self.lenth += 1

    def deleteNode(self, index):
        if index >= 0 and index <= self.lenth:
            cur = self.head
            if index == 0:
                toDelete = cur
                cur.setData(toDelete.getNext())
                cur.setPrev(self.tail)
            else:
                for i in range(index - 1):
                        cur = cur.getNext()
                
                toDelete = cur.getNext()
                cur.setNext(toDelete.getNext())
                toDelete.setPrev(cur)

    def insert(self, index, item):
        length = self.length
        if (index<0 and abs(index)>length) or (index>0 and index>=length):
            return False
        if index < 0:
            index = index + length
        if index == 0:
            node = Node(item)
            if self.head != None:
                self.head.prev = node
            else:
                self.tail = node
            node.next = self.head
            self.head = node
            self.length += 1
            return True
        if index == length - 1:
            return self.append(item)

        node1 = self.head
        for i in range(0, index):
            node1 = node1.next
        node2 = node1.next

        node = Node(item)
        node.prex = node1
        node.next = node2
        node1.next = node
        node2.prev = node

        self.length += 1
        return True

    def sortListByNom(self):    
        if(self.head == None):    
            return;    
        else:    
            current = self.head    
            while(current.next != None):    
                next = current.next;    
                while(next != None):    
                    if(current.data.nom > next.data.nom):    
                        temp = current.data;    
                        current.data = next.data;    
                        next.data = temp;    
                    next = next.next    
                current = current.next    
    
    def sortListByType(self):    
        if(self.head == None):    
            return;    
        else:    
            current = self.head    
            while(current.next != None):    
                next = current.next;    
                while(next != None):    
                    if(current.data.type > next.data.type):    
                        temp = current.data;    
                        current.data = next.data;    
                        next.data = temp;    
                    next = next.next    
                current = current.next    

    def show(self):
        cur = self.head
        while cur:
            data = cur.getData()
            data.show()
            cur = cur.getNext()

    def showByAccuracy(self, accuracy):
        cur = self.head
        while cur:
            data = cur.getData()
            if data.accuracy <= accuracy:
                data.show()
            cur = cur.getNext()


            