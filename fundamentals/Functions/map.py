
# capitalize each name
names = ["alice", "bob", "charlie", "david"]
capital = list(map(lambda x: x.upper(), names))
print(capital)  # Output: ['Alice', 'Bob', 'Charlie', 'David']


#  square each number
numbers = [2, 5, 8, 10]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [4, 25, 64, 100]