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
  
# カスタマイズの画像データをyoloで学習させる
```
cd darknet
git clone https://github.com/xjw1996/yolo_template.git
```
- yolo_template を名前を学習する対象のものの名前を変更した方が区別しやすい
  まずweights/download_default_weight.shを実行し、事前にトレーニングされたウェイトのファイルをダウンロードする
- 続いては前もって作成した学習データをpicturesのフォルダに入れる、下の図ように番号つけたデータセットを入れる（番号は必ず00オブジェクト1，01オブジェクト2の形にする）

  ![Screenshot from 2022-04-21 03-46-45](https://user-images.githubusercontent.com/50350039/164301640-7228b441-321b-4986-a69e-0a6d3ab03672.png)

  中身は下図に示した通り左図が学習画像で、右図は対応したアノテーションしたデータとなる

  ![Screenshot from 2022-04-21 03-52-40](https://user-images.githubusercontent.com/50350039/164302344-1783b8f5-2c56-47fd-9468-0ceb1f9f761e.png)

  作成した学習データのサンプル（缶、ペットボトル、弁当、各種つきおよそ2000枚ずつ）についてはシェアのフォルダに私（2021年度薛　経緯）のところにアップロードした.
- 下の写真に示したようにcrun.pyを開いて、dir_dataset、path_cfgとpath_templateを絶対パスに変更する
  
  ![Screenshot from 2022-04-21 04-04-17](https://user-images.githubusercontent.com/50350039/164304243-5f994045-667c-4758-8e7e-4151cbe5ae7d.png)
  pythonファイルを実行する、面倒くさいことを自動的にやってくれる.一体どんなことを処理したのかについてはコードを読んたらわかるはず
  ```
  python3 crun.py
  ```
  ![Screenshot from 2022-04-21 04-11-37](https://user-images.githubusercontent.com/50350039/164305231-df400837-5124-4891-802c-42f20f8c4896.png)

  

把`run.sh和test.sh`文件放在darknet文件夹下，里面的path.conf cfg weights 等文件的路径改为绝对路径

运行 `python crun.py` 根据放入的图片自动编辑配置文件

crun.py的dir_dataset路径也改为绝对路径

然后 `./run.sh` 开始学习

执行 `./test.sh` 打开摄像头测试
