class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
    

    def forward_traversal(self):
        if self.head == None:
            print("cant front travesal,its empty")
        else:
            n = self.head
            while n:
                print(n.data,"-->",end="")
                n = n.ref
    
    def backward_traversal(self):
        if self.head == None:
            print("cant back traversal,its empty")
        else:
            prev = None
            curent = self.head
            while curent:
                next = curent.ref
                curent.ref = prev
                prev = curent
                curent = next
            
            self.head = prev
            n = self.head
            while n:
                print(n.data,"-->",end="")
                n = n.ref
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref:
                n = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        new_node = Node(data)
        if self.head == None:
            print("its empty,cant add before")
        elif self.head.data == x:
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            found = False
            while n.ref:
                if n.ref.data == x:
                    found = True
                    break
                n = n.ref
            if found:
                new_node.ref = n.ref
                n.ref = new_node
            else:
                print("specified value not found")

    def add_after(self,data,x):
        new_node = Node(data)
        if self.head == None:
            print("cant add after,its empty")
        elif self.head.data == x and self.head.ref == None:
            self.head.ref = new_node
        elif self.head.data == x and self.head.ref != None:
            new_node.ref = self.head.ref
            self.head.ref = new_node
        else:
            n = self.head
            found = False
            while n.ref:
                if n.ref.data == x:
                    found = True
                    break
                n = n.ref
            
            if found:
                new_node.ref = n.ref.ref
                n.ref.ref = new_node
            else:
                print("specified item not found")

    def delete_begin(self):
        if self.head == None:
            print("cant delete,it already empty")
        else:
            self.head = self.head.ref
    
    def delete_end(self):
        if self.head == None:
            print("cant delete,it already empty")
        elif self.head and self.head.ref == None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref:
                n = n.ref
            n.ref = None

    def delete_by_specified_value(self,x):
        if self.head == None:
            print("cant delete,it already empty")
        elif self.head.data == x and self.head.ref == None:
            self.head = None
        elif self.head.data == x and self.head.ref != None:
            self.head = self.head.ref
        else:
            n = self.head
            found = False
            while n.ref:
                if n.ref.data == x:
                    found = True
                    break
                n = n.ref
            if found:
                n.ref = n.ref.ref
            else:
                print("specified value not found")

    def find_sum_average_count(self):
        if self.head == None:
            print("cant operate,its empty")
        else:
            sum = 0
            count = 0
            n = self.head
            while n:
                sum += n.data
                count += 1
                n = n.ref
            avg = sum/count
            print(f"sum is {sum},average is {avg},count is {count}")

               

sll = SingleLinkedList()
sll.add_begin(10)
sll.add_begin(15)
sll.add_after(12,15)
# sll.add_before(11,15)
sll.delete_by_specified_value(17)
# sll.delete_by_specified_value(10)
sll.forward_traversal()
print()
sll.backward_traversal()
print()
sll.find_sum_average_count()


