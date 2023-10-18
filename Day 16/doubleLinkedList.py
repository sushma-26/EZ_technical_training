#(int(s,2)) binary string is converted to decimal
class node:
    def __init__(self,val=0):
        self.val=val
        self.prev=None
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_end(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
    def insert_begin(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def delete_beg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    def delete_end(self):
        if self.head==None:
            return
        self.tail = self.tail.prev
        self.tail.next = None
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end="->")
            temp=temp.next
    def reverse(self):
        curr=self.head
        p=None
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.tail=self.tail,self.head
        
o = Linkedlist()
l = [1, 2, 3, 4, 5]
for i in l:
    o.insert_begin(i)
o.printing()
print()
'''for i in l:
    o.insert_end(i)
o.printing()
o.delete_beg()
o.printing()
print()
o.delete_end()
o.printing()'''
print()
o.reverse()
o.printing()