###############
# Tic tac toe #
###############

def create_board():    
    global A
    A = [['','',''],
         ['','',''],
         ['','','']]
    return A 

def insert(element, row, column):
    try:
        if element == 'o':
            A[row][column]='o'
        elif element == 'x':
            A[row][column]='x'
        else:
            print("Input error")
        return A
    finally:
        show_board()

def show_board():
    for row in A:
        print(row) 


# Example Usage:
create_board()
show_board()

insert('o',0,0)
insert('x',1,1)

insert('o',1,2)
insert('x',2,2)

insert('o',1,0)
insert('x',2,0)

insert('o',2,1)
insert('x',0,2)

