class stack:
    # need to 1 parameter pass for funcrion call no mater you are passing argument
    # constructor function 
    def __init__(self):
        self.arr=[]
    def pop(self):
        print("This is pop method", id(self))
        return self.arr.pop()        # arr.re 
    def push(self, number):
        self.arr.append(number)
        print(f"push method is {number}", id(self))
    def printf(self):
        print(self.arr)
    def empty(self):
        if len(self.arr)==0:
            print("Array is Empty")
        else:
            print("Not Empty ")
    def size(self):
        print(f"size of array is {len(self.arr)}")
    def top(self):
        print(f"top of elemet is {self.arr[len(self.arr)-1]}")
        
s1=stack()
s2=stack()
s1.push(12)
s1.push(22)
s2.push(11)
s2.push(33)
# s1.printf()
# s2.printf()
s1.empty()
s1.top()
s1.size()
# print("id of s1 =", id(s1))
# print("id of s2 =", id(s2))
# s2.pop()
# s1.pop()
