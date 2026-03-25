class Hoteles:
    def __init__(self):
        super().__init__()
        self.url = 'https://tamus.io/hoteles/'
        self.opHotLink = 'HOTELES'
        self.primeraLineaHotXPath = '/html/body/div[1]/div[1]/div/div/article/div/div/div/div[1]/div[1]/div/div[1]/div/h1'
        self.primeraLineaHotTXT = 'Tener todo apunto en un hotel es una tarea complicada.'
        self.nombrepesHot = 'HOTELES - TAMUS'
