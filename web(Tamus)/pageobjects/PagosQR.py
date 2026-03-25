class PagosQR:
    def __init__(self):
        super().__init__()
        self.url = 'https://tamus.io/pagos-qr/'
        self.opPQRLink = 'PAGO QR'
        self.primeraLineaPQRXPath = '/html/body/div[1]/div[1]/div/div/article/div/div/div/div[1]/div[1]/div/div/div/p'
        self.primeraLineaPQRTXT = 'No hay nada más rápido y cómodo que hacer operaciones desde un QR'
        self.nombrepesPQR = 'PAGOS QR - TAMUS'
