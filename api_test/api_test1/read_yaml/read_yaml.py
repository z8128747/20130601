import yaml


# yaml文件数据的读取
def read_yaml_file(path):
    f = open(path, 'r', encoding='utf-8')
    data = yaml.load(f, Loader=yaml.FullLoader)
    return data


if __name__ == '__main__':
    print(read_yaml_file('../data/phone.yaml'))
