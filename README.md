#   ロボ研へーこのマニュアルはYoloV3の環境構築及びデータ学習までの流れを示すために作成した
作成した動画は以下に示す
<iframe src="//player.bilibili.com/player.html?aid=73316901&bvid=BV1VE41117r4&cid=125414920&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>


# YoloV3の環境構築
- GPU環境のセッティングはyolo_template中のcuda.pdfに参照する
- OpenCVのインストールはhttps://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/に参照する
- このサイトはYOLOV3の公式サイトhttps://pjreddie.com/darknet/yolo/　
  ですが、GPUとOpenCVの環境をセッティング完了したら、以下の手順に進む
  ```
  cd ~
  git clone https://github.com/pjreddie/darknet
  cd darknet
  ```
  darknetフォルダ内のMakefileを開いて、GPU,CUDNN,OPeNCVの０を１に変更する.少なくともGPUを変更すること、全部０のままにしたら、CPUだけを使うことになる.opencvを１に変更すると、認識した画像の結果がチェックしやすくになる.CUDNN、opencvを使わなくてもGPUだけ使ってもデータを学習できる.NVCCの行も現在使っているCUDAのパスを変更する.例として以下に示す.
  ```
  GPU=1
  CUDNN=1
  OPENCV=1　//私が使っているopencvはopencv４なので、正しく設定したいとしたら手間がかかる作業なので動画の方で説明する
  //opencv4をyolov3でも使えるようにする方法はhttps://lifesaver.codes/answer/src-image-opencv-cpp-5-10-fatal-error-opencv2-opencv-hpp-no-such-file-or-directory-1886　に参照する
  NVCC=/usr/local/cuda-10.1/bin/nvcc
  ```
  Makefileを変更したあとに、makeでコンパイルする.
  ```
  make
  ```
  コンパイルが通ったら、ディフォルトの画像を使って構築した環境を確認する
  ```
  wget https://pjreddie.com/media/files/yolov3.weights //著者が学習した重みをダウンロード
  ```
  ここまで来たら、/darknet/cfg/yolov3.cfgを開いて、認識モードとトレーンモードが分けられているため、画像を認識したいときはトレーンモードをコマンドアウトしなあかん、逆に言うと画像を学習させるときも同じ作業をやる.
  
  
  ![Screenshot from 2022-04-20 23-28-07](https://user-images.githubusercontent.com/50350039/164253774-05989589-c9e8-4da3-ba12-f474850ff08e.png)

  
  ```
  ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg　//画像の物体を検出する、このコマンドを打ち終わったあとに認識した画像が/darknetの下に出てくれると思う.
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
