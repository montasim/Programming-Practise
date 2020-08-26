file1 = open("montasim.txt", "wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("this is inside a file", "UTF-8"))
file1.close()

file1 = open('montasim.txt', 'r+')
file1Text = file1.read()
print(file1Text)
