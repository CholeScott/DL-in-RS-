# -*- coding: utf-8 -*-
 
import os
import numpy as np
import PIL
import matplotlib.pyplot as plt
import pandas as pd
 
 
def convert_train_data(file_dir):
 
    root_dir = 'D:/TF/BelgiumTSC_Testing_jpg'
    # 这是图片转换成jpg后另存为的根目录，在运行程序前需要自己先创建
 
    directories = [file for file in os.listdir(file_dir)  if os.path.isdir(os.path.join(file_dir, file))]
    # print(directories)
    # directories是一个列表，其中每个元素都是file_dir目录下的文件名，部分展示如下所示：
    # ['00000', '00001', '00002', '00003', '00004', '00005', '00006',
    #  '00007', '00008', '00009', '00010', '00011','00012', '00013',
    #  ...
 
    for files in directories:
        path = os.path.join(root_dir,files)
        if not os.path.exists(path):
            os.makedirs(path)
        # print( path)
        # 判断path路径是否存在，不存在就先创建路径，部分展示如下：
        # E:\DataSet\GTRSB\GTSRB_Final_Training_Images_roi_jpg\00000
        # E:\DataSet\GTRSB\GTSRB_Final_Training_Images_roi_jpg\00001
        # E:\DataSet\GTRSB\GTSRB_Final_Training_Images_roi_jpg\00002
        # E:\DataSet\GTRSB\GTSRB_Final_Training_Images_roi_jpg\00003
 
        data_dir = os.path.join(file_dir, files)
        # print(data_dir)，部分输出如下：
        # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00000
        # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00001
        # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00002
        # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00003
 
        file_names = [os.path.join(data_dir, f) for f in os.listdir(data_dir)  if f.endswith(".ppm")]
        # file_name里面每个元素都是以.ppm为后缀的文件的绝对地址
 
        for f in os.listdir(data_dir):
            if f.endswith(".csv"):
                csv_dir = os.path.join(data_dir, f)
                # 获取注解文件的绝对地址
                # print(csv_dir)，部分展示如下：
                # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00000\GT - 00000.csv
                # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00001\GT - 00001.csv
                # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00002\GT - 00002.csv
                # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00003\GT - 00003.csv
 
        csv_data = pd.read_csv(csv_dir)
        # csv_data是一个DataFrama形式的数据结构
 
        csv_data_array = np.array(csv_data)
        # print(csv_data_array)，部分展示如下：
        # [['00000_00000.ppm;29;30;5;6;24;25;0']
        #  ['00000_00001.ppm;30;30;5;5;25;25;0']
        #  ['00000_00002.ppm;30;30;5;5;25;25;0']
        #  ['00000_00003.ppm;31;31;5;5;26;26;0']
        #  ['00000_00004.ppm;30;32;5;6;25;26;0']
        #  ...
 
        for i in range(csv_data_array.shape[0]):
            csv_data_list = np.array(csv_data)[i,:].tolist()[0].split(";")
            # print(csv_data_list)，部分展示如下：
            # ['00000_00000.ppm', '29', '30', '5', '6', '24', '25', '0']
            # ['00000_00001.ppm', '30', '30', '5', '5', '25', '25', '0']
            # ['00000_00002.ppm', '30', '30', '5', '5', '25', '25', '0']
            # ['00000_00003.ppm', '31', '31', '5', '5', '26', '26', '0']
            # ['00000_00004.ppm', '30', '32', '5', '6', '25', '26', '0']
            # ['00000_00005.ppm', '31', '31', '6', '6', '26', '26', '0']
 
            sample_dir = os.path.join(data_dir, csv_data_list[0])
            # 获取该data_dir目录下每张图片的绝对地址
            # print(sample_dir)，部分展示如下：
            # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00000\00000_00000.ppm
            # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00000\00000_00001.ppm
            # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00000\00000_00002.ppm
            # E:\DataSet\GTRSB\GTSRB_Final_Training_Images\GTSRB\Final_Training\Images\00000\00000_00003.ppm
 
 
            img = PIL.Image.open(sample_dir)
            box = (int(csv_data_list[3]),int(csv_data_list[4]),int(csv_data_list[5]),int(csv_data_list[6]))
            roi_img = img.crop(box)
            # 获取兴趣ROI区域
 
            new_dir = os.path.join(path, csv_data_list[0].split(".")[0] + ".jpg")
            # 截取到兴趣区域后，准备另存为的地址
            # print(new_dir)，部分输出如下：
            # E:\DataSet\GTRSB\GTSRB_Final_Training_Images_roi_jpg\00000\00000_00000.jpg
            # E:\DataSet\GTRSB\GTSRB_Final_Training_Images_roi_jpg\00000\00000_00001.jpg
            # E:\DataSet\GTRSB\GTSRB_Final_Training_Images_roi_jpg\00000\00000_00002.jpg
            # E:\DataSet\GTRSB\GTSRB_Final_Training_Images_roi_jpg\00000\00000_00003.jpg
 
            roi_img.save(new_dir, 'JPEG')
 
 
 
 
def convert_test_data(file_dir):
 
    root_dir = 'D:/TF/BelgiumTSC_Testing_jpg'
 
    for f in os.listdir(file_dir):
        if f.endswith(".csv"):
            csv_dir = os.path.join(file_dir, f)
    csv_data = pd.read_csv(csv_dir)
    csv_data_array = np.array(csv_data)
 
    for i in range(csv_data_array.shape[0]):
        csv_data_list = np.array(csv_data)[i, :].tolist()[0].split(";")
        sample_dir = os.path.join(file_dir, csv_data_list[0])
        img = PIL.Image.open(sample_dir)
        box = (int(csv_data_list[3]), int(csv_data_list[4]), int(csv_data_list[5]), int(csv_data_list[6]))
        roi_img = img.crop(box)
        new_dir = os.path.join(root_dir, csv_data_list[0].split(".")[0] + ".jpg")
        roi_img.save(new_dir, 'JPEG')
 
 
 
if __name__ == "__main__":
    train_data_dir = 'D:/tf/BelgiumTSC_Testing/Testing'
    #test_data_dir = 'D:/tf/BelgiumTSC_Testing/Testing'
    convert_train_data(train_data_dir)
    #convert_test_data(test_data_dir)

