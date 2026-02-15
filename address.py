book = {}

book['Tom'] = {
    "name" : "Tom",
    "address" : "Uppal",
    "phno" : 9397939110
}

book['Jerry'] = {
    "name" : "Jerry",
    "address" : "NGRI",
    "phno" : 9397339110
}

import json

s = json.dumps(book)
with open("el-krate.json", "w") as f:
    f.write(s)

print(s)
