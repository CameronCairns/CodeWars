def simplify(poly):
    poly = poly.replace('+', ' ').replace('-', ' -')
    poly_dict = {}
    for polynomial in poly.split():
        is_negative = -1 if '-' in polynomial else 1
        const_str = ''.join([char for char in polynomial if char.isdigit()])
        variable = ''.join(sorted(
            polynomial.replace(const_str, '').strip('-')))
        constant = is_negative if const_str == '' else int(const_str)*is_negative
        if variable in poly_dict:
            poly_dict[variable] = poly_dict[variable] + constant
        else:
            poly_dict[variable] = constant
    # Now construct a list to be sorted out of the dictionary
    poly_list = [[variable, constant]
                 for variable, constant
                 in poly_dict.items()] 
    poly_list.sort(key=lambda polynomial: (len(polynomial[0]), polynomial[0]))
    simplified = ''
    is_first = True
    for polynomial in poly_list:
        if polynomial[1] != 0:
            if polynomial[1] > 0 and not is_first:
                simplified += '+'
            if abs(polynomial[1]) != 1:
                simplified += str(polynomial[1])
            elif polynomial[1] == -1:
                simplified += '-'
            simplified += polynomial[0]
            is_first = False
    return simplified
