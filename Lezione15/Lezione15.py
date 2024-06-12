file = open("file_txt.txt")
try:
    pass #actions on file_txt.txt
finally:
    file.close

with open ("file_txt.txt") as reader:
    pass #actions on file_txt.txt
