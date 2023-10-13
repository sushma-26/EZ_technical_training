''' for achiving obj we need to put class child(parent class name)
polymorphism ==what ever is at last that will be executed this method is method overriding
encapsulation eg:class all related mthods variables are grouped together
abstraction cant be achived using python we should use abc module
hiding internal working
'''
class parent:
    def fun(s):
        print("parent")
    def fun2(s):
        print("grand child")
class child(parent):
    def fun1(s):
        super() #super will give access to parent class
        print("child")
class gchild(child):
    def fun2(s):
        print("grand child")
class multiple(child,parent):
    def fun3(s):
        print("multiple")
o=parent()
o.fun()
c=child()
c.fun1()
c.fun()