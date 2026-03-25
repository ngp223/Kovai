import configparser
import logging
import time

logger = logging.getLogger('WebLogs')


def load_config(self):
    configuracion = configparser.ConfigParser()
    configuracion.read('./conf/config.cfg')
    configuracion.sections()
    self.environment = configuracion['Environment']['tamusEnvironment']
    self.outputs = configuracion['Environment']['outputsPath']
    self.inputs = configuracion['Environment']['inputsPath']


def load_config_logging(self, feature):
    configLoggin = configparser.ConfigParser()
    configLoggin.read('./conf/logging.cfg')
    configLoggin.sections()
    # Cogemos config para logs
    logger.setLevel(configLoggin['handler_fileHandler']['level'])
    # NO FUNCIONA SI VAMOS A COGER EL FORMATO DEL LOGGING.CFG
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s [%(module)s] %(message)s -> %(funcName)s %(lineno)d')
    date = time.strftime("_%Y%m%d")
    log_name = './logs/' + str(feature)[11:18] + '_Web' + date + '.log'
    ch = logging.FileHandler(filename=log_name)
    # ch = logging.handlers.RotatingFileHandler(filename=log_name, maxBytes=10240, backupCount=10)
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def load_data(self):
    configData = configparser.ConfigParser()
    configData.read('./loginData/loginData.cfg')
    configData.sections()
    self.user_OK = configData['User_OK']['username']
    self.password_OK = configData['User_OK']['password']
    self.changePass = configData['User_OK']['changePass']
    self.user_KO = configData['User_KO']['username']
    self.password_KO = configData['User_KO']['password']
    self.changePass_KO = configData['ChangePass_KO']['changePass_KO']
    self.repChangePass_KO = configData['ChangePass_KO']['repChangePass_KO']
