# -*- coding: utf-8 -*-
import sys
import re
import os
import time

text = sys.argv[1]
name = text.split('/')
length = len(name)
length_end = len(name[length - 1])
houzhui = name[length - 1][-3:]
newpath = text[:-length_end]
filename = text[-length_end:]


def deldir(path):
    """
    清理空文件夹和空文件
        param path: 文件路径，检查此文件路径下的子文件
        """
    print('*' * 30)
    try:
        files = os.listdir(path)  # 获取路径下的子文件(夹)列表
        print(files)
        for file in files:
            print('遍历路径：' + os.fspath(path + '/' + file))
            if os.path.isdir(os.fspath(path + '/' + file)):  # 如果是文件夹
                print(file + '是文件夹')
                if not os.listdir(os.fspath(path + '/' + file)):  # 如果子文件为空
                    print(file + '是空文件夹,即将执行删除操作')
                    os.rmdir(os.fspath(path + '/' + file))  # 删除这个空文件夹
                else:
                    print(file + '不是空文件夹')
                    deldir(os.fspath(path + '/' + file))  # 遍历子文件
                    if not os.listdir(os.fspath(path + '/' + file)):  # 如果子文件为空
                        print(file + '是空文件夹,即将执行删除操作')
                        os.rmdir(os.fspath(path + '/' + file))  # 删除这个空文件夹
            elif os.path.isfile(os.fspath(path + '/' + file)):  # 如果是文件
                print(file + '是文件')
                if os.path.getsize(os.fspath(path + '/' + file)) == 0:  # 文件大小为0
                    print(file + '是空文件，即将执行删除操作！')
                    os.remove(os.fspath(path + '/' + file))  # 删除这个文件
        return
    except FileNotFoundError:
        print("文件夹路径错误")


zhengze = re.compile(r'\[(.+?)\]', re.S)
try:
    judge = re.findall(zhengze, filename)
    test = judge[0]
except:
    nn = name[length - 3]  # nn=剧集名
    seanson1 = name[length - 2]
    seanson = re.findall("\d+", seanson1)[0]  # season=季
    # nn = nn.encode("ISO-8859-1").decode('utf-8')
    os.system('python3 -X utf8 ./EpisodeReName.py --path ' + '"' + newpath[:-1] + '"')
    deldir(newpath)
else:
    if (judge[0] == "NC-Raws"):
        name1 = text.split(' - ')
        EP = re.findall("\d+", name1[1])[0]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)


    elif (judge[0] == "NaN-Raws"):
        EP = judge[1]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)


    elif (judge[0] == "ANi"):
        name1 = text.split(' - ')
        EP = re.findall("\d+", name1[1])[0]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)





    elif (judge[0] == "jibaketa"):
        name1 = text.split(' - ')
        EP = re.findall("\d+", name1[1])[0]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + 'S' + seanson + 'E' + EP + ' - 粤语.' + houzhui)


    elif (judge[0] == "Lilith-Raws"):
        name1 = text.split(' - ')
        EP = re.findall("\d+", name1[1])[0]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)

    elif (judge[0] == "LoliHouse"):
        name1 = text.split(' - ')
        EP = re.findall("\d+", name1[1])[0]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + 'S' + seanson + 'E' + EP + '.' + houzhui)

    elif (judge[0] == "WMSUB"):
        EP = judge[2]
        SN = judge[1]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + SN + ' - S' + seanson + 'E' + EP + '.' + houzhui)


    elif (judge[0] == "SBSUB"):
        EP = judge[2]
        SN = judge[1]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + SN + ' - S' + seanson + 'E' + EP + '.' + houzhui)

    elif (judge[0] == "CoolComic404"):
        EP = judge[2]
        SN = judge[1]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + SN + ' - S' + seanson + 'E' + EP + '.' + houzhui)


    elif (judge[0] == "Nekomoe kissaten"):
        EP = judge[2]
        SN = judge[1]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + SN + ' - S' + seanson + 'E' + EP + '.' + houzhui)


    elif (judge[0] == "Skymoon-Raws"):
        EP = judge[2]
        SN = judge[1]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + SN + ' - S' + seanson + 'E' + EP + '.' + houzhui)


    elif (judge[0] == "OPFansMaplesnow"):
        EP = judge[2]
        SN = judge[1]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + SN + ' - S' + seanson + 'E' + EP + '.' + houzhui)


    elif (judge[0] == "DMG"):
        EP = judge[2]
        SN = judge[1]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + SN + ' - S' + seanson + 'E' + EP + '.' + houzhui)


    elif (judge[0] == "XKsub"):
        EP = judge[2]
        SN = judge[1]
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]
        os.rename(text, newpath + SN + ' - S' + seanson + 'E' + EP + '.' + houzhui)
    else:
        nn = name[length - 3]  # nn=剧集名
        seanson1 = name[length - 2]
        seanson = re.findall("\d+", seanson1)[0]  # season=季
        # nn = nn.encode("ISO-8859-1").decode('utf-8')
        print(newpath[:-1])
        os.system('python3 -X utf8 ./EpisodeReName.py --path ' + '"' + newpath[:-1] + '"')
        deldir(newpath)

time.sleep(5)
upload='rclone copy --drive-chunk-size 64M /media/Emby_Temp/ gd1:/emby/02-动漫追更/2022-10/ &'
sh=upload.encode("utf-8").decode("latin1")
os.system(sh)
print('Upload successful')
time.sleep(90)
os.rmdir(newpath)
