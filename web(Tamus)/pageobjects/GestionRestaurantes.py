
class GestionRestaurantes:
    def __init__(self):
        super().__init__()
        # Primeras comprobaciones: URL cargada, primer texto, título de la página
        self.url = 'https://tamus.hi-iberia.es/restaurants/terminals'
        self.titPagGestResXPath = 'html/body/div[2]/div[2]/div[1]/div[1]/div'
        self.titPagGestResTXT = 'LISTADO DE TERMINALES'
        self.nomPagGestRes = 'Gestión de Restaurantes - Listado de terminales'
        self.guaPagGestResXPath = '//*[@id="saveChanges"]'
        self.guaPagGestResTXT = 'Guardar cambios'
        self.guaPagGestROKXPath = '//*[@id="saveChanges"]/span[3]'
        self.guaPagGestROKTXT = '¡Guardado!'


        # Menú lateral
        self.latPagGestTerXPath = '/html/body/div[2]/div[1]/ul/li[1]'
        self.latPagGestTerTXT = 'Terminales'
        self.latPagGestZonXPath = '/html/body/div[2]/div[1]/ul/li[2]'
        self.latPagGestZonTXT = 'Zonas y Mesas'
        self.latPagGestCarXPath = '/html/body/div[2]/div[1]/ul/li[3]/div'
        self.latPagGestCarTXT = 'Carta'
        self.latPagGestSubXPath = '/html/body/div[2]/div[1]/ul/li[3]/ul/li[1]'
        self.latPagGestSubTXT = 'Subcategorías'
        self.latPagGestProXPath = '/html/body/div[2]/div[1]/ul/li[3]/ul/li[2]'
        self.latPagGestProTXT = 'Productos'
        self.latPagGestGruXPath = '/html/body/div[2]/div[1]/ul/li[3]/ul/li[3]'
        self.latPagGestGruTXT = 'Menús del día/grupos'
        self.latPagGestComXPath = '/html/body/div[2]/div[1]/ul/li[3]/ul/li[4]'
        self.latPagGestComTXT = 'Menús del día/combosN'
        self.latPagGestObsXPath = '/html/body/div[2]/div[1]/ul/li[3]/ul/li[5]'
        self.latPagGestObsTXT = 'Menús combo (obsoleto)'
        self.latPagGestAccXPath = '/html/body/div[2]/div[1]/ul/li[3]/ul/li[6]'
        self.latPagGestAccTXT = 'Acciones'
        self.latPagGestTarXPath = '/html/body/div[2]/div[1]/ul/li[3]/ul/li[7]'
        self.latPagGestTarTXT = 'Tarifas'
        self.latPagGestModXPath = '/html/body/div[2]/div[1]/ul/li[3]/ul/li[8]'
        self.latPagGestModTXT = 'Modificadores'
        self.latPagGestResXPath = '/html/body/div[2]/div[1]/ul/li[3]/ul/li[9]'
        self.latPagGestResTXT = 'Grupos de restaurantes'
        self.latPagGestAleXPath = '/html/body/div[2]/div[1]/ul/li[4]/div'
        self.latPagGestAleTXT = 'Alérgenos'
        self.latPagGestAl2XPath = '/html/body/div[2]/div[1]/ul/li[4]/ul/li[1]'
        self.latPagGestAl2TXT = 'Alérgenos'
        self.latPagGestAlCXPath = '/html/body/div[2]/div[1]/ul/li[4]/ul/li[2]'
        self.latPagGestAlCTXT = 'Carta'
        self.latPagGestProXPath = '/html/body/div[2]/div[1]/ul/li[5]/div'
        self.latPagGestProTXT = 'Promociones'
        self.latPagGestPr2XPath = '/html/body/div[2]/div[1]/ul/li[5]/ul/li[1]'
        self.latPagGestPr2TXT = 'Promociones'
        self.latPagGestInvXPath = '/html/body/div[2]/div[1]/ul/li[5]/ul/li[2]'
        self.latPagGestInvTXT = 'Invitaciones'
        self.latPagGestFesXPath = '/html/body/div[2]/div[1]/ul/li[5]/ul/li[3]'
        self.latPagGestFesTXT = 'Festivos'
        self.latPagGestImpXPath = '/html/body/div[2]/div[1]/ul/li[6]/div'
        self.latPagGestImpTXT = 'Impresoras'
        self.latPagGestRsmXPath = '/html/body/div[2]/div[1]/ul/li[6]/ul/li[1]'
        self.latPagGestRsmTXT = 'Resumen'
        self.latPagGestTpvXPath = '/html/body/div[2]/div[1]/ul/li[6]/ul/li[2]'
        self.latPagGestTpvTXT = 'TPVs'
        self.latPagGestTicXPath = '/html/body/div[2]/div[1]/ul/li[6]/ul/li[3]'
        self.latPagGestTicTXT = 'Ticket'
        self.latPagGestAvaXPath = '/html/body/div[2]/div[1]/ul/li[6]/ul/li[4]'
        self.latPagGestAvaTXT = 'Avanzada'
        self.latPagGestAjuXPath = '/html/body/div[2]/div[1]/ul/li[7]'
        self.latPagGestAjuTXT = 'Ajustes de TPV'
        self.latPagGestCamXPath = '/html/body/div[2]/div[1]/ul/li[8]'
        self.latPagGestCamTXT = 'Cambios pendientes'

        # Página principal
        self.ti2PagGestResXPath = '//*[@id="terminals-space"]/h2/text()'
        self.ti2PagGestResTXT = 'Por favor, seleccione un restaurante'

        # Restaurante seleccionado
        self.latPagGestRSeXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[8]/h4'
        self.latPagGestRSeTXT = 'LTL Consell'

        # Terminales
        self.pgpPagGestTTeXPath = '//*[@id="terminals-space"]/h2[1]'
        self.pgpPagGestTTeTXT = 'TERMINALES'

        # terminales_icono
        #self.pgpPagGestTIcXPath = '//*[@id="computerTerminals"]/div[2]/div[1]/div/i'
        self.pgpPagGestTIcXPath = '/html/body/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[1]/div/i'
        self.pgpPagGestTIcTXT = 'flaticon-monitor'

        # terminales 1,2
        self.pgpPagGestTS1XPath = '//*[@id="computerTerminals"]/div[2]/div[3]'  # Terminal 1 status
        self.pgpPagGestTS1TXT = 'DESCONECTADO'
        self.pgpPagGestTP1XPath =  '//*[@id="computerTerminals"]/div[2]/div[4]/div[1]/span'
        self.pgpPagGestTP1TXT = 'Terminal principal'
        self.pgpPagGestTC1XPath = '//*[@id="computerTerminals"]/div[2]/div[4]/div[2]/span'
        self.pgpPagGestTC1TXT = 'Terminal de cobro'
        self.pgpPagGestTc1XPath = '//*[@id="computerTerminals"]/div[2]/div[4]/div[3]/span'
        self.pgpPagGestTc1TXT = 'Terminal de cierre'
        self.pgpPagGestTD1XPath = '//*[@id="computerTerminals"]/div[2]/div[4]/div[4]/span'
        self.pgpPagGestTD1class = '//*[@id="computerTerminals"]/div[2]/div[4]/div[4]/i'
        self.pgpPagGestTD1TXT = 'Deshabilitar terminal'
        self.pgpPagGestTS2XPath = '//*[@id="computerTerminals"]/div[3]/div[3]'
        self.pgpPagGestTS2TXT = 'DESCONECTADO'
        self.pgpPagGestTP2XPath = '//*[@id="computerTerminals"]/div[3]/div[4]/div[1]/span'
        self.pgpPagGestTP2TXT = 'Terminal principal'
        self.pgpPagGestTC2XPath = '//*[@id="computerTerminals"]/div[3]/div[4]/div[2]/span'
        self.pgpPagGestTC2TXT = 'Terminal de cobro'
        self.pgpPagGestTc2XPath = '//*[@id="computerTerminals"]/div[3]/div[4]/div[3]/span'
        self.pgpPagGestTc2TXT = 'Terminal de cierre'
        self.pgpPagGestTD2XPath = '//*[@id="computerTerminals"]/div[3]/div[4]/div[4]/span'
        self.pgpPagGestTD2class = '//*[@id="computerTerminals"]/div[3]/div[4]/div[4]/i'
        self.pgpPagGestTD2TXT = 'Deshabilitar terminal'

        # Terminales móviles 1,2
        self.pgpPagGestRTMIXPath = '//*[@id="mobileTerminals"]/div[2]/div[1]/div/i'
        self.pgpPagGestRTMITXT= 'flaticon'
        #self.pgpPagGestRTMIClass = 'flaticon-smartphone'
        self.pgpPagGestRTMXPath = '//*[@id="terminals-space"]/h2[2]'
        self.pgpPagGestRTMTXT = 'TERMINALES MÓVILES'

        self.pgpPagGestRTMC1XPath = '//*[@id="mobileTerminals"]/div[2]/div[2]/div[1]/span' # Terminal movil 1
        self.pgpPagGestRTMC1TXT = 'Terminal de cobro'
        self.pgpPagGesRTMD1Xpath = '//*[@id="mobileTerminals"]/div[2]/div[2]/div[2]/span'
        self.pgpPagGesRTMD1TXT = 'Deshabilitar terminal'

        self.pgpPagGesRTMC2Xpath = '//*[@id="mobileTerminals"]/div[9]/div[2]/div[1]/span' # Terminal movil 2
        self.pgpPagGesRTMC2TXT = 'Terminal de cobro'
        self.pgpPagGesRTMC2_class = '//*[@id="mobileTerminals"]/div[8]/div[2]/div[1]/i'
        self.pgpPagGesRTMD2Xpath = '//*[@id="mobileTerminals"]/div[14]/div[2]/div[2]/span'
        self.pgpPagGesRTMD2TXT = 'Deshabilitar terminal'

        # Terminales Kitchen Display
        self.pgpPagGestRTKXPath = '//*[@id="terminals-space"]/h2[3]'
        self.pgpPagGestRTKTXT = 'TERMINALES KITCHEN DISPLAY'








