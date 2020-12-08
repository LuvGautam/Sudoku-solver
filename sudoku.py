#Project : Sudoku Solver

from collections import defaultdict

#taking input from user
def user_input():

    #defining 2d array of size 9x9
    grid = [ [0 for j in range(9)] for i in range(9) ]

    
    grid = [
        [9, 6, 0, 0, 4, 0, 1, 0, 0],
        [0, 0, 0, 3, 8, 0, 0, 0, 0],
        [7, 0, 8, 0, 6, 0, 0, 0, 9],
        [1, 2, 0, 8, 0, 0, 9, 0, 3],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [3, 0, 5, 0, 0, 2, 0, 6, 4],
        [8, 0, 0, 0, 9, 0, 4, 0, 7],
        [0, 0, 0, 0, 3, 8, 0, 0, 0],
        [0, 0, 9, 0, 2, 0, 0, 8, 5]
        ]
    
    '''
    for i in range(9):
        grid[i] = [ int(num) for num in input(f'Row {i+1} : ').split() ]
    '''
    
    return grid
    

#displaying formatted grid
def display(grid):
    print()
    for i,row in enumerate(grid):
        print(' ', end='')
        if i == 3 or i == 6:
            print('-'*20)
            print(' ',end='')
            
        for j,item in enumerate(row):
            if item == 0:
                if j==2 or j==5:
                    print('  |', end='')
                else:
                    print('  ', end='')
            else:
                if j==2 or j==5:
                    print(f' {item}|', end='')
                else:
                    print(f' {item}', end='')
                
        print()


#dividing grid
def divide(grid):

    dict_section = {
        'section1' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'section2' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'section3' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'section4' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'section5' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'section6' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'section7' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'section8' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'section9' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        }

    dict_row = {
        'row1' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'row2' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'row3' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'row4' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'row5' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'row6' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'row7' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'row8' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'row9' : {
            'given' : {},  'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        }

    dict_col = {
        'col1' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'col2' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'col3' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'col4' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'col5' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'col6' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'col7' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'col8' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        
        'col9' : {
            'given' : {}, 'missing' : [], 'available_pos' : [],
            'all_pos' : [], 'all_fill' : False
            },
        }


    #finding given digits and available positions in each section, row and col

    #given digits
    def given_sec(flag, i, j, item, sec):
        sec = 'section' + str(sec)

        if flag:
                if item != 0:
                    dict_section[sec]['given'][item] = (i, j)
                else:
                    dict_section[sec]['available_pos'].append( (i, j) )

    def given_row(i, j, item):
        row = 'row' + str(i+1)
        
        if item != 0:
            dict_row[row]['given'][item] = (i, j)
        else:
            dict_row[row]['available_pos'].append( (i, j) )

    def given_col(i, j, item):
        col = 'col' + str(j+1)
        
        if item != 0:
            dict_col[col]['given'][item] = (i, j)
        else:
            dict_col[col]['available_pos'].append( (i, j) )

    for i, row in enumerate(grid):
        
        for j, item in enumerate(row):

            #for sections

            given_sec(0 <= i < 3 and 0 <= j < 3, i, j, item, 1)
            given_sec(0 <= i < 3 and 3 <= j < 6, i, j, item, 2)
            given_sec(0 <= i < 3 and 6 <= j < 9, i, j, item, 3)
            given_sec(3 <= i < 6 and 0 <= j < 3, i, j, item, 4)
            given_sec(3 <= i < 6 and 3 <= j < 6, i, j, item, 5)
            given_sec(3 <= i < 6 and 6 <= j < 9, i, j, item, 6)
            given_sec(6 <= i < 9 and 0 <= j < 3, i, j, item, 7)
            given_sec(6 <= i < 9 and 3 <= j < 6, i, j, item, 8)
            given_sec(6 <= i < 9 and 6 <= j < 9, i, j, item, 9)
        

            #for rows

            given_row(i, j, item) 


            #for columns
            
            given_col(i, j, item)


    #finding missing digits in each section, row and column
    
    #for section
    def missing_sec(sec, num):
        if num not in dict_section[sec]['given'].keys():
            dict_section[sec]['missing'].append(num)

    #for row
    def missing_row(row, num):
        if num not in dict_row[row]['given'].keys():
            dict_row[row]['missing'].append(num)       

    #for column
    def missing_col(col, num):
        if num not in dict_col[col]['given'].keys():
            dict_col[col]['missing'].append(num)

    for num in range(1, 10):
        
        for i in range(1, 10):
            col_name = 'col' + str(i)
            missing_col(col_name, num)

            sec_name = 'section' + str(i)
            missing_sec(sec_name, num)

            row_name = 'row' + str(i)
            missing_row(row_name, num)

    #finding all positions

    #for sections
    for sec in dict_section:
        dict_section[sec]['all_pos'].extend(
            list(dict_section[sec]['given'].values()))
        dict_section[sec]['all_pos'].extend(
            dict_section[sec]['available_pos'])

    #for rows
    for row in dict_row:
        dict_row[row]['all_pos'].extend(
            list(dict_row[row]['given'].values()))
        dict_row[row]['all_pos'].extend(
            dict_row[row]['available_pos'])

    #for columns
    for col in dict_col:
        dict_col[col]['all_pos'].extend(
            list(dict_col[col]['given'].values()))
        dict_col[col]['all_pos'].extend(
            dict_col[col]['available_pos'])
        

    #creating a dict to store possibilities of each block(unit)
    dict_block = {}
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                dict_block[(i,j)] = [num for num in range(1, 10)]


    return dict_section, dict_row, dict_col, dict_block


#counting and sorting sections, rows and columns using known digits and
#returning section, row and col with most no. of known digits 
def count(dict_section, dict_row, dict_col):
    #print('hello')
    count_sec = {}
    count_row = {}
    count_col = {}

    for sec, row, col in zip( dict_section, dict_row, dict_col ):
        sec_len = len( dict_section[sec]['given'] )
        row_len = len( dict_row[row]['given'] )
        col_len = len( dict_col[col]['given'] )
        
        if sec_len != 9:
            count_sec[sec] = sec_len

        if row_len != 9:
            count_row[row] = row_len

        if col_len != 9:
            count_col[col] = col_len

    '''
    #sorting in decsending order
    count_sec = {key: value for key, value in
                 sorted(count_sec.items(),
                        key=lambda item: item[1], reverse=True) if value != 9}

    count_row = {key: value for key, value in
                 sorted(count_row.items(),
                        key=lambda item: item[1], reverse=True) if value != 9}

    count_col = {key: value for key, value in
                 sorted(count_col.items(),
                        key=lambda item: item[1], reverse=True) if value != 9}
    '''

    most_feasible = []
    most_feasible.extend(count_sec.items())
    most_feasible.extend(count_row.items())
    most_feasible.extend(count_col.items())

    most_feasible = sorted( most_feasible,
                            key=lambda item: item[1], reverse=True )

    '''
    highest_no_sec = next(iter(count_sec.items()))
    highest_no_row = next(iter(count_row.items()))
    highest_no_col = next(iter(count_col.items()))
    '''

    #print(count_sec, highest_no_sec)
    #print('hi')
    return most_feasible


#checking if any or all section, row or column is completely filled
def check_fill(dict_section, dict_row, dict_col):

    for sec in dict_section.keys():
        if ( not dict_section[sec]['missing'] and
             not dict_section[sec]['available_pos'] ):
            dict_section[sec]['all_fill'] = True

    for row in dict_row.keys():
        if ( not dict_row[row]['missing'] and
             not dict_row[row]['available_pos'] ):
            dict_row[row]['all_fill'] = True

    for col in dict_col.keys():
        if ( not dict_col[col]['missing'] and
             not dict_col[col]['available_pos'] ):
            dict_col[col]['all_fill'] = True


#updating data in section, row and column dictionaries
def update(available_pos, dict_section, dict_row, dict_col):

    digit = next(iter(available_pos.keys()))
    pos = available_pos[digit][0]
    #print(digit, pos)

    #update section
    for sec in dict_section.keys():
        
        for p in dict_section[sec]['all_pos']:

            if p == pos:
                dict_section[sec]['given'][digit] = pos
                dict_section[sec]['available_pos'].remove(pos)
                dict_section[sec]['missing'].remove(digit)

    #update row
    for row in dict_row.keys():
        
        for p in dict_row[row]['all_pos']:

            if p == pos:
                dict_row[row]['given'][digit] = pos
                dict_row[row]['available_pos'].remove(pos)
                dict_row[row]['missing'].remove(digit)

    #update column
    for col in dict_col.keys():
        
        for p in dict_col[col]['all_pos']:

            if p == pos:
                dict_col[col]['given'][digit] = pos
                dict_col[col]['available_pos'].remove(pos)
                dict_col[col]['missing'].remove(digit)

    check_fill(dict_section, dict_row, dict_col)

#evaluating single block possibility
def block_pos(dict_section, dict_row, dict_col, dict_block):

    list_block = list( dict_block.keys() )
    for index in list_block:

        for sec in dict_section:
            if index in dict_section[sec]['all_pos']:
                if index in dict_section[sec]['given'].values():
                    dict_block.pop(index, 0)
                else:
                    for digit in dict_section[sec]['given'].keys():
                        if digit in dict_block[index]:
                            dict_block[index].remove(digit)

        for row in dict_row:
            if index in dict_row[row]['all_pos']:
                if index in dict_row[row]['given'].values():
                    dict_block.pop(index, 0)
                else:
                    for digit in dict_row[row]['given'].keys():
                        if digit in dict_block[index]:
                            dict_block[index].remove(digit)

        for col in dict_col:
            if index in dict_col[col]['all_pos']:
                if index in dict_col[col]['given'].values():
                    dict_block.pop(index, 0)
                else:
                    for digit in dict_col[col]['given'].keys():
                        if digit in dict_block[index]:
                            dict_block[index].remove(digit)



    #creating a dictionary containing possibilities of each block seperated
    #into sections, rows and columns
    dict_block_sep = {
        'section' : {},
        'row' : {},
        'col' : {}
        }

    for item in dict_block_sep.keys():
        for i in range(1,10):
            dict_block_sep[item][item+str(i)] = {}


    for bindex in dict_block:
        
        for sec in dict_section.keys():
            if bindex in dict_section[sec]['all_pos']:
                dict_block_sep['section'][sec][bindex] = dict_block[bindex]

        for row in dict_row.keys():
            if bindex in dict_row[row]['all_pos']:
                dict_block_sep['row'][row][bindex] = dict_block[bindex]

        for col in dict_col.keys():
            if bindex in dict_col[col]['all_pos']:
                dict_block_sep['col'][col][bindex] = dict_block[bindex]


    #checking for naked double
    '''
    for bindex in dict_block:
        if len( dict_block[bindex] ) == 2:
            for item in dict_block_sep.keys():

                for sec in dict_block_sep['section']:
                    counter = 0
                    if bindex in dict_block_sep['section'][sec]:
                            for sindex in dict_block_sep['section'][sec]:
                                if dict_block_sep['section'][sec][sindex] == dict_block[bindex]:
                                    counter += 1
                                if ( dict_block[bindex] != dict_block_sep['section'][sec][sindex]
                                    and counter >= 2 ):
                                    dict_block[sindex] = [ digit for digit in dict_block[sindex]
                                                           if digit not in dict_block[bindex]]
     '''                                   
                                
                    
    def update_dict_block(item, div, pair):
        
        for index in dict_block_sep[item][div]:
            
            if dict_block_sep[item][div][index] != pair:
                
                if pair[0] in dict_block_sep[item][div][index]:
                    dict_block_sep[item][div][index].remove(pair[0])
                    dict_block[index] = dict_block_sep[item][div][index]
                    
                if pair[1] in dict_block_sep[item][div][index]:
                    dict_block_sep[item][div][index].remove(pair[1])
                    dict_block[index] = dict_block_sep[item][div][index]
            


    for item in dict_block_sep.keys():
        for div in dict_block_sep[item].keys():
            flag = True
            pair = []
            for index in dict_block_sep[item][div]:
                if flag and len( dict_block_sep[item][div][index] ) == 2:
                    pair = dict_block_sep[item][div][index]
                    #print(item, div, pair, index)
                    flag = False
                    continue
                if dict_block_sep[item][div][index] == pair:
                    #print(item, div, pair, index)
                    update_dict_block(item, div, pair)
                    
                    

    one_possibility = defaultdict(list)
    for index in dict_block.keys():
        if len( dict_block[index] ) == 1:
            digit = next(iter( dict_block[index] ))
            one_possibility[digit].append(index)
            break

    return one_possibility
                   

#solving the puzzle
def solve(dict_section, dict_row, dict_col, dict_block):
    #print(dict_section)

    while True:

        #checking through digits
        #to start
        most_feasible = count(dict_section, dict_row, dict_col)

        #most_feasible = sorted( most_feasible,
                                #key=lambda item: item[1], reverse=True )

        #highest = max( most_feasible,
         #              key=lambda item: item[1])

        #print(most_feasible)
            

        for feasible in most_feasible:

            element = feasible[0][:-1]
            #index = int(feasible[0][-1])

            #print(begin, index)
            
            
            if( element == 'section' ):
                #print('section')
                sec = feasible[0]

                missing = dict_section[sec]['missing'].copy()

                for digit in missing:

                    possibility = defaultdict(list)
                    #print(digit)
                    for pos in dict_section[sec]['available_pos']:
                        i,j = pos
                        row = 'row' + str(i+1)
                        col = 'col' + str(j+1)
                        #print(row, col)
                        #print(dict_row[row]['given'].keys())
                        #print(dict_col[col]['given'].keys())
                        if ( digit not in dict_row[row]['given'].keys()
                             and digit not in dict_col[col]['given'].keys() ):
                            possibility[digit].append(pos)

                    #print(possibility)
                    if possibility and len(possibility[digit]) == 1:
                        #print('hello')
                        update(possibility, dict_section, dict_row, dict_col)


            elif( element == 'row' ):
                #print('row')
                row = feasible[0]

                missing = dict_row[row]['missing'].copy()

                for digit in missing:

                    possibility = defaultdict(list)
                    #print(digit)
                    for pos in dict_row[row]['available_pos']:
                        i,j = pos

                        if (0 <= i < 3 and 0 <= j < 3):
                            sec = 'section1'
                        elif (0 <= i < 3 and 3 <= j < 6):
                            sec = 'section2'
                        elif (0 <= i < 3 and 6 <= j < 9):
                            sec = 'section3'
                        elif (3 <= i < 6 and 0 <= j < 3):
                            sec = 'section4'
                        elif (3 <= i < 6 and 3 <= j < 6):
                            sec = 'section5'
                        elif (3 <= i < 6 and 6 <= j < 9):
                            sec = 'section6'
                        elif (6 <= i < 9 and 0 <= j < 3):
                            sec = 'section7'
                        elif (6 <= i < 9 and 3 <= j < 6):
                            sec = 'section8'
                        elif (6 <= i < 9 and 6 <= j < 9):
                            sec = 'section9'
                        
                        col = 'col' + str(j+1)

                        #print(sec, col)
                        #print(dict_section[sec]['given'].keys())
                        #print(dict_col[col]['given'].keys())

                        if ( digit not in dict_section[sec]['given'].keys()
                             and digit not in dict_col[col]['given'].keys() ):
                            possibility[digit].append(pos)

                    #print(possibility)
                    if possibility and len(possibility[digit]) == 1:
                        #print('hello')
                        update(possibility, dict_section, dict_row, dict_col)


            elif( element == 'col' ):
                #print('column')
                col = feasible[0]

                missing = dict_col[col]['missing'].copy()

                for digit in missing:

                    possibility = defaultdict(list)
                    #print(digit)
                    for pos in dict_col[col]['available_pos']:
                        i,j = pos

                        if (0 <= i < 3 and 0 <= j < 3):
                            sec = 'section1'
                        elif (0 <= i < 3 and 3 <= j < 6):
                            sec = 'section2'
                        elif (0 <= i < 3 and 6 <= j < 9):
                            sec = 'section3'
                        elif (3 <= i < 6 and 0 <= j < 3):
                            sec = 'section4'
                        elif (3 <= i < 6 and 3 <= j < 6):
                            sec = 'section5'
                        elif (3 <= i < 6 and 6 <= j < 9):
                            sec = 'section6'
                        elif (6 <= i < 9 and 0 <= j < 3):
                            sec = 'section7'
                        elif (6 <= i < 9 and 3 <= j < 6):
                            sec = 'section8'
                        elif (6 <= i < 9 and 6 <= j < 9):
                            sec = 'section9'
                        
                        row = 'row' + str(i+1)

                        #print(sec, row)
                        #print(dict_section[sec]['given'].keys())
                        #print(dict_row[row]['given'].keys())

                        if ( digit not in dict_section[sec]['given'].keys()
                             and digit not in dict_row[row]['given'].keys() ):
                            possibility[digit].append(pos)

                    #print(possibility)
                    if possibility and len(possibility[digit]) == 1:
                        #print('hello')
                        update(possibility, dict_section, dict_row, dict_col)



        #checking through blocks
        possibility = block_pos(dict_section, dict_row, dict_col, dict_block)
        if possibility:
            update(possibility, dict_section, dict_row, dict_col)

        flag = False

        for sec in dict_section.keys():
            if dict_section[sec]['all_fill'] == False:
                flag = False
                break
            else:
                flag = True
                    
        
        if flag:
            break

            
#to convert dict to list
def dict_to_list(dict_row):

    grid = [ [0 for j in range(9)] for i in range(9) ]
    
    for row in dict_row.keys():
        i = int(row[-1])-1
        for item in dict_row[row]['given'].items():
            j = item[1][1]
            grid[i][j] = item[0]

    return grid
        

#main code
grid = user_input()
display(grid)
dict_section, dict_row, dict_col, dict_block = divide(grid)
solve(dict_section, dict_row, dict_col, dict_block)
solved_grid = dict_to_list(dict_row)
display(solved_grid)
print('OVER')


