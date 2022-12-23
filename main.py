file = open(r"C:\Users\Алема милашка\OneDrive\lessons\lessons\Data0.txt", 'r', encoding='utf-8')
a = file.read()
b = a.split(sep='\n')
index = [0]

first = [b[x] for x in index]
index2 = [2]
second = [b[x] for x in index2]
index3 = [3]
third = [b[x] for x in index3]
with open("1.txt", "w") as file:
    print(first, file=file)
with open("2.txt", "w") as file:
    print(second, file=file)
with open("3.txt", "w") as file:
    print(third, file=file)
