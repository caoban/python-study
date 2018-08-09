import yaml

# from pyaml import dumps as dump
# from yaml import load


#官方的导入 yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper, load, dump

def print_err(msg,quit=False):
    output = "\033[31;1mError: %s\033[0m" % msg
    if quit:
        exit(output)
    else:
        print(output)


def yaml_parser(yml_filename):
    '''
    load yaml file and return
    :param yml_filename:
    :return:
    '''
    #yml_filename = "%s/%s.yml" % (settings.StateFileBaseDir,yml_filename)
    try:
        yaml_file = open(yml_filename,'r')
        data = yaml.load(yaml_file)
        return data
    except Exception as e:
        print_err(e)








