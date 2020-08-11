'''
Program to Store Data in JSON file
'''
import json, datetime

def file_read():
    ''' Reading File and checking for existance '''
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File Not Found")
        file_write()

def file_write(data = {}):
    ''' Writing into file '''
    with open('data.json', 'w') as f:
        json.dump(data, f, indent = 4, sort_keys=True)

def file_display():
    ''' Displaying the file content '''
    data = file_read()
    print(json.dumps(data, indent = 4, sort_keys=True))

def file_add():
    ''' Adding new value to json file '''
    website = input("Enter Website: ")
    userid = input("Enter Username: ")
    password = input("Enter Password: ")
    data = file_read()
    uid = str(datetime.datetime.now()).replace(' ', '')
    data[uid] = [website, userid, password]
    file_write(data)

def file_delete():
    ''' Deleting a value from json file '''
    data = file_read()
    print(data)
    to_remove = input("Website to delete: ")
    removed = data.pop(to_remove, 'Value Not Found')
    file_write(data)

def main():
    while True:
        choice = input("*"*30 +"\n1. Open\n2. Add\n3. Delete\n4. Exit\n>> ")
        if choice == '1':
            file_display()
        elif choice == '2':
            file_add()
        elif choice == '3':
            file_delete()
        elif choice == '4':
            break
        else:
            print('Value Not Found!!!')


if __name__ == "__main__":
    main()    