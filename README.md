#   ロボ研へーこのマニュアルはYoloV3の環境構築及びデータ学習までの流れを示すために作成した
作成した動画は以下に示す


# YoloV3の環境構築
- このサイトはYOLOV3の公式サイトhttps://pjreddie.com/darknet/yolo/　ですが、以下にまとめると
```
cd ~
git clone https://github.com/pjreddie/darknet
cd darknet
make
```
  
初次需要运行 `weights/download_default_weight.sh` 下载与训练模型

训练图片时把图片放到 `pictures/{两位数字+英文类型名称}/images/{图片名称}.jpg`

对应的annotation 放到 `pictures/{两位数字+英文类型名称}/lables/{图片名称}.txt`

`{图片名称}.txt` 文件中的头两个数字 必须和 文件夹的两位数字 一致 必须是连续数字

`{图片名称}.txt` 解释:
`两位数字的编号` `对象x中心 / 图片weight` `对象y中心 / 图片height` `对象weight / 图片weight`  `对象height / 图片height` 

把`run.sh和test.sh`文件放在darknet文件夹下，里面的path.conf cfg weights 等文件的路径改为绝对路径

运行 `python crun.py` 根据放入的图片自动编辑配置文件

crun.py的dir_dataset路径也改为绝对路径

然后 `./run.sh` 开始学习

执行 `./test.sh` 打开摄像头测试
