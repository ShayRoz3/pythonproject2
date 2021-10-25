def showEmployee(name, salary=9000):
    print("Employee", name, "salary is", salary)


showEmployee("Shay", 9000)
showEmployee("shay")

def func1(*args):
    for i in args:
        print(i)
func1(20, 40, 60)
func1(80, 100)

def demo(name, age):
    print(name, age)
demo("Shay", 25)

#example1
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('shay')

#exercise1
def greet(given_name, surname, age):
    print('Hello', given_name, surname, 'you are', age, 'years old')
    print("you're initials are: ")
    print(given_name[0]+surname[0], age)

greet('Rachel','Rozner', 55)

#1.2
my_string = "{} rely on {} datasets"
method = "Supervised algorithms"
condition = "labeled"
print(my_string.format(method, condition))

def check(*args):
    for i in args:
        print(i)
check("a","b","c","aaaa")

#yield?

def yeah_you_can(str):
    for l in str:
        print(l)

yeah_you_can("go willld")
#def to print each character