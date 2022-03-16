import os

import yaml

# 读取yaml文件
def read_yaml(key):

    with open(os.getcwd()+'/extract.yml',encoding="utf-8") as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]

#写入yaml文件，mode=‘a'追加方式
def write_yaml(data):
    with open (os.getcwd()+'/extract.yml',encoding="utf-8",mode="a") as f:
        yaml.dump(data,stream=f,allow_unicode=True)

#清空yaml文件
def clear_yaml():
    with open(os.getcwd()+'/extract.yml',encoding="utf-8",mode="w") as f:
        f.truncate()