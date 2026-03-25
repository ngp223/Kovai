class Notificaciones:
    def __init__(self):
        super().__init__()
        self.panelBuscarTXT = 'Buscar'
        self.panelBuscarXPath = '//div[@id="notification-action"]/div[1]'
        self.panelBoxBuscarXPath = '//div[@id="notification-action"]/div[1]/div/input'
        self.panelConteoXPath = '//div[@id="notification-action"]/div[2]'
        self.panelConteoTXT = 'Mostrando del0al0de0notificaciones'  # REVISAR!!!
        self.panelFechaXPath = '//div[@id="notification-table"]/table/thead/tr[1]/th[1]/div'
        self.panelFechaTXT = 'Fecha'
        self.panelMsajeXPath = '//div[@id="notification-table"]/table/thead/tr[1]/th[2]/div/span'
        self.panelMsajeTXT = 'Mensaje'
        self.panelTipoXPath = '//div[@id="notification-table"]/table/thead/tr[1]/th[3]/div/span'
        self.panelTipoTXT = 'Tipo'
        self.panelAccionesXPath = '//div[@id="notification-table"]/table/thead/tr[1]/th[4]/div/span'
        self.panelAccionesTXT = 'Acciones'
        self.panelTablaID = 'notification-table'
