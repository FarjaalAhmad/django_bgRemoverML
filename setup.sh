#!/bin/bash
wget http://download.tensorflow.org/models/deeplabv3_mnv2_pascal_train_aug_2018_01_29.tar.gz
wget http://download.tensorflow.org/models/deeplabv3_pascal_train_aug_2018_01_04.tar.gz

mkdir -p models/mobile_net_model/model
tar xvzf deeplabv3_mnv2_pascal_train_aug_2018_01_29.tar.gz -C models/mobile_net_model/model --strip=1

mkdir -p models/xception_model/model
tar xvzf deeplabv3_pascal_train_aug_2018_01_04.tar.gz -C models/xception_model/model --strip=1


mkdir -p models/basnet
mkdir -p models/u2net
mkdir -p models/u2netp

cd setup/
/usr/bin/python3 download.py

mv basnet.pth ../models/basnet/
mv u2net.pth ../models/u2net/
mv u2netp.pth ../models/u2netp/

cd ../
rm deeplabv3_mnv2_pascal_train_aug_2018_01_29.tar.gz
rm deeplabv3_pascal_train_aug_2018_01_04.tar.gz
rm -rf setup/
