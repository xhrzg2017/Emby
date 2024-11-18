# 乌班图+网盘+流媒体整理+emby
## 挂载盘基于网盘方案

### rclone 安装
1、安装rclone
```
curl https://rclone.org/install.sh | sudo bash
```
### 安装 fuse（具体看rclone更新）
```
apt-get install fuse3
```
2、配置
```
rclone config
```
```
o remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n

name gd1 随意取 但是后面的代码也会相应改变

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
1 / 阿初宽频
\ "0AGfwXXXXXXXXXXXX"
2 / 阿初宽频
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
```
3.路径创建
share1= 团队盘1
```
mkdir -p /home/emby/media/share1
```
4、设置开机脚步
```
cat > /etc/systemd/system/gd1.service <<EOF
[Unit]
Description=Rclone
AssertPathIsDirectory=/home/emby/media/share1
After=network-online.target

[Service]
Type=notify
ExecStart=/usr/bin/rclone mount gd1: /home/emby/media/share1  --use-mmap --umask 000 --default-permissions --no-check-certificate --allow-other --allow-non-empty --vfs-cache-mode full --buffer-size 256M --vfs-read-ahead 512M --vfs-read-chunk-size 32M --vfs-read-chunk-size-limit off --vfs-cache-max-size 10G --low-level-retries 200
ExecStop=/bin/fusermount -qzu /home/emby/media/share1
Restart=on-abort
User=root

[Install]
WantedBy=default.target
EOF
```
重新加载
```
systemctl daemon-reload
```
```
systemctl enable gd1
```
```
systemctl start gd1
```
解除挂载
```
umount /home/emby/media/share1
```
