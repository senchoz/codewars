#!/usr/bin/python3


# Given: an array containing hashes of names
# 
# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
# 
# Example:
# 
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
# 
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'
# 
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'
# 
# namelist([])
# # returns ''


from eval_time import eval_time

names_list = []
names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]
names_list.append(names)
names = [ {'name': 'Bart'}, {'name': 'Lisa'} ]
names_list.append(names)
names = [ {'name': 'Bart'} ]
names_list.append(names)
names = []
names_list.append(names)

def namelist(names):
    # Making a list of names
    list_names = [ name['name'] for name in names ]
    
    # Saving last element (if any) to join it like " & name" later
    part2 = list_names.pop() if list_names else ''
    
    # Joining remaining names with ', '
    part1 = ', '.join(list_names) if list_names else ''
    
    # Appending last name to part1 if part1 contain names. Otherwise assigning value of part2. 
    # If the 'names' list is empty, empty string will be returned.
    result = ' & '.join([part1, part2]) if part1 else part2
    
    return result


# better
# First I tried to do somewhat similar with    
#
# ' & '.join(', '.join([name_list[:-1], name_list[-1]]) if name_list else ''
#
# but if name_list contains only 1 element we'll be joining an empty string with a result like ' & Bart'

def namelist_improved(names):
    nameList = [elem['name'] for elem in names]
    return ' & '.join(', '.join(nameList).rsplit(', ', 1))

for names in names_list:
    eval_time(namelist(names))
    eval_time(namelist_improved(names))
