class OrderedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderedList(object):
    def __init__(self):
        self.__head = None
        self.__count = 0

    def add(self, item):
        if self.__head == None:
            self.__head = OrderedListNode(item)
        else:
            current = self.__head
            previous = None
            done = False
            new_node = OrderedListNode(item)
            while not done:
                if current is None:
                    done = True
                else:
                    if current.data > item:
                        done = True
                    else:
                        previous = current
                        current = current.next

            if previous is None:
                new_node.next = self.__head
                self.__head = new_node
            else:
                previous.next = new_node
                new_node.next = current
        self.__count += 1

    def remove(self, item):
        done = False
        current = self.__head
        previous = None
        while not done:
            if current is None:
                print("Couldn't find item '{0}'".format(item))
                done = True
            else:
                if item == current.data:
                    self.__count -= 1
                    if previous is None:
                        self.__head = current.next
                    else:
                        previous.next = current.next
                    done = True
                else:
                    previous = current
                    current = current.next

    def search(self, item):
        found = False
        current = self.__head
        while current is not None:
            if item == current.data:
                found = True
                break
            else:
                current = current.next
        return found

    def is_empty(self):
        return True if self.size() == 0 else False

    def size(self):
        return self.__count

    def pop(self):
        done = False
        current = self.__head
        if self.is_empty():
            return

        if self.size() == 1:
            temp = self.__head.data
            self.__head = None
            self.__count -= 1
            return temp
        else:
            while current.next.next is not None:
                current = current.next
            temp = current.next.data
            current.next = None
            self.__count -= 1
            return temp

    def clear(self):
        self.__head = None
        self.__count = 0

    def __str__(self):
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(current.data)
            current = current.next
        return str(nodes)
