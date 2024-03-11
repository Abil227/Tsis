import json

file = open(r"C:\Users\ASUS\Desktop\PP2\lab4\json\data.json", "r")
x = json.loads(file.read())


dn = []
for i in range(len(x["imdata"])):
    dn.append(x["imdata"][i]["l1PhysIf"]["attributes"]["dn"])
    
speed = []
for i in range(len(x["imdata"])):
    speed.append(x["imdata"][i]["l1PhysIf"]["attributes"]["fecMode"])
    
mtu = []
for i in range(len(x["imdata"])):
    mtu.append(x["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])


print("""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for i in range(len(dn)):
    if(len(dn[i]) == 42):
        print(dn[i], "                            ", speed[i], " ", mtu[i])
    else:
        print(dn[i], "                             ", speed[i], " ", mtu[i])

