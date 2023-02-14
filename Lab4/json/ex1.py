import json

with open('sample-data.json','r') as txt:
   data = txt.read()
   
data=json.loads(txt.read())

print('Interface Status')    
print('================================================================================')
print('DN                                                 Description           Speed    MTU ')
print('-------------------------------------------------- --------------------  ------  ------')

y = data["imdata"]  
  
for i in range(3):  
    DN = y[i]["l1PhysIf"]["attributes"]["dn"]  
    Description = y[i]["l1PhysIf"]["attributes"]["descr"]  
    Speed = y[i]["l1PhysIf"]["attributes"]["speed"]  
    MTU = y[i]["l1PhysIf"]["attributes"]["mtu"]  
    print(f'{DN}                              {Description}{Speed}   {MTU}')
