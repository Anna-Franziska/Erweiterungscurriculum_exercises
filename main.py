def name_age():
    name = input("whats your name")
    age = input("whats your age")
    print("Hello", name, "Your age is:", age)
    return name, age



def swap_integers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1,num2


def check_numbers(num1, num2):
    if num1 % 10 != 0:
        return False
    if num2 % 10 != 0:
        return False
    if num1 % 6 == 0:
     return True
    if num2 % 6 == 0:
      return True
    else: return False


def sum_up(num1, num2):
    if num2 < num1:
        return 0
    if num1 < 0:
        return 0
    if num2 < 0:
        return 0
    return sum(range(num1,num2 +1))

def circle_area(r1,r2,r3):
    area1 = 3.14 * (r1*r1)
    area2 = 3.14 * (r2*r2)
    area3 = 3.14 * (r3*r3)
    return (float(area1 + area2 + area3))

def check_string(text):
     if text.startswith(("a", "A")):
         return True
     if text.endswith(("a", "A")):
         return True
     else:
         return False

def triangle(rows):
    x = rows
    for i in range(x):
        for j in range(i + 1):
            print ("*", end="")
        print("")



