import sys

# [Define group level master information]
#dictionary for incident type I. Key is vim number, value is type, make, year

current_key = None
value_list = []

def reset():
    # [Logic to reset master info for every new group]
    global current_key
    global value_list
    current_key = None
    value_list = []


#Run for end of every group
def flush():
    global current_key
    global value_list
    # write the output
    sum = 0

    for value in value_list:
        #each value is a tuple with format (type, make, year)
        count_val = value
        sum += count_val
    print(f'{current_key}\t{sum}')

#input comes from stdin (the mapper)
# the input is key value pair. key is the composite key of make and year, value is 1
for line in sys.stdin:
    # parse the input we got from mapper and update the master info
    str_vals = line.split('\t')
    key = str_vals[0]
    value = int(str_vals[1])

    #detect key changes
    if current_key != key:
        if current_key != None:
            #Write result to stdout
            flush()
        reset()

    # update more master info after the key change handling
    value_list.append(value)
    current_key = key

# do not forget to output the last group if needed!
flush()