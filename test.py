import re

text = '''
42/case-battle,["BC_CREATE_V3",[21128477,4,"2023-05-05 09:27:17",null,null,"public",true,[[1035,"SERENITY",0.4,1,1,"SERENITY.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21128478,3,"2023-05-05 09:27:17",null,null,"public",true,[[1034,"PROGRESS",0.4,1,1,"ANEW.png",null],[1035,"SERENITY",0.4,2,1,"SERENITY.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21128513,4,"2023-05-05 09:27:45",null,null,"public",true,[[607,"TECH",0.48,1,1,"TECH.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21128514,3,"2023-05-05 09:27:45",null,null,"public",true,[[69,"ICE BLAST",0.32,1,1,"ice_blast.jpg",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132887,2,"2023-05-05 10:24:16",null,null,"public",true,[[28,"BEAST",0.51,1,1,"191.jpg",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132888,3,"2023-05-05 10:24:16",null,null,"public",true,[[1033,"JOY",0.4,1,1,"NEW2.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132925,4,"2023-05-05 10:24:44",null,null,"public",true,[[1033,"JOY",0.4,1,1,"NEW2.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132926,2,"2023-05-05 10:24:44",null,null,"public",true,[[34,"MILSPEC",0.23,1,1,"6.jpg",null],[1035,"SERENITY",0.4,2,1,"SERENITY.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132968,3,"2023-05-05 10:25:12",null,null,"public",true,[[30,"TEETH",0.56,1,1,"17.jpg",null]],[],1]]
'''

pattern = r'\[(\d+),"(\w+)"'
matches = re.findall(pattern, text)

import re

text = '''
42/case-battle,["BC_CREATE_V3",[21128477,4,"2023-05-05 09:27:17",null,null,"public",true,[[1035,"SERENITY",0.4,1,1,"SERENITY.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21128478,3,"2023-05-05 09:27:17",null,null,"public",true,[[1034,"PROGRESS",0.4,1,1,"ANEW.png",null],[1035,"SERENITY",0.4,2,1,"SERENITY.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21128513,4,"2023-05-05 09:27:45",null,null,"public",true,[[607,"TECH",0.48,1,1,"TECH.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21128514,3,"2023-05-05 09:27:45",null,null,"public",true,[[69,"ICE BLAST",0.32,1,1,"ice_blast.jpg",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132887,2,"2023-05-05 10:24:16",null,null,"public",true,[[28,"BEAST",0.51,1,1,"191.jpg",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132888,3,"2023-05-05 10:24:16",null,null,"public",true,[[1033,"JOY",0.4,1,1,"NEW2.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132925,4,"2023-05-05 10:24:44",null,null,"public",true,[[1033,"JOY",0.4,1,1,"NEW2.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132926,2,"2023-05-05 10:24:44",null,null,"public",true,[[34,"MILSPEC",0.23,1,1,"6.jpg",null],[1035,"SERENITY",0.4,2,1,"SERENITY.png",null]],[],1]]
42/case-battle,["BC_CREATE_V3",[21132968,3,"2023-05-05 10:25:12",null,null,"public",true,[[30,"TEETH",0.56,1,1,"17.jpg",null]],[],1]]
'''

pattern = r'\[\d+,"([^",\]]+)'
matches = re.findall(pattern, text)

print(f'Text: {text}\n')
print(f'Pattern: {pattern}\n')
print(f'Matches: {matches}\n')
