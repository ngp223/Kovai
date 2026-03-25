class Contacto:
    def __init__(self):
        super().__init__()
        self.url = 'https://tamus.io/contacto/'
        self.opConXPath = '/html/body/div[1]/div[1]/header/div/div/div/div/div[2]/div/div/nav/div[8]/div/div/div/a'
        self.primeraLineaConXPath = '/html/body/div[1]/div[1]/div/div/article/div/div/div/div[2]/div[1]/div/div[1]/div/p/span'
        self.primeraLineaConTXT = 'Tener un asistente como TAMUS te hará la vida más fácil a ti y a tu personal, además de un negocio más rentable.'
        self.nombrepesCon = 'CONTACTO - TAMUS'
