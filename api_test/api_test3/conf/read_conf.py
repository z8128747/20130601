"""

   获取配置文件的相关信息

"""
import configparser
import pathlib

file = pathlib.Path(__file__).parent[0].resolve() / 'conf.ini'


# 读取配置信息
def read(section, option):
    conf = configparser.ConfigParser()
    conf.read(file)
    values = conf.get(section, option)
    return values
