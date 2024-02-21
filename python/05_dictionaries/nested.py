children={
    "child1":{
        "name":"a",
        "age":10

    },
     "child2":{
        "name":"b",
        "age":10

    }, 
    "child3":{
        "name":"c",
        "age":10

    },
     "child4":{
        "name":"d",
        "age":10

    },
}
one=children.get("child1")
print(one.get("name"))



myfamily={
    "child1":children.get("child1"),
    "child2":children.get("child2"),
    "child3":children.get("child3")

}
print(myfamily)


print(myfamily["child2"]["name"])
