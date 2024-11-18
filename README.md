# qb自动追剧系统搭建

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
python3 /root/Emby/update/update.py "%F"
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
