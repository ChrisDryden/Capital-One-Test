import os

#Additional filetypes can be added by adding the file extensions
# filetype | single line comment | multiline begin | multiline end 
filetype = {
    ".py": ["#", '"""', '"""'],
    ".java": ["//", '/*', '*/'],
}

def countTodo(file):
    return str(sum([1 for line in file if "TODO" in line]))

def count_comments(file, extension):
    return str(sum([1 for line in file if filetype[extension][0] in line ]))


def multilineComments(file, extension):
    comment = False
    total, swaps = 0, 0
    for line in file:
        if comment or line.count(filetype[extension][1])+line.count(filetype[extension][2]) > 1:
            total += 1
        if line.count(filetype[extension][1]) % 2 == 1 and line.count(filetype[extension][2]) % 2 == 1:
            comment = not comment
            swaps += 1
    return total, str(swaps)

def countLines(file, extension):
    return str(sum([1 for line in file if not line.strip().startswith(filetype[extension][0])])
            - multilineComments(file, extension)[0])

#Iterates through every file in folder
#If file has known extension, runs above functions on list of file lines
path = os.getcwd()
for root, dirs, files in os.walk(path):
    for file in files:
        extension = "." + file.split(".")[-1]
        if extension in filetype.keys():
            filename = os.path.join(root, file)
            f = open(filename)
            opened_file = f.readlines()

            print("File: " + file)
            print("Total Lines of Code: " + countLines(opened_file, extension))
            print("Total TODO's: " + countTodo(opened_file))
            print("Total Single Line Comments: " + count_comments(opened_file, extension))
            print("Total Multiline Comment Lines: " + str(multilineComments(opened_file, extension)[0]))
            print("Total Multiline Comment Blocks: " + multilineComments(opened_file, extension)[1])



