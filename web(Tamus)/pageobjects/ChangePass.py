class ChangePass:
    def __init__(self):
        super().__init__()
        self.titlePath = '//div[@id="passChangeModal"]/div/div[1]/span'
        self.title = 'CAMBIO DE CONTRASEÑA'
        self.closeXPath = '//div[@id="passChangeModal"]/div/div[1]/i'
        self.passActTXT = 'Contraseña actual*'
        self.passActTXTXPath = '//div[@id="passChangeModal"]/div/form/div[1]/div[1]/label/div'
        self.passActBoxXPath = '//div[@id="passChangeModal"]/div/form/div[1]/div[1]/label/input'
        self.passNewTXT = 'Contraseña nueva*'
        self.passNewTXTXPath = '//div[@id="passChangeModal"]/div/form/div[1]/div[2]/label/div'
        self.passNewBoxXPath = '//div[@id="passChangeModal"]/div/form/div[1]/div[2]/label/input'
        self.passRepNewTXT = 'Repetir contraseña nueva*'
        self.passRepNewTXTXPath = '//div[@id="passChangeModal"]/div/form/div[1]/div[3]/label/div'
        self.passRepNewBoxXPath = '//div[@id="passChangeModal"]/div/form/div[1]/div[3]/label/input'
        self.btnChangeXPath = '//div[@id="passChangeModal"]/div/form/div[3]/button[2]'
        self.btnCancelXPath = '//div[@id="passChangeModal"]/div/form/div[3]/button[1]'
        self.msgeErrorXPath = '/html/body/div[4]/div/div[2]/span'
        self.msgeKoCpoVacioTXT = 'Los campos seleccionados son obligatorios.'
        self.msgeKoFormKOTXT = 'La contraseña debe tener una longitud de al menos 8 caracteres y contener una mayúscula, una minúscula y un número. Caracteres no permitidos: ,;&|'
        self.msgeKoActErrorTXT = 'La contraseña actual es incorrecta'
        self.msgeKoNoCoincTXT = 'Las contraseñas no concuerdan'

