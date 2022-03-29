#coding=utf-8

import os
import re
import string

dir_dataset = './pictures'
path_cfg = './yolov3-voc.cfg'


# 遍历 dataset 目录
lables_total = []
classes_total = []
for dir_name in sorted(os.listdir(dir_dataset)):
    dir_data = os.path.join(dir_dataset, dir_name)
    if os.path.isdir(dir_data):

        # 汇总类型
        classes_total.append(dir_name.lstrip(string.digits).capitalize())

        print('find images: ' +
              classes_total[-1] + '  index: ' + str(len(classes_total)-1))

        # 找出所有 图片 路径
        dir_images = os.path.join(dir_data, 'images')
        files_images = os.listdir(dir_images)
        for file_img in files_images:
            file_label = os.path.splitext(file_img)[0]+'.txt'
            path_img = os.path.join(dir_images, file_img)
            path_label = os.path.join(dir_images, '../labels', file_label)
            if(os.path.exists(path_label)):
                lables_total.append(path_img)

# 汇总结果到 train.txt 中
with open('./train.txt', 'w+') as f:
    f.writelines([s+'\n' for s in lables_total])

# 汇总类型到 names.txt 中
with open('./names.txt', 'w+') as f:
    f.writelines([s+'\n' for s in classes_total])

# 设置path.conf文件
with open('./path.conf', 'w') as f:
    f.writelines(
        '''classes = %s
train = train.txt
valid = test.txt
names = names.txt
backup = weights
''' % len(classes_total))

# 修改 cfg 文件 classes 相关参数
with open(path_cfg, 'r') as f:
    lines = f.readlines()
    find_yolo = False
    index_filters = -1
    for index, line in enumerate(lines):
        if line.find('filters') >= 0:
            index_filters = index
        if line.find('[yolo]') >= 0:
            find_yolo = True
        if line.find('classes') >= 0 and find_yolo and index_filters >= 0:
            lines[index] = 'classes='+str(len(classes_total))+'\n'
            lines[index_filters] = 'filters=' + \
                str((len(classes_total)+5)*3)+'\n'

with open(path_cfg, 'w') as f:
    f.writelines(lines)


# 判断存在预存连模型 否则下载
# path = "./weights/"+os.path.splitext(path_cfg)[0]+'.backup'
# if not os.path.exists(path):
#     print('\ncan not found first weight file , download it')
#     f_weight = urllib2.urlopen(first_weight_url)
#     with open(path,'wb') as f:
# 	f.write(f_weight.read())
#     print('download ok')

print('\nover !!')
