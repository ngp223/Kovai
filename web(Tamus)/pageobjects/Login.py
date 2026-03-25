class Login:
    def __init__(self):
        super().__init__()
        self.url = 'https://tamus.hi-iberia.es/'
        self.title = 'TAMUS - Iniciar sesión'
        self.subtitleXPath = '/html/body/div[1]/div[1]/div[1]/div[2]/label'
        self.subtitle = 'Accede a tu cuenta'
        self.logoImgPath = "//div[@id='images']//img[@id='logoImg']"
        self.logoImgID = 'logoImg'
        self.logoNameID = 'logoName'
        self.logoNameXPath = "//*[@id='logoName']"
        self.usernameID = 'username'
        self.passwordID = 'pass'
        self.inicioBtnID = 'loginButton'
        self.forgotpassID = 'forgotPass'
        self.registerID = 'register'
        self.votquestionXPath = '/html/body/div[1]/div[2]/i'
        self.msgLoginErrorID = 'error-messages'
        self.msgLoginErrorXPath = '//*[@id="error-messages"]'
        self.msgLoginError = 'Contraseña o nombre de usuario incorrecto.'
        self.msgLoginErrorPassXPath = '/html/body/div[1]/div[1]/div[2]/div[1]/label'
        self.msgLoginErrorPass = 'Por favor, introduzca la contraseña.'

