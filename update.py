import sys
import re
import os
import time

text = sys.argv[1]
name = text.split('/')
length = len(name)
length_end = len(name[length-1])
houzhui = name[length-1][-3:]
newpath = text[:-length_end]
filename = text[-length_end:]

zhengze = re.compile(r'\[(.+?)\]', re.S)
judge = re.findall(zhengze, filename)

if(judge[0] == "NC-Raws"):
    name1 = text.split(' - ')
    EP = re.findall("\d+", name1[1])[0]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')
elif (judge[0] == "NaN-Raws"):
    EP = judge[1]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')
elif (judge[0] == "ANi"):
    name1 = text.split(' - ')
    EP = re.findall("\d+", name1[1])[0]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')
elif (judge[0] == "WMSUB"):
    EP = judge[2]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')    
elif (judge[0] == "SBSUB"):
    EP = judge[2]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')    
elif(judge[0] == "jibaketa"):
    name1 = text.split(' - ')
    EP = re.findall("\d+", name1[1])[0]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + 'S' + seanson + 'E' + EP + '-TVB.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')    
elif(judge[0] == "Lilith-Raws"):
    name1 = text.split(' - ')
    EP = re.findall("\d+", name1[1])[0]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')    
elif(judge[0] == "LoliHouse"):
    name1 = text.split(' - ')
    EP = re.findall("\d+", name1[1])[0]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')   
elif(judge[0] == "CoolComic404"):
    EP = judge[2]
    SN = judge[1]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + SN +' - S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')
elif(judge[0] == "Nekomoe kissaten"):
    EP = judge[2]
    SN = judge[1]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + SN +' - S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')
elif(judge[0] == "Skymoon-Raws"):
    EP = judge[2]
    SN = judge[1]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + SN +' - S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')
elif(judge[0] == "OPFansMaplesnow"):
    EP = judge[2]
    SN = judge[1]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + SN +' - S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')
elif(judge[0] == "DMG"):
    EP = judge[2]
    SN = judge[1]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + SN +' - S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')
elif(judge[0] == "XKsub"):
    EP = judge[2]
    SN = judge[1]
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]
    os.rename(text, newpath + SN +' - S' + seanson + 'E' + EP + '.' + houzhui)
    nn = name[length - 3]
    nn = nn.encode("ISO-8859-1").decode('utf-8')
time.sleep(5)
os.system('rclone copy --drive-chunk-size 64M /media/Emby_Temp/ emby:/????????????/2022-7/ &')  # ????????????????????????????????????????????????????????????/media/Emby_Temp/????????????????????????????????????????????????????????????????????????/media/Emby_Temp/???????????????
time.sleep(90)
