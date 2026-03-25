class Restaurantes:
    def __init__(self):
        super().__init__()
        self.url = 'https://tamus.io/restaurantes-2/'
        self.opResLink = 'RESTAURANTES'
        self.primeraLineaResXPath = '/html/body/div[1]/div[1]/div/div/article/div/div/div/div[1]/div[1]/div/div[1]/div/h1'
        self.primeraLineaResTXT = 'Si diriges un restaurante…'
        self.nombrepesRes = 'RESTAURANTES - TAMUS'
