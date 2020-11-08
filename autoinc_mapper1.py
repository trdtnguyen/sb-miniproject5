import sys


#input comes from STDIN
for line in sys.stdin:

    str_vals = line.split(',')
    type_val = str_vals[1]
    vim_num_val = str_vals[2]
    make_val = str_vals[3]
    year_val = str_vals[5]
    value = (type_val, make_val, year_val)
    print(f'{vim_num_val}\t{value}')


