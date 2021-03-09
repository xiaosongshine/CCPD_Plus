# CCPD_Plus
Chinese City Parking Dataset（with Blue and Green add Yellow）


## UPdate on 10/03/2019. CCPD Dataset is now updated. We are confident that images in subsets of CCPD is much more challenging than before with over 300k images and refined annotations. 

(If you are benefited from this dataset, please cite our paper.) 
It can be downloaded from and extract by (tar xf CCPD2019.tar.xz):
 - [Google Drive](https://drive.google.com/open?id=1rdEsCUcIUaYOVRkx5IMTRNA7PcGMmSgc) 
 
 - [BaiduYun Drive(code: hm0u)](https://pan.baidu.com/s/1i5AOjAbtkwb17Zy-NQGqkw)


#### train\val\test split
The split file is available under 'split/' folder.

Images in CCPD-Base is split to train/val set. Sub-datasets (CCPD-DB, CCPD-Blur, CCPD-FN, CCPD-Rotate, CCPD-Tilt, CCPD-Challenge) in CCPD are exploited for test.
****
## UPdate on 16/09/2020. We add a new energy vehicle sub-dataset (CCPD-Green) which has an eight-digit license plate number.

It can be downloaded from: 
 - [Google Drive](https://drive.google.com/file/d/1m8w1kFxnCEiqz_-t2vTcgrgqNIv986PR/view?usp=sharing) 
 
 - [BaiduYun Drive(code: ol3j)](https://pan.baidu.com/s/1JSpc9BZXFlPkXxRK4qUCyw)
  
### metric
As each image in CCPD contains only a single license plate (LP). Therefore, we do not consider recall and concerntrate on precision. Detectors are allowed to predict only one bounding box for each image.

- Detection. For each image, the detector outputs only one bounding box. The bounding box is considered to be correct if and only if its IoU with the ground truth bounding box is more than 70% (IoU > 0.7). Also, we compute AP on the test set. 

- Recognition. A LP recognition is correct if and only if all characters in the LP number are correctly recognized.


## UPdate on 10/03/2021. Add a new sub-dataset (CCPD-Yellow) which has an eight-digit license plate number.

todo..
finish soon

## Dataset Annotations

Annotations are embedded in file name.

A sample image name is "025-95_113-154&383_386&473-386&473_177&454_154&383_363&402-0_0_22_27_27_33_16-37-15.jpg". Each name can be splited into seven fields. Those fields are explained as follows.

- **Area**: Area ratio of license plate area to the entire picture area.

- **Tilt degree**: Horizontal tilt degree and vertical tilt degree.

- **Bounding box coordinates**: The coordinates of the left-up and the right-bottom vertices.

- **Four vertices locations**: The exact (x, y) coordinates of the four vertices of LP in the whole image. These coordinates start from the right-bottom vertex.

- **License plate number**: Each image in CCPD has only one LP. Each LP number is comprised of a Chinese character, a letter, and five letters or numbers. A valid Chinese license plate consists of seven characters: province (1 character), alphabets (1 character), alphabets+digits (5 characters). "0_0_22_27_27_33_16" is the index of each character. These three arrays are defined as follows. The last character of each array is letter O rather than a digit 0. We use O as a sign of "no character" because there is no O in Chinese license plate characters.
```
provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "警", "学", "O"]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z', 'O']
ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
       'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O']
```

- **Brightness**: The brightness of the license plate region.

- **Blurriness**: The Blurriness of the license plate region.



## Acknowledgement

If you have any problems about CCPD, please contact detectrecog@gmail.com.



Please cite the paper _《Towards End-to-End License Plate Detection and Recognition: A Large Dataset and Baseline》_, if you benefit from this dataset.

