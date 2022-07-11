# book={}
# book['Tom']={
#     "name":"Tom",
#     "address":"1 street red day NY",
#     "phone":23456543
# }
# book['Bob']={
#     "name":"Bob",
#     "address":"4 street green NY",
#     "phone":9574638438
# }
# import json 
# s=json.dumps(book)
# with open("book.txt","w") as f:
#     f.write(s)


with open("book.txt","r") as f:
    b=f.read()
import json
book=json.loads(b)
print(book["Bob"])