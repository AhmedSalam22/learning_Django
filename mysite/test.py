num = 1 

def function():
    global num
    num = 5
    return num

print(function())
print(num)
