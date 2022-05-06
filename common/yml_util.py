import os,string

import yaml
from common.recursion import GetDictParam


class YmlUtil(GetDictParam):

    # 获取自定义“”开头的所有yml文件名，返回一个列表
    def read_yaml_names(self, yml_name_base):
        il = [i for i in os.walk(os.getcwd() + '/case_data_ym')]
        fl = [i.replace(".yml", "") for i in il[0][2] if yml_name_base in i]
        return fl

    # 读取指定yaml文件里的所有值支持占位替换
    def read_yaml_values(self, yml_name, data: dict = None):
        with open(os.getcwd() + '/case_data_ym/{}.yml'.format(yml_name), encoding="utf-8") as f:
            values_template = string.Template(f.read())
            values = values_template.safe_substitute(data) if data else \
                values_template.safe_substitute({"insert_value": ""})
            return yaml.safe_load(values)

    # 获取路径下自定义文件名开头的yml文件名，配到文件里的Key,生成一个元组对的列表，
    def read_yaml_all_tuple(self, yml_name_base):
        yml_names = self.read_yaml_names(yml_name_base)
        tl = []
        for item in yml_names:
            yml_values = self.read_yaml_values(item)
            if yml_values:
                vl = [(item, b) for b in yml_values.keys()]
                tl.extend(vl)
        # print(tl)
        return tl

    # 写入yaml文件，mode=‘a'追加方式
    def write_yaml(self, data):
        with open(os.getcwd() + '/case_data_ym/token_head.yml', encoding="utf-8", mode="a") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # 清空yaml文件
    def clear_yaml(self):
        with open(os.getcwd() + '/case_data_ym/token_head.yml', encoding="utf-8", mode="w") as f:
            f.truncate()
    #输出值写入临时yml
    def output_value(self, resp_data, output_name, output_key):

        output_dict = {output_name: self.get_value(resp_data, output_key)}
        print(output_dict)
        self.write_yaml(output_dict)
    #传入case_photo下一个图片或视频文件的（全名+后缀），返回完整的路径地址
    def get_file_path(self, file_name):
        return os.getcwd() + '/case_photo/{}'.format(file_name)





