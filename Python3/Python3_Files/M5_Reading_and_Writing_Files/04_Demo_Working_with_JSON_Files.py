import json

def read_print_json(fn, pretty, load):
    with open(fn) as json_file:
        data = json.load(json_file)
        print(json.dumps(data, sort_keys=True, indent=4 if pretty else data))

def update_author_json(fn, arr_name, pos, key, val):
    with open(fn, "r") as read_file:
        data = json.load(read_file)
        data[arr_name][pos][key] = val
        with open(fn, "w") as write_file:
            json.dump(data, write_file)

# read_print_json("./Files/authors.json", True, False)
update_author_json("./Files/authors.json", "authors", 1, "courses", 10)