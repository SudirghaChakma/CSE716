import pickle


def write():        # writing a string of two lines in a binary file
    with open('myfile.info', 'wb') as f:
        a = input("Enter first line: ")
        b = input("Enter second line: ")
        x = a + '\n' + b
        pickle.dump(x, f)


def read():
    with open('myfile.info', 'rb') as f:
        data = pickle.load(f)
        print(data)


def main():
    write()
    print('Your string has been written to the binary file.')
    print('The file containing your string is as follows: ')
    read()
    print()
    print('The file up untill letter o is: ')   # the code to only print the file until letter o
    with open('myfile.info', 'rb') as f:
        data = pickle.load(f)
    for word in data:
        if word == 'o':
            break
        print(word, end='')


if __name__ == '__main__':
    main()