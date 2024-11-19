## docker 部分
### 乌班图教程 安装docker
详见知乎教程
https://zhuanlan.zhihu.com/p/651148141
```
sudo apt-get update
```
```
sudo apt-get install docker-ce
```
 #### portainer  docker管理器
```
docker run -d --name portainer \
-p 9000:9000 \
--restart always \
-v /var/run/docker.sock:/var/run/docker.sock \
6053537/portainer-ce
```
#### emby 服务端
限制 cpu 50% 750m内存
```
docker run -d --name emby \
-m 750m \
--cpus=1 \
-v /home/emby/config:/config \
-v /home/emby/media:/home/emby/media \
--net=host \
-e UID=0 \
-e GID=0 \
-e GIDLIST=0 \
-e TZ="Asia/Shanghai" \
--device /dev/dri:/dev/dri \
--restart unless-stopped \
emby/embyserver:latest
```
#### 大佬修改（含开心版插件）
```
docker run -d --name emby \
-m 750m \
--cpus=1 \
-v /home/emby/config:/config \
-v /home/emby/media/:/media \
--net=host \
-e UID=0 \
-e GID=0 \
-e GIDLIST=0 \
-e TZ="Asia/Shanghai" \
--device /dev/dri:/dev/dri \
--restart unless-stopped \
lovechen/embyserver:latest
```
docker exec -it emby sh

美化
```
 docker exec emby /bin/sh -c 'cd /system/dashboard-ui && wget -O - https://tinyurl.com/2p97xcpd | sh'
```
旧版网页 弹幕
```
docker exec emby /bin/sh -c 'cd /system/dashboard-ui && wget -O - https://raw.githubusercontent.com/xhrzg2017/Emby/main/danmaku.sh | sh'
```
