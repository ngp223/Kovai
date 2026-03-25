class Tarifas:
    def __init__(self):
        super().__init__()
        self.url = 'https://tamus.io/tarifas/'
        self.opTarLink = 'TARIFAS'
        self.primeraLineaTarXPath = '/html/body/div[1]/div[1]/div/div/article/div/div/div/div[1]/div/div/div/div/p'
        self.primeraLineaTarTXT = 'Por menos del coste de un café al día, PAGAS EL SISTEMA durante el mes completo.'
        self.nombrepesTar = 'TARIFAS - TAMUS'
