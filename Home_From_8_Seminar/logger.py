from datetime import datetime

def log_to_file(entry):  
    
    with open('base.csv', 'a') as file:
        file.write(
            f'{entry[0]} {entry[1]} {entry[2]} {entry[3]}\n')    

def reading_file(param): 
        list = []
        with open('base.csv', 'r') as file:
            for line in file:
                if param in line:
                    list = line.split(";")
                    print(f'{list[0]} {list[1]} {list[2]} {list[3]}')                       

def read_all_file(): 
        with open('base.csv', 'r') as file:
            for line in file:
                print(line)