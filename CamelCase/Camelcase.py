string = 'learningWhiteboardCodingCanBeFun'

def camelCount(string):
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 0
    for i in string:
        if i not in lowercase:
            count += 1
    print(count + 1)

if __name__ == '__main__':
    camelCount(string)