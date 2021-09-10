file1 = str(input("Enter the name of the first file: "))
file2 = str(input("Enter the name of the second file: "))
def readFiles():
    with open (str(file1), "r") as a:
        data_a = a.read()
    with open (str(file2), "r") as b:
        data_b = b.read()
readFiles()
def changeData():
    with open (str(file1), "w") as c:
        c.write(data_b)
    with open (str(file2), "w") as d:
        c.write(data_a)
changeData()
