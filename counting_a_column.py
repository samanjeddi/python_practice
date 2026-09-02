def counting_a_column(a, b):
    '''
    this function is for counting a column in a word or a line.
    '''
    counter = 0
    for x in a:
        if x == b:
            counter += 1
    return(counter)

name = input("write a word: ")
column = input("write a column: ")
whole = counting_a_column(name, column)

print(f"{name} , has {whole} {column}.")