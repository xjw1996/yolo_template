while true
do
darknet detector train ./path.conf ./yolov3-voc.cfg ./weights/yolov3-voc.backup
done
