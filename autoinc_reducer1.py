import sys

# [Define group level master information]
#dictionary for incident type I. Key is vim number, value is type, make, year
i_dict = {}
current_vin = None
value_list = []
def reset():
    # [Logic to reset master info for every new group]
    i_dict = {}
    current_vin = None
    value_list = []

#Run for end of every group
def flush():
    # write the output

    for value in value_list:
        #each value is a tuple with format (type, make, year)
        type_val = value[0]
        if type_val == 'A':
            # Get make, year from the dictionary using vim number
            make_val = i_dict[current_vin][1]
            year_val = i_dict[current_vin][2]
            value = (type_val, make_val, year_val)
            print(f'{current_vin}\t{value}')
        else:
            #skip those records
            continue

#input comes from stdin (the mapper)
# the input is key value pair that sorted by key
for line in sys.stdin:
    # parse the input we got from mapper and update the master info
    str_vals = line.split('\t')
    vin = str_vals[0]

    #convert string to tuple
    value = eval(str_vals[1])

    # Update lookup dicktionary
    type_val = value[0]
    if type_val == 'I':
        # add (key, value) to dictionary
        i_dict[vin] = value
    #detect key changes
    if current_vin != vin:
        if current_vin != None:
            #Write result to stdout
            flush()
        reset()

    # update more master info after the key change handling
    value_list.append(value)
    current_vin = vin

# do not forget to output the last group if needed!
flush()

