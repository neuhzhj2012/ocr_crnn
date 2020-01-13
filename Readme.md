## 字库文件 ##
- windows字库路径：C:\Windows\Fonts

    `[Windows + E] -> %WINDIR%/Fonts`

- linux字库路径：/usr/share/fonts

    `root@9080e45b4485:~# apt-get install  fontconfig   root@9080e45b4485:~# fc-list`

## 文字样本生成及增强 ##
- 文字生成命令

    `python main_ipl.py`

- 数据增强命令

    `python aug_data.py`

## 模型训练 ##

### 识别网络 ###

- 深度学习网络[crnn.pytorch](https://github.com/meijieru/crnn.pytorch)用做训练字符识别的模型，该模型依赖于ctcloss计算损失值，需要安装[warp-ctc](https://github.com/SeanNaren/warp-ctc)。  ps：使用py2环境,torch=1.1.0。
- 训练集和测试集的生成程序详见[create_dataset.py](https://github.com/bgshih/crnn/blob/master/tool/create_dataset.py)
- 训练命令，需要修改学习率为0.0001，设置区间一般为 [0.00005, 0.001]

    `python2 train.py --lr 0.0001 --trainroot carplate_lmdb/train/ --valroot carplate_lmdb/val/ --cuda --random_sample --workers 10 --displayInterval 500 --valInterval 500 --expr_dir newmodel --alphabet "云京冀吉宁川新晋桂沪津浙渝湘琼甘皖粤苏蒙藏豫贵赣辽鄂闽陕青鲁黑ABCDEFGHJKLMNOPQRSTUVWXYZ0123456789"`