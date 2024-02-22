# # import myModule // rename can be done
# import myModule as module # its created by me
# import platform as pt # built in module
# # myModule.greeting("AYAN")



# # a=module.person1["age"]
# # print(a)
# # ist all the defined names belonging to the platform module:
# d=dir(pt)
# print(d)

# a = pt.system()
# print(a)


from myModule import person1

print (person1["age"])