
class RemPass():
    def __init__(self):
        super().__init__()
        self.title = 'TAMUS - Iniciar sesión'
        self.subtitle ='Recupera tu cuenta'
        self.subtitleXPath = '/html/body/div[1]/div[1]/div[1]/div[2]/label'
        self.mailXPath = "/html/body/div[1]/div[1]/div[2]/div/input"
        self.btnConfirmID = 'recoveryButton'
        self.btnBackID = 'cancelButton'
        self.helpID = 'login-help'


class ConfirmRemPass():
    def __init__(self):
        super().__init__()
        self.url = 'https://tamus.hi-iberia.es/?recovery'
        self.subtitleXPath = '/html/body/div[1]/div[1]/div[1]/div[2]/label'
        self.subtitle = 'Recupera tu cuenta'
        self.messageXPath = '/html/body/div[1]/div[1]/div[2]/div/h3'
        self.message = 'Se ha enviado un correo con tu nueva contraseña. Lo recibirá en unos minutos. Compruebe su ' \
                       'carpeta de spam.'
        self.resendEmailID = 'resend_mail'
        self.btnBackID = 'cancelButton'
        self.btnBackXPATH = '//*[@id="cancelButton"]'
