# yolo_template

默认使用voc的cfg文件
初次需要运行 `weights/download_default_weight.sh` 下载与训练模型

训练图片时把图片放到 `pictures/{两位数字+英文类型名称}/images/{图片名称}.jpg`
对应的annotation 放到 `pictures/{两位数字+英文类型名称}/lables/{图片名称}.txt`

`{图片名称}.txt` 文件中的头两个数字 必须和 文件夹的两位数字 一致 必须是连续数字

`{图片名称}.txt` 解释:
`两位数字的编号` `对象x中心 / 图片weight` `对象y中心 / 图片height` `对象weight / 图片weight`  `对象height / 图片height` 

运行 `python crun.py` 根据放入的图片自动编辑配置文件
然后 `./run.sh` 开始学习
执行 `./test.sh` 打开摄像头测试