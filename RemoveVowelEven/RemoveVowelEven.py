

def remove_vowel_even(str):

    voweless_str = ''
    final_str = ''
    vowels = ['a','e','i','o','u']
    for char in str:
        if char not in vowels:
            voweless_str += char
    for i in range(len(voweless_str)):
        if i % 2 == 0:
            final_str += voweless_str[i]
    return final_str

if __name__ == '__main__':
    print(remove_vowel_even('Launchcode'))