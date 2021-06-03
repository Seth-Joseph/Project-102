# I think the most time consuming part is downloading source file or code from internet...So here is the solution
from urllib import request

file_url = input(r"Enter Download link :")

def downloading_file(url):
    file_open = request.urlopen(url)
    file_info = file_open.read()
    file_open_str = str(file_info)
    file_lines = file_open_str.split('\\n')
    new_file = open('d.txt',"w")
    
    for i in file_lines:
        new_file.write(i + '\n')
    new_file.close()
    
downloading_file(file_url)

