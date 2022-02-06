import json
import sys  # to pass args from command file to py program
import clipboard

# clipboard.copy("asdf")  # copy to clipboard
# data = clipboard.paste()  # paste the data from clipboard to data variable
# print(data)

# print(sys.argv)  # gives all the args in cmd-line after the keyword python
# print(sys.argv[1:])  # all args after the first arg(word)

SAVED_DATA = "multiclip.json"  # file to store the key value data

# save items in a json file
def save_data(filepath, data):
    with open(filepath, "w") as f:  # open filepath and write as f var
        json.dump(data, f)  # put "data" in file f var

# save_items("test.json", {"key": "value"})

# load the json file
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        print("The file doesnt exist! Please enter a key to create new file")
        return{}

if len(sys.argv) == 2:  # needs to be 2 cmd args like "multiclip.py save"
    cmd = sys.argv[1]
    # print(cmd)
    data = load_data(SAVED_DATA)

    if cmd == "load".lower():
        # print("load")
        key = input("Enter a key: ")
        if key in data:  # check if key is in dictionary
            clipboard.copy(data[key])  # copy to clipboard
            print("Data was copied to clipboard!")
        else:
            print("Key doesn't exist!")

    elif cmd == "save".lower():
        # print("save")
        key = input("Enter a key: ")
        data[key] = clipboard.paste()  # paste in SAVED_DATA as a key
        save_data(SAVED_DATA, data)
        print("Key data saved!")


    elif cmd == "list".lower():
        # print("list")
        print(data)  # print the data
    else:
        print("Unknown command")
else:
    print("Please type 1 command!")