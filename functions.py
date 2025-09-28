def strength(password):
    upper=False
    digit=False
    for i in password:
        if i.isupper()==True:
            upper=True
        elif i.isdigit()==True:
            digit=True
        else:
            pass
    if len(password)>8 and upper==True and digit==True:
        return ("Strong Password")
    else:
        return ("Weak Password")

def read_file():
    with open("/Users/garvitagangwal/Desktop/Python Projects/to-do list/todoss/todos.txt", "r") as file:
        todos=file.readlines()
        return todos
        
def write_files(todoss):
    with open("/Users/garvitagangwal/Desktop/Python Projects/to-do list/todoss/todos.txt", "w") as file:
        file.writelines(todoss)
        return todoss