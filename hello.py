# miao = "miao miao"
# print (type(miao))

# project_name = "simple-cloude-project"
# servers_count = 24
# servers_status = True


# print (type(project_name)) 
# print (type(servers_count))
# print (type(servers_status))

# server_cost_per_minute = 0.03
# storge_cost_per_minute = 0.02
# backup_cost_per_minute = 0.01
# total_servers = 8

# total_cost = server_cost_per_minute + storge_cost_per_minute + backup_cost_per_minute
# miao = total_cost * total_servers
# print (miao)


servers = [
    {"name":"miao1", "cpu":60},
    {"name":"miao2", "cpu":70},
    {"name":"miao3", "cpu":81},
    {"name":"miao4", "cpu":91},
    {"name":"miao5","cpu":40}

]
for server in servers:
    if server ["cpu"] > 80:
        print (server["name"], "warning")
    elif server ["cpu"] > 59 and server ["cpu"] < 71:
        print (server["name"], "normal")
    else:
        print (server["name"],"Nothing")



for number in range (3,16,3):
    print (number)


attempt = 1
while attempt <=4:
    print ("checking server attempt",attempt)
    attempt = attempt+1
print("Check completed!")
<<<<<<< HEAD
## i forgot this
## i forgot this also
## i also forgot this
=======
<<<<<<< HEAD


servers = [
    {"name":"first","cpu":89,"runing":True},
    {"name":"second","cpu":90,"runing":True},
    {"name":"third","cpu":91,"runing":False},
    {"name":"fourth","cpu":91,"runing":False},
    {"name":"fifth","cpu":91,"runing":True},
    {"name":"sex","cpu":91,"runing":False}

]

for server in servers:
    
    if not server["runing"]:
        print (server["name"], " server :" , "is stopped")
        continue
    if server ["runing"]:
        print (server["name"], " server :" , "is runing, and the cpu % is " , server["cpu"])
    
print("Cheacking is Completed!")




## i forgot this

>>>>>>> e92c798375ff05bb948ec0a6c4b2910e5dd826ea
