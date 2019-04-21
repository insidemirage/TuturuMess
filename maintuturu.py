from form import *
import configparser
def CheckconfiginiFile():
    config = configparser.ConfigParser()
    config.read('config.ini')
    CreateForm(config['kwork']['pass'], config['kwork']['login'])
CheckconfiginiFile()
    