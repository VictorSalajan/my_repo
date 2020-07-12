def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    if len(aStr) == 1:
        return char == aStr
    middle_index = len(aStr) // 2
    middle_char = aStr[middle_index]
    if char == middle_char:
        return True
    elif char < middle_char:
        return isIn(char, aStr[:middle_index])
    else:
        return isIn(char, aStr[middle_index + 1:])

print(isIn('r', 'cceixz'))
print(isIn('x', 'cceixz'))

print(isIn('x', ''))
print(isIn('x', 'x'))
print(isIn('y', 'x'))
