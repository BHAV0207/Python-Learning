def hello(name , game) :
    print("hello , world")
    print("Hello, " + name + "!")
    print("I like to play " + game)
    return
def inputt() :
    name = input("What is your name? ")
    print("Hello, " + name + "!")
    number = input("What is your favorite number? ")
    print (int(number) + 6)
    return


hello("bhav" , "cricket")
inputt()
#  in python the input default is srintg so we need to convert it to int for math operations
#  in python string are immutable when we try to change the value of a string it will create a new string