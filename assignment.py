# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    if line_number<=0:
        return ""
    file = open(filename,"r")
    lst = file.readlines()
    line=""
    if line_number>len(lst):
        return ""
    else:
        for i in range(line_number):
            line=lst[i]
    return lst[line_number - 1].rstrip("\n")
    file.close()
    pass

# Exercise 2
def reverse_lines(source, destination):
    file = open(source,"r")
    lst = file.readlines()
    file.close()
    file1 = open(destination,"w")
    c=0
    for i in range(len(lst)-1,-1,-1):
        file1.write(f"{lst[i]}")
        c+=1
    file1.close()
    return c
    pass

# Exercise 3
def merge_files(first, second, destination):
    file = open(first,"r")
    lst = file.readlines()
    file.close()
    file1 = open(second,"r")
    lst1 = file1.readlines()
    file1.close()
    file2 = open(destination,"w")
    for i in range(len(lst)):
        file2.write(f"{lst[i]}")
    file2.close()
    file2 = open(destination,"a")
    for i in range(len(lst1)):
        file2.write(f"{lst1[i]}")
    file2.close()
    pass

# Exercise 4
def find_score(filename, name):
    # Write your code here
    pass

# Exercise 5
def update_score(filename, name, new_score):
    # Write your code here
    pass
