# -*- coding: utf-8 -*-

import random


def generate(row,column):
    
    MainBoard=[]
    a=-1
    for i in range(row):
        board_row=[]
        for j in range(column):
            a+=1
            board_row.append(a)
        MainBoard.append(board_row)
    return MainBoard

def is_valid(board:list):
    number_of_rows=0
    for elem in board:
        number_of_rows+=1
    
    number_of_columns=len(elem)
    
    for row in board:
        for number in row:
            if row.count(number) > 1 or number  >= number_of_columns*number_of_rows or number < 0:
                print(number_of_rows)
                return False
    return True
   

def is_solved(board):
    a=0
    for row in board:
        for number in row:
            if number!=a:
                return False
            else:
                a+=1
    return True
                
def reset(board):
    a=0
    for row in board:
        index_row=board.index(row)
        for column in range(len(row)):
            board[index_row][column]=a
            a+=1
    return None     
def get_board_size(board):
    rows_count=0

    for row in board:
        rows_count+=1
    columns_count=len(row) 
    aTuple=(rows_count,columns_count)
    return aTuple
           


def print_board(board):

    for elem in board:
        for elem2 in elem:
            print(elem2,end="\t")
        print("\n")

def check_right(index_of_number ,row_with_number):
    
    if index_of_number < len(row_with_number)-1:
        return True
    else:
        return False
def check_left(index_of_number):
    
    if index_of_number >0:
        return True
    else:
        return False
def check_down(row_index , board):
        if row_index < len(board)-1:
            return True
        else:
            return False
def check_up(row_index):
        if row_index >0:
            return True
        else:
            return False
def move_right(board:list):
    rows_count=len(board)
    for row in range(rows_count):
        row_with_0= list(board[row]) if list(board[row]).__contains__(0) else None
        if row_with_0 != None:
            row_index=row
            break
    index_of_zero= row_with_0.index(0)
    if check_right(index_of_zero,row_with_0):
        row_with_0[index_of_zero],row_with_0[index_of_zero+1]=row_with_0[index_of_zero+1],row_with_0[index_of_zero]
        board[row_index]=row_with_0
        return 1
    else:
        return 0


def move_left(board:list):
    rows_count=len(board)
    for row in range(rows_count):
        row_with_0= list(board[row]) if list(board[row]).__contains__(0) else None
        if row_with_0 != None:
            row_index=row
            break
    index_of_zero= row_with_0.index(0)
    if check_left(index_of_zero) :
        row_with_0[index_of_zero],row_with_0[index_of_zero-1]=row_with_0[index_of_zero-1],row_with_0[index_of_zero]
        board[row_index]=row_with_0
        return 1
    else:
        return 0

def move_down(board:list):
    rows_count=len(board)
    for row in range(rows_count):
        row_with_0= list(board[row]) if list(board[row]).__contains__(0) else None
        if row_with_0 != None:
            row_index=row
            break
    index_of_zero= row_with_0.index(0)
    
    if check_down(row_index,board):
        down_row=board[row_index+1]

        row_with_0[index_of_zero],down_row[index_of_zero]=down_row[index_of_zero],row_with_0[index_of_zero]
        board[row_index]=row_with_0
        board[row_index+1]=down_row
        return 1
    else:
        return 0

def move_up(board:list):
    rows_count=len(board)
    for row in range(rows_count):
        row_with_0= list(board[row]) if list(board[row]).__contains__(0) else None
        if row_with_0 != None:
            row_index=row
            break
    index_of_zero= row_with_0.index(0)
    if check_up(row_index):
        up_row=board[row_index-1]

        row_with_0[index_of_zero],up_row[index_of_zero]=up_row[index_of_zero],row_with_0[index_of_zero]
        board[row_index]=row_with_0
        board[row_index-1]=up_row
        return 1
    else: 
        return 0


def move_random(board):
    rows_count=len(board)
    for row in range(rows_count):
        row_with_0= list(board[row]) if list(board[row]).__contains__(0) else None
        if row_with_0 != None:
            row_index=row
            break
    index_of_zero= row_with_0.index(0)
    moveList=[1,2,3,4]
    move_number=random.choice(moveList)
    if move_number ==1 and check_left(index_of_zero):
        move_left(board)

        return 'L'
    elif move_number==2 and check_right(index_of_zero,row_with_0):
        move_right(board)

        return 'R'

    elif move_number==3 and check_down(row_index,board):
        move_down(board)
        return 'D'

    elif move_number==4 and check_up(row_index):
        move_up(board)

        return 'U'
    
    else:
        return move_random(board)

def shuffle(board, times=20):
    moves_record=""
    for i in range(times):
        moves_record=moves_record+ move_random(board)
    if not is_solved():
        return moves_record
    else:
        return shuffle(board,times)
def move(board,moves:str):
    count_moves=0
    for move in moves:
        if move =='l' or move=='L':
            count_moves+=move_left(board)
        elif move =='r' or move=='R':
            count_moves+=move_right(board)
        elif move=='d' or move=='D':
            count_moves+=move_down(board)
        elif move=='u' or move =='U':
            count_moves+=move_up(board)
    return count_moves

def rotate(board):
    rows,columns=get_board_size(board)
    new_board=generate(columns,rows)
    
    new_column_index=-1
    for row in board:
        new_row_index=0 

        for i in range(len(row)):
            new_board[new_row_index][new_column_index]=row[i]
            new_row_index+=1
        new_column_index-=1
    return new_board
        

def play(board,moves):
    if not is_valid(board):
        return -2
    if is_solved(board):
        return 0
    moves_count=0    
    for ch in moves:
        moves_count+=move(board,ch)
        if is_solved(board):
            return moves_count
    return -1

def play_interactive(board=None):
    if board==None:
        print("Please type the puzzle size number.")
        row=int(input("Row number:"))
        column=int(input("Column number:"))
        board=generate(row,column)

        shuffle(board,20)

    if not is_valid(board):
        print("The board matrix elements must be between 0:1:row*column-1")
        return("''",-2)
    
    legal_moves=["l","L","r","R","U","u","d","D"]

    moves_string=""

    count_moves=0
    while True:
        print("Current board is:")
        print_board(board)

        if is_solved(board):
            print("Congrats! You solved the board in "+str(count_moves) +" moves.")
            return (moves_string,len(moves_string))
        
        move_input=input("Where do you want to move: ")
        if move_input=='Q' or move_input=="q":
            
            return (moves_string,-1) if is_solved(board)==False else 2
            
        if move_input=="M" or move_input=="m":
            moves_string=moves_string+ move_random(board)
            count_moves+=1
        elif move_input in legal_moves:
            play(board,move_input)
            moves_string=moves_string+move_input
        else:
            print("Wrong move.")



