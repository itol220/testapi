import os, string, re

import yaml
from common.recursion import GetDictParam


class YmlUtil(GetDictParam):

    # 获取case_data下自定义“”开头的所有ymlpath+文件名，返回一个列表
    def read_yaml_paths(self, yml_name_base):
        il = [i[0]+"/"+f for i in os.walk(os.getcwd() + '/case_data') for f in i[2]]
        fl = [i.replace(".yml", "") for i in il if yml_name_base in i]
        return fl

    # 读取指定yaml文件里的所有值支持占位替换
    def read_yaml_values(self, yml_path, data: dict = None):
        with open("{}.yml".format(yml_path), encoding="utf-8") as f:
            values_template = string.Template(f.read())
            values = values_template.safe_substitute(data) if data else \
                values_template.safe_substitute({"insert_value": ""})
            return yaml.safe_load(values)

    # 获取路径下自定义文件名开头的yml文件名，配到文件里的Key,生成一个元组对的列表，
    def read_yaml_all_tuple(self, yml_name_base):
        yml_paths = self.read_yaml_paths(yml_name_base)
        tl = []
        for item in yml_paths:
            yml_values = self.read_yaml_values(item)
            if yml_values:
                vl = [(item, b) for b in yml_values.keys()]
                tl.extend(vl)
        # print(tl)
        return tl

    # 写入yaml临时文件，mode=‘a'追加方式
    def write_yaml(self, data):
        with open(os.getcwd() + '/case_data/token_head.yml', encoding="utf-8", mode="a") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # # 清空yaml文件
    # def clear_yaml(self):
    #     with open(os.getcwd() + '/case_data/token_head.yml', encoding="utf-8", mode="w") as f:
    #         f.truncate()

    # 删除yaml临时文件
    def remove_yml(self):
        os.remove(os.getcwd() + '/case_data/token_head.yml')

    # 取临时值并插入case模板
    def insert_value(self, yml_path, case_data):
        insert_value = self.read_yaml_values(self.read_yaml_paths("token_head")[0]).get(case_data.get("insert_value"))
        print(insert_value)
        return self.read_yaml_values(yml_path, {"insert_value": insert_value})

    # 输出值写入临时yml
    def output_value(self, resp_data, output_name, output_key):
        output_dict = {output_name: self.get_value(resp_data, output_key)}
        print(output_dict)
        self.write_yaml(output_dict)

    # 传入case_photo下一个图片或视频文件的（全名+后缀），返回完整的路径地址
    def get_photo_path(self, file_name):
        return os.getcwd() + '/case_photo/{}'.format(file_name)

    # host映射参数test对应host_test.yml,//pre对应host_pre.yml,用以切换服务器
    def host_map_url(self, case_data, host_map=None, ):
        if host_map:

            host_v = re.findall(r'https://(.+?)/', case_data.get("url"))[0]
            host_name = host_v.replace(".", "-")
            host_test = self.read_yaml_values(self.read_yaml_paths("host_{}".format(host_map))[0]).\
                get("hosts").get("{}".format(host_name))
            host_url = case_data.get("url").replace(host_v, host_test)
            return host_url
        return case_data.get("url")






