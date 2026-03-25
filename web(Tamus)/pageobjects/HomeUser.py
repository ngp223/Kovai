class HomeUser:
    def __init__(self):
        super().__init__()
        self.url = 'https://tamus.hi-iberia.es/notifications'
        self.title = 'Notificaciones'
        self.logoID = 'logo'
        # Header - Gestión
        self.gestResXPath = '/html/body/div[1]/div[3]/div[1]/div'
        self.gestResTXT = 'Gestión de Restaurantes'
        self.gestAlmXPath = '/html/body/div[1]/div[3]/div[2]/div'
        self.gestAlmTXT = 'Gestión de Almacén'
        self.gestVenXPath = '/html/body/div[1]/div[3]/div[3]/div'
        self.gestVenTXT = 'Gestión de Ventas'
        self.gestFacXPath = '/html/body/div[1]/div[3]/div[4]/div'
        self.gestFacTXT = 'Gestión de Facturación'
        self.gestUsuXPath = '/html/body/div[1]/div[3]/div[5]/div'
        self.gestUsuTXT = 'Gestión de Usuarios'
        # Header user
        self.userEyeID = 'trash'
        self.userEyeXPath = '/html/body/div[1]/div[4]/div[1]/i'
        self.userNotID = 'notifications'
        self.userNotXPath = '/html/body/div[1]/div[4]/div[2]/i'
        self.userSubUserNameTXT = 'QA Tamus'  # Según usuario
        self.userSubUserNameXPath = '/html/body/div[1]/div[4]/div[3]/div[1]/span'
        self.userSubImgUserXPath = '/html/body/div[1]/div[4]/div[3]/div[1]/i[1]'
        self.userSubDropXPath = '/html/body/div[1]/div[4]/div[3]/div[1]/i[2]'
        # Header user - Notificaciones
        self.userNotListID = 'notification-dropdown'
        self.userNotAlertTXT = 'Alertas'
        self.userNotImgAlertXPath = '/html/body/div[1]/div[4]/div[2]/div/ul/li[1]/i'
        self.userNotAlertXPath = '/html/body/div[1]/div[4]/div[2]/div/ul/li[1]/span'
        self.userNotEvenXPath = '/html/body/div[1]/div[4]/div[2]/div/ul/li[2]/span'
        self.userNotEvenTXT = 'Eventos'
        self.userNotImgEvenXPath = '/html/body/div[1]/div[4]/div[2]/div/ul/li[2]/i'
        # No deja hacer click para ver los Eventos, no parece q haga nada tal ver porque no hay ninguna
        self.userNotImgAviXPath = '/html/body/div[1]/div[4]/div[2]/div/ul/li[3]/i'
        self.userNotAviTXT = 'Avisos'
        # No deja hacer click para ver los Avisos, no parece q haga nada tal ver porque no hay ninguna
        self.userNotAviXPath = '//*[@id="notification-dropdown"]/ul/li[3]/span'
        self.userNotAllTXT = 'Ver todas'
        # No deja hacer click para ver todas
        self.userNotAllXPath = '//div[@id="notification-dropdown"]/div/span'
        # Header user - User top
        self.userSubAjuTXT = 'Ajustes'
        self.userSubAjuID = 'usermenu-settings'
        self.userSubImgAjuXPath = '/html/body/div[1]/div[4]/div[3]/div[2]/ul/li[1]/i'
        self.userSubCPssTXT = 'Cambiar contraseña'
        self.userSubCPssID = 'usermenu-password'
        self.userSubImgPssXPath = '/html/body/div[1]/div[4]/div[3]/div[2]/ul/li[2]/i'
        self.userSubClosTXT = 'Cerrar sesión'
        self.userSubClosID = 'usermenu-logout'
        self.userSubImgClosXPath = '/html/body/div[1]/div[4]/div[3]/div[2]/ul/li[3]/i'
        # Habilitar - Deshabilitar Menu Lateral
        self.imgXPath = '/html/body/div[2]/div[1]/div[1]/img'
        self.menuLatID = 'quick-menu'
        # Menu Lateral
        self.menuGlobXPath = '/html/body/div[2]/div[1]/div[2]/div[1]/h4'
        self.menuGlobTXT = 'GLOBAL'
        self.submenuGlobXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/h4'
        self.submenuGlobID = 'global'
        self.submenuGlobTXT = 'GLOBAL'
        self.submenuNotXPath = '/html/body/div[2]/div[1]/ul/li'
        self.submenuNotTXT = 'Notificaciones'
        # Menu Lateral - Listado de restaurantes - según usuario
        self.submenuLatXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/h4'
        self.submenuLatTXT = 'LATERAL'
        self.submenuLatRestID = 'restaurant_list'
        self.submenuLatRest1XPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/h4'
        # Menu Lateral - Listado de obradores - según usuario
        self.submenuObradXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/h4'
        self.submenuObradTXT = 'LOBRADOR'
        self.submenuObrID = 'restaurant_list'
        self.submenuObr1XPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/div[1]/h4'
        # Menu Lateral - Listado de papizza
        self.submenuPZZXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[5]/h4'
        self.submenuPZZTXT = 'PAPIZZA'
        self.submenuPZZID = 'restaurant_list'
        self.submenuPZZ1XPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[6]/div[1]/h4'
        # Menu Lateral - Listado de SantaGloria
        self.submenuSTGXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[7]/h4'
        self.submenuSTGTXT = 'SANTAGLORIA'
        self.submenuSTGID = 'restaurant_list'
        self.submenuSTG1XPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[8]/div[1]/h4'
        # Menu Lateral - Listado de Vezzo
        self.submenuVEZXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[9]/h4'
        self.submenuVEZTXT = 'VEZZO'
        self.submenuVEZID = 'restaurant_list'
        self.submenuVEZ1XPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[10]/div[1]/h4'
        # Menu Lateral - Listado de Volapié
        self.submenuVLPXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[11]/h4'
        self.submenuVLPTXT = 'VOLAPIÉ'
        self.submenuVLPID = 'restaurant_list'
        self.submenuVLP1XPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[12]/div[1]/h4'
        # Menu Lateral - Franquicias
        self.submenuFranqID = 'franchise'
        self.submenuFranqTXT = 'Franquicias'
        self.submenuOcuFranqXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/i'
        self.submenuMosFranqXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]/i'
        self.submenuSolFranqXPath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[3]/i'
        # Panel principal
        self.panelPpalID = 'contentcontainer'
        self.panelPpaltitleID = 'contenttitle'
        self.panelPpalMarkID = 'markNotifications'
        self.panelPpalContID = 'content'
