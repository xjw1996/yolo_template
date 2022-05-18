#   ロボ研へーこのマニュアルはYoloV3の環境構築及びデータ学習までの流れを示すために作成した
作成した動画はシェアに上げた．パスは以下に示す．

\\158.217.176.190\Share\#2_学生\2021年度卒修論\R班\薛　経緯\yolo.mp4


# YoloV3の環境構築
- GPU環境のセッティングはyolo_template中のcuda.pdfに参照する
- OpenCVのインストールはhttps://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/ に参照する
- このサイトはYOLOV3の公式サイトhttps://pjreddie.com/darknet/yolo/
　
  ですが、GPUとOpenCVの環境をセッティング完了したら、以下の手順に進む
  ```
  cd ~
  git clone https://github.com/pjreddie/darknet
  cd darknet
  ```
  darknetフォルダ内のMakefileを開いて、GPU,CUDNN,OPeNCVの０を１に変更する.少なくともGPUを変更すること、全部０のままにしたら、CPUだけを使うことになる.opencvを１に変更すると、認識した画像の結果がチェックしやすくになる.CUDNN、opencvを使わなくてもGPUだけ使ってもデータの学習作業が進められる.NVCCの行も現在使っているCUDAのパスを変更した方がコンパイル時にエラーが出にくいと思う.例として以下に示す.
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
  コンパイルが通ったら、ディフォルトの画像を使って構築した環境を確認する．まず著者が64オブジェクトに対して学習した重みファイルをダウンロードすること．
  ```
  wget https://pjreddie.com/media/files/yolov3.weights //著者が学習した重みをダウンロード
  ```
  ここまで来たら、/darknet/cfg/yolov3.cfgを開いて、認識モードとトレーンモードが分けられているため、画像を認識したいときはトレーンモードをコマンドアウトしなあかん、逆に言うと画像を学習させるときも同じ作業をやる.
  
  ![Screenshot from 2022-04-21 04-38-18](https://user-images.githubusercontent.com/50350039/164309531-35fc2873-54d0-42ab-9838-3aafc4f06b60.png)
  
  最後に，以下のコマンドを実行すると，画像中のオブジェクトを検出する．

  ```
  ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg　//画像の物体を検出する、このコマンドを打ち終わったあとに認識した画像が/darknetの下に出てくれると思う.
  ```

  ちなみに，ウェブカメラを使ってリアルタイムで物体を検出したい場合では，以下のコマンドを実行する．しかし，MakefileなかのGPUとOpenCVを１に修正しコンパイルが通った（GPUとOpenCVを使うこと）前提としてウェブカメラでリアルタイムで検出結果をチェックできる．
  ```
  ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights　//ウェブカメラでリアルタイム検出
  ```
  
 # カスタマイズの画像データをyoloで学習させる
   ```
   cd darknet
   git clone https://github.com/xjw1996/yolo_template.git
   ```
 - yolo_template の名前を学習させたい対象の名前を変更した方が区別しやすい．まずweights/download_default_weight.sh（実行できるように権限を与える）を実行し、事前にトレーニングされたウェイトのファイルをダウンロードする ．続いては前もって作成した学習データをpicturesのフォルダの下に、下の図ように番号つけたデータセットを入れる（番号は必ず00オブジェクト1，01オブジェクト2の形にする）
 
  ![Screenshot from 2022-04-21 03-46-45](https://user-images.githubusercontent.com/50350039/164308407-8879dab1-41cb-4ea2-a388-b8e35886af91.png)

  学習データの中身は下図に示した通り左図が学習画像で、右図は対応したアノテーションしたオブジェクトのラベリングファイルデータとなる．
 
 
  ![Screenshot from 2022-04-20 23-28-07](https://user-images.githubusercontent.com/50350039/164302344-1783b8f5-2c56-47fd-9468-0ceb1f9f761e.png)
  
  .txtの中身を見ると座標みたいなもんが出てくる，その意味は弁当(学習させたいオブジェクト)が画像中にどこら辺に位置するのかを表す．詳しいことは以下に示す．オブジェクトのラベリ   ングデータを作成するについて　https://www.youtube.com/watch?v=EGQyDla8JNU　　に参照する．　オブジェクトのラベリングの自動化について私の修論にも書かれた．
  
  ```
  <object-class> <x> <y> <width> <height> //オブジェクト番号　オブジェクトの中心は画像中の座標(x,y)  画像の幅　画像の高さ
  ```

  作成した学習データのサンプル（缶、ペットボトル、弁当、各種つきおよそ2000枚ずつ）についてはシェアのフォルダに私（2021年度薛　経緯）のところにアップロードした.(競技会でこの   ぐらいの量を使うと足りないと思う．照明変動によって(晴れる日，曇り日，日当たりが強い日，弱い日など)異なる時間帯の学習画像を作成する必要がある．試合の2ヶ月前から身をもって動   いてくれ，YoloV3のニューラルネットワークを使うと５万回までに学習させるの時間(GTX 1080のグラフィックカード　KUARO用の古いAlienware)は少なくとも一周間(7×24時間)がかかる．ガ   レリアGTX 2080のグラフィックカードを使う5日がかかるかもしれない．YoloV3-tinyという軽量化のネットワークもあるのですが，それについてまたほかの倉庫を開いて説明したいと思う．   できたらここにリンクを張り付ける)

- 下の写真に示したようにcrun.pyを開いて、dir_dataset、path_cfgとpath_templateを絶対パスに変更する
  
  ![Screenshot from 2022-04-21 04-04-17](https://user-images.githubusercontent.com/50350039/164304243-5f994045-667c-4758-8e7e-4151cbe5ae7d.png)
  
  
  crun.pyを実行できるように権限を与えてpythonファイルを実行すると面倒くさいことを自動的にやってくれる.一体どんなことを自動的に処理してくれたのかについてはコードを読んたらわ   かるはず
  ```
  python3 crun.py
  ```
  ![Screenshot from 2022-04-21 04-11-37](https://user-images.githubusercontent.com/50350039/164305231-df400837-5124-4891-802c-42f20f8c4896.png)
  
  run.sh と　test.sh中の絶対パスをすべて使っているパソコンの方に合わせて、実行できるように権限を与える.
  
  run.shをdarknetフォルダの下に移動する.
  ```
  ./run.sh //学習開始となる
  ./test.sh　//学習した重みでカメラでテストする
  ```
  
- 学習した重みファイルを使って未学習の画像に対して結果の検証については以下のコマンド
  ```
  ./darknet detector test <dir>/path.conf  <dir>/YOLOv3-voc.backup <dir>/picture.png 
  ```
