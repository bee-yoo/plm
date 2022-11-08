# 人力资源领域多模态语言模型——伯乐

## 目录
 - [模型介绍](#模型介绍)
 - [模型下载](#模型下载)
 - [依赖安装](#依赖安装)
 - [快速上手](#快速上手)
 - [联系方式](#联系方式)
 - [免责声明](#免责声明)

## 模型介绍
[官方介绍页面](https://yoo-ai.com/pre-training.html)

## 模型下载

|    模型    | 层数 | 特征数 | 参数量 |
| :--------: | :--: | :----: | :----: |
| 伯乐-base  |  12  |  768   |  117M  |
| 伯乐-large |  36  |  1280  |  762M  |

 [下载链接](https://download.yoo-ai.com/resource/pretrain-model.zip)
（目前只开放伯乐-base模型下载）

## 依赖安装
使用 transformers 包加载
``` shell
pip install transformers
```

## 快速上手

```python
from transformers import AutoTokenizer, AutoModel

MODEL_DIR = r'/path/to/model'

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModel.from_pretrained(MODEL_DIR)
```



## 联系方式

chenruntian@yoojober.com

## 免责声明
该项目中的内容仅供技术研究参考，不作为任何结论性依据。使用者可以在许可证范围内任意使用该模型，但我们不对因使用该项目内容造成的直接或间接损失负责。技术报告中所呈现的实验结果仅表明在特定数据集和超参组合下的表现，并不能代表各个模型的本质。 实验结果可能因随机数种子，计算设备而发生改变。

使用者以各种方式使用本模型（包括但不限于修改使用、直接使用、通过第三方使用）的过程中，不得以任何方式利用本模型直接或间接从事违反所属法域的法律法规、以及社会公德的行为。使用者需对自身行为负责，因使用本模型引发的一切纠纷，由使用者自行承担全部法律及连带责任。我们不承担任何法律及连带责任。

我们拥有对本免责声明的解释、修改及更新权。
