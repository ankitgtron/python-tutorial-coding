book = {}
book["tom"] = {
    'name' : 'tom',
    'address' : '1 red street, NY',
    'phone' : '989898'
}
book["bob"] = {
    'name' : 'bob',
    'address' : '1 green street, NY',
    'phone' : '232323'
}

import json
s = json.dumps(book)
with open("H:\\book.txt", "w+") as f:
    f.write(s)



