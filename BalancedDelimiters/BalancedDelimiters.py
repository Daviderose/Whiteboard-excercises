
str = '([()])'

def determine_balance(str):
    openers = ['(','[','{']
    beg_str = ''
    end_str = ''
    
    for i in str:
        if i in openers:
            beg_str += i
        else:
            end_str += i
    '''if ''.join(reversed(beg_str)) == end_str:
        return True
    else:
        return False'''
    check = beg_str[::-1]
    return check

if __name__ == '__main__':
    print(determine_balance(str))