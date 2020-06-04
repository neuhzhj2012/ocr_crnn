## 字库文件

- windows字库路径：C:\Windows\Fonts
  
    `[Windows + E] -> %WINDIR%/Fonts`

- linux字库路径：/usr/share/fonts
  
    `root@9080e45b4485:~# apt-get install  fontconfig   root@9080e45b4485:~# fc-list`

## 文字样本生成及增强

- 文字生成命令
  
    `python main_ipl.py`

- 数据增强命令
  
    `python aug_data.py`

## 模型训练

### 识别网络

- 深度学习网络[crnn.pytorch](https://github.com/meijieru/crnn.pytorch)用做训练字符识别的模型，该模型依赖于ctcloss计算损失值，需要安装[warp-ctc](https://github.com/SeanNaren/warp-ctc)。  ps：使用py2环境,torch=1.1.0。

- 训练集和测试集的生成程序详见[create_dataset.py](https://github.com/bgshih/crnn/blob/master/tool/create_dataset.py)

- 训练命令，需要修改学习率为0.0001，设置区间一般为 [0.00005, 0.001]
  
    `python2 train.py --lr 0.0001 --trainroot carplate_lmdb/train/ --valroot carplate_lmdb/val/ --cuda --random_sample --workers 10 --displayInterval 500 --valInterval 500 --expr_dir newmodel --alphabet "云京冀吉宁川新晋桂沪津浙渝湘琼甘皖粤苏蒙藏豫贵赣辽鄂闽陕青鲁黑ABCDEFGHJKLMNOPQRSTUVWXYZ0123456789"`

- 测试程序中修改如下,CRNN第三个参数为alphabet长度加1。
  
    `model = crnn.CRNN(32, 1, 37, 256) -> model = crnn.CRNN(32, 1, 129, 256)`  
  
    `model.load_state_dict(torch.load(model_path)) -> model.load_state_dict({k.replace('module.',''):v for k,v in torch.load(model_path).items()})`

- 测试图片高度resize为32，宽度随意。

- 训练注意事项：

> 1. 训练集和测试集图片高参数imgH设置为32
> 
> 2. lr参数应修改在[0.00005, 0.001]区间。默认参数过大，造成不符合梯度的计算公式，从而无法收敛；参数过小时，模型参数更新较慢，学习过程较长；
> 
> 3. keep_ratio参数仅对训练集起作用，测试集缩放为100\*32，所以会造成测试集误差和训练集误差不一致(测试集误差远大于训练集误差，可能会误以为模型过拟合了)
> 
> 4. pretrained参数仅当模型输出节点数与待训练模型节点数相同时可加载，否则会报错；load_state_dict(strict=False) 设置为False时允许名字不匹配，但是名字匹配的层参数必须相同，所以无法fine-tune不同输出节点的网络；
> 
> 5. alphabet参数为待训练的字母集合，该字段长度+1=输出类别数(1标识ctc中的标识符)；
> 
> 6. saveInterval参数为模型保存地址；
> 
> 7. random_sample参数来shuffle训练数据
