# Emby自动追剧系统 —— 动漫篇

本文所有教程基于root用户，默认git clone后文件夹地址为：/root/Emby

关于代码中的自动重命名部分，只适配了以下字幕组（排名不分先后），看得懂代码的可以自己适配。
```
 NC-Raws
 NaN-Raws
 ANi
 风车字幕组(WMSUB)
 银色子弹字幕组(SBSUB)
 jibaketa
 Lilith-Raws
 LoliHouse(萝莉工坊)
 CoolComic404（酷漫404)
 Nekomoe kissaten(喵萌奶茶屋)
```
### 环境准备

qBittorrent、rclone、Python3 & Pip3、已经搭建好的Emby

#### qBittorrent

```
wget https://github.com/c0re100/qBittorrent-Enhanced-Edition/releases/download/release-4.4.3.12/qbittorrent-enhanced-nox_x86_64-linux-musl_static.zip
apt install -y unzip
unzip qbittorrent-enhanced-nox_x86_64-linux-musl_static.zip
chmod +x ./qbittorrent-nox
  
./qbittorrent-nox -d
```

此时，qBittorrent已经成功在后台运行。浏览器输入http://IP:8080 ，默认用户名：admin，默认密码：adminadmin。登入后，点击左上方设置图标的按钮，选择Web UI标签页，第一个选项可以更改页面语言，下方可以修改登录密码，改完了别忘了点击最下方的保存(Save)

#### rclone

1、安装rclone
```
curl https://rclone.org/install.sh | sudo bash
```
2、配置
```
rclone config
```
o remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n

name emby 随意取 但是后面的代码也会相应改变

Choose a number from below, or type in your own value
选谷歌 （13） 可能会因为版本的不同而改变 注意选择 Google drive

client_id> 直接回车

client_secret> 直接回车

Choose a number from below, or type in your own value
scope> 1 选1 有最大的使用权限。

ID of the root folder
Leave blank normally.

Fill in to access "Computers" folders (see docs), or for rclone to use
a non root folder as its starting point.

Note that if this is blank, the first time rclone runs it will fill it
in with the ID of the root folder.

Enter a string value. Press Enter for the default ("").
root_folder_id> 空，直接回车。空是跟路径如果想用别的根路径

Service Account Credentials JSON file path
Leave blank normally.
Needed only if you want use SA instead of interactive login.
Enter a string value. Press Enter for the default ("").
service_account_file> 直接回车

Edit advanced config? (y/n)
y) Yes
n) No (default)
y/n> n 不用别的高级配置

Use auto config?

Say Y if not sure
Say N if you are working on a remote or headless machine
y) Yes (default)
n) No
y/n> n 因为我们是vps操作，不能auto config
Please go to the following link: https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Log in and authorize rclone for access
Enter verification code>贴入你获取到的key

Configure this as a team drive?
y) Yes
n) No (default)
y/n> y

Choose a number from below, or type in your own value
1 / 影音云端盘
\ "0AGfwXXXXXXXXXXXX"
2 / homenet6精英nas盘
\ "0AXXXXXXXXXXXXXXX"
Enter a Team Drive ID>

y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q

3.挂载
```
mkdir -p /home/gdrive

/usr/bin/rclone mount emby: /home/gdrive \
 --umask 0000 \
 --default-permissions \
 --allow-non-empty \
 --allow-other \
 --buffer-size 32M \
 --dir-cache-time 12h \
 --vfs-read-chunk-size 64M \
 --vfs-read-chunk-size-limit 1G &

```
4、查看挂载
```
df -h
```
5、自动挂载
```
cat > /etc/systemd/system/rclone.service <<EOF
[Unit]
Description=Rclone
AssertPathIsDirectory=LocalFolder
After=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/rclone mount emby: /home/gdrive \
 --umask 0000 \
 --default-permissions \
 --allow-non-empty \
 --allow-other \
 --buffer-size 32M \
 --dir-cache-time 12h \
 --vfs-read-chunk-size 64M \
 --vfs-read-chunk-size-limit 1G
ExecStop=/bin/fusermount -u LocalFolder
Restart=on-abort
User=root

[Install]
WantedBy=default.target
EOF
```
6、设置启动
```
systemctl start rclone
```
7、开启启动
```
systemctl enable rclone
```

#### Python3 & Pip3

自己上网查找安装，教程太多不再赘述

```
git clone https://github.com/xhrzg2017/Emby.git
```



### 自动更新

进入qBittorrent，点击【设置】，做如下修改：

![](https://tva4.sinaimg.cn/large/007dA9Dely8h2iks6781xj31ov0u00vm.jpg)

![](https://tva2.sinaimg.cn/large/007dA9Dely8h2iksmik7jj31ot0u0djt.jpg)


```
python3 /root/Emby/update.py "%F"
```

然后点击右上角【RSS】，进入RSS配置页面：

![](https://tva4.sinaimg.cn/large/007dA9Dely8h2iktqgb0oj31ot0u0aby.jpg)

首先，点击【新RSS订阅】，输入动漫订阅地址，或用其他你自己找的也行
```
https://bangumi.moe/rss/latest
https://acg.rip/.xml
```
![](https://tva2.sinaimg.cn/large/007dA9Dely8h2ikvdlgwyj31or0u0tau.jpg)

再点击【RSS下载器】，这里示范添加一个新番【间谍过家家】

![](https://tva3.sinaimg.cn/large/007dA9Dely8h2iky1jzhvj31ox0u00xh.jpg)

里面这样设置，红框标出三个需要修改的地方：

![](https://tva4.sinaimg.cn/large/007dA9Dely8h2ikz3ua0lj30va0p7aes.jpg)

具体这个【必须包含】里面该填什么，需要你去RSS订阅源里自己找，然后提取一个独一无二，只属于这个资源的标识。比如图中的【间谍过家家 NC B-Global】，NC代表NC-RAWS的资源，这样就不会抓取到别的字幕组；B-Global是NC-RAWS为了区分Baha源和港澳台源所加的标识，我们这里需要港澳台源，所以加B-Global；间谍过家家为番剧名，这个具体是什么要去看字幕组发布的资源叫什么，同一个番，有些字幕组会按繁体来，叫做间谍家家酒。有时你还可以加上清晰度，比如1080。

![](https://tva2.sinaimg.cn/large/007dA9Dely8h2il447d3tj31ov0u07gy.jpg)

【保存到指定目录】必须要像我这样写，格式为/***/间谍过家家/Season 1，因为重命名脚本会读取路径，最后两个如果不是番剧名和季数就会报错。

最后点击保存，番剧便会开始下载，有更新时也会自动下载。



如果你这个qBittorrent只用于更新番剧，并且VPS硬盘空间也不大，可以改下这个设置，适当做种后删除文件。

![](https://tva2.sinaimg.cn/large/007dA9Dely8h2ilfidpmnj30r00pldii.jpg)
