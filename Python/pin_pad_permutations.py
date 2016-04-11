# The idea with this problem is that an observed pin code may contain errors in
# sight. Any number in the observed pin code may actually be an adjacent number
# so create an algorithm to find all possible variations of an observed pin
# number so that you can try to brute force the pin with a known set of 
# dictionaries

# Necessary to merge dictionaries in comprehension due to lack of 2.7
# support of {**{}, **{}} syntax
def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z


#Pin pad used
pin_pad = [['1', '2', '3'],
           ['4', '5', '6'],
           ['7', '8', '9'],
           [None, '0', None],]
           
# Dictionary of all possible adjacent keys and key itself
possible = {pin_pad[posx][posy]:
			merge_two_dicts(
               {pin_pad[posx + x][posy]
            	for x in [-1, 0, 1]
            	if(posx + x < len(pin_pad) and
                   posx + x >= 0 and
                   pin_pad[posx + x][posy] is not None)},
			   {pin_pad[posx][posy + y]
            	for y in [-1, 0, 1]
            	if(posy + y < len(pin_pad[0]) and
                   posy + y >= 0 and
                   pin_pad[posx][posy + y] is not None)})
            for posx in range(len(pin_pad))
            for posy in range(len(pin_pad[0]))
            if pin_pad[posx][posy] is not None}

def get_pins(observed):
    # Start with an empty string
    permutations = ['',]
    for num in list(observed):
        # Loop over every observed number
        # Store the old set of permutations for iterating over
        oldperms = permutations
        # Point permutations to an empty list
        permutations = []
        for perm in oldperms:
            # loop over every current permutation in the oldperms list
            for pos in possible[num]:
                # Create a new array index with the permutation so far in
                # addition to one of the possible values for the observed 
                # number
                permutations.append(perm + pos)
    return permutations

# Best practice solution from CodeWars
# from itertools import product
# 
# ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')
# 
# def get_pins(observed):
#     return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
