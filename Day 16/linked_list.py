#(int(s,2)) binary string is converted to decimal
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            cur=self.head
            while(cur.next):
                cur=cur.next
            new=node(data)
            cur.next=new
    def insert_begin(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def delete_begin(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.val
    def delete_end(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=None
        return temp.val
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end="->")
            temp=temp.next
    def reverse(self):
        
l = [5, 2, 8, 45, 21]
o = Linkedlist()
for i in l:
    o.insert_begin(i)
o.printing()
print()
print(o.delete_begin())
print(o.delete_end())
'''
o1=node(2)
o2=node(6)
o1.next=o2
print(o1)#memory location of object
print(o1.val,o2.val)
print(o1.next,o2.next)'''