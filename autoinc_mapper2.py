import sys


#input comes from reducer1 through STDIN
for line in sys.stdin:

    str_vals = line.split('\t')
    vin = str_vals[0]
    #value is a tuple with format (type, make, year)
    value = eval(str_vals[1])

    make_val = value[1]
    year_val = value[2]

    #make the composite key
    new_key = f'{make_val}{year_val}'
    #print composite key and count 1
    print(f'{new_key}\t1')