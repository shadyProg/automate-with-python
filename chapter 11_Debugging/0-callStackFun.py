def func1():
    print("func1")
    func2()

def func2():
    print("func2")
    func3()

def func3():
    print("func3")

def func1_1():
    
    func2_2()
    print("func1")

def func2_2():
    
    func3_3()
    print("func2")

def func3_3():
    print("func3")

print("Calling func1:")
func1_1()
print("\nCalling func1_1:")
func1_1()