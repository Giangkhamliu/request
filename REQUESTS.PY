import requests,json
r=requests.get("http://saral.navgurukul.org/api/courses")
a=r.json()
with open("courses.json","w") as f1:
    new=json.dump(a,f1,indent=4)
store=(a["availableCourses"])
name,id=[],[]
for i in range(len(store)):
    a=store[i]["name"]
    b=store[i]["id"]
    name.append(a)
    id.append(b)
    print(i+1,":",a,"--",b)
print(" ")
user=int(input("Enter the chapter you want to read:-"))-1
user1=name[user]
user2=id[user]
print(user1,":-",user2)
req=requests.get("http://saral.navgurukul.org/api/courses/74/exercises")
b=req.json()
with open("api.json","w") as f2:
    json.dump(b,f2,indent=4)
req1=requests.get("http://saral.navgurukul.org/api/courses/"+user2+"/exercises")
content=req1.json()
with open("api2.json","w") as f3:
    json.dump(content,f3,indent=4)
slug=[]
i=0
while i<len(content["data"]):
    print(i+1,content["data"][i]["name"])
    print()
    if content["data"][i]["childExercises"]==[]:
        print("         ","[]")
        store=content["data"][i]["slug"]
        slug.append(store)
    else:
        j=0
        while j<len(content["data"][i]["childExercises"]):
            print("     ",j+1,content["data"][i]["childExercises"][j]["name"])
            j+=1
    i+=1  
k=0
while k<len(slug):
    print(k,slug[k])
    k=k+1
var1=int(input("Show the content of slug:- "))
var2=requests.get("https://saral.navgurukul.org/api/courses/"+user2+"/exercise/getBySlug?slug="+(slug[var1]))
data3=var2.json()
with open ("data3.json","w") as f3:
    json.dump(data3,f3,indent=4)
print(data3["slug"])
while True:
    x=var1
    print()
    print("....................")
    options=input("Enter your option back,next,exit:-")
    if options=="next":
        x+=1
        req=requests.get("https://saral.navgurukul.org/api/courses/"+user2+"/exercise/getBySlug?slug="+(slug[x]))
        r1=req.json()
        print(r1["content"],"\n")
    elif options=="back":
        c=1
        for i in content["data"]:
            print(c,i["name"])
            c+=1
            for j in i["childExercises"]:
                print("    ",c,j["name"])
                c+=1
                break
    else:
        break
