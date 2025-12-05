squares = [x**2 for x in range(1,10)]
print(squares)

evens =  [x for x in range(1,21) if x % 2 == 0]
print(evens)

name = ["robeen", "alice", "bob", "charlie"]
uppercase_names = [n.upper() for n in name]
print(uppercase_names)

matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
print(matrix)

numbers = [1, 2, 3, 4, 5]
result = ["Even " if x % 2 == 0 else "Odd" for x in numbers]
print(result)