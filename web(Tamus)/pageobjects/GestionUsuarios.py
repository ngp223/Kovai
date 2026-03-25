import datetime
import random

class GestionUsuarios:
    def __init__(self):
        super().__init__()
        # Primeras comprobaciones: URL cargada, primer texto, título de la página
        self.url = 'https://tamus.hi-iberia.es/users/userlist'
        self.titPagGestUsuXPath = '/html/body/div[2]/div[2]/div[1]/div[1]/div'
        self.titPagGestUsuTXT = 'GESTIÓN DE USUARIOS'
        self.nomPagGestUsu = 'Gestión de Usuarios'
        self.date = datetime.datetime.today()
        self.QA = 'QANER'

        # Página principal
        self.gestUsuBusXPath = '//*[@id="userlist-action"]/div[1]'
        self.gestUsuMosXPath = '//*[@id="userlist-action"]/div[2]'
        self.gestUsuMosTXT = 'Mostrando del1al12de12usuarios'
        self.gestUsuColNyAXPath = '//*[@id="userlist-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestUsuColNyATXT = 'Nombre y apellidos'
        self.gestUsuColUsuXPath = '//*[@id="userlist-table"]/table/thead/tr[1]/th[2]/div/span'
        self.gestUsuColUsuTXT = 'Usuario'
        self.gestUsuColRolXPath = '//*[@id="userlist-table"]/table/thead/tr[1]/th[3]/div/span'
        self.gestUsuColRolTXT = 'Rol'
        self.gestUsuColResXPath = '//*[@id="userlist-table"]/table/thead/tr[1]/th[4]/div/span'
        self.gestUsuColResTXT = 'Restaurantes'
        self.gestUsuColEstXPath = '//*[@id="userlist-table"]/table/thead/tr[1]/th[5]/div/span'
        self.gestUsuColEstTXT = 'Estado'
        self.gestUsuColAccXPath = '//*[@id="userlist-table"]/table/thead/tr[1]/th[6]/div/span'
        self.gestUsuColAccTXT = 'Acciones'
        self.gestUsuEliXPath = '//*[@id="userlist-table"]/div[2]/label/div'
        self.gestUsuEliTXT = 'Mostrar usuarios eliminados'

        # Buscar
        self.gestUsuBusXPath = '//*[@id="userlist-action"]/div[1]'
        self.gestUsuBusTXT = 'Buscar:'
        self.gestUsuPalTXT = 'QA'
        self.gestUsuBusClass = 'searchInput'
        self.gestUsuRes1XPath = '//*[@id="userlist-table"]/table/tbody/tr/td[1]'
        self.gestUsuRes1TXT = 'QA Tamus'
        self.gestUsuIt1XPAth = '//*[@id="user-action"]/div[2]/span[1]'
        self.gestUsuIt1TXT = "1"

        # Opción: Exportar  --> Variables en Commons
        self.gestUsuExpDesNFTXT = 'Gesti%C3%B3n%20de%20Usuarios_' # nombre del Nuevo Fichero


        # Validar formulario
        self.gestUsuNUsID = 'newUser'
        self.gestUsuNUsTXT = 'Dar de alta'
        self.gestUsuNUTitXPath = '//*[@id="newUserModal"]/div/div[1]/span'
        self.gestUsuNUTitTXT = 'ALTA DE USUARIO'
        self.gestUsuNUNyAXPath = '//*[@id="newUserModal"]/div/form/div[1]/div[1]/label/div'
        self.gestUsuNUNyATXT = 'Nombre y apellidos*'
        self.gestUsuNUNusXPath = '//*[@id="newUserModal"]/div/form/div[1]/label/div'
        self.gestUsuNUNusTXT = 'Nombre de usuario (email)*'
        self.gestUsuNUResXPath = '//*[@id="restaurantnew-space"]/label/div[1]'
        self.gestUsuNUResTXT = 'Restaurantes*'
        self.gestUsuNURolXPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[1]'
        self.gestUsuNURolTXT = 'Rol*'
        self.gestUsuNUTESXPath = '//*[@id="newUserModal"]/div/form/div[1]/div[5]'
        self.gestUsuNUSCCoXPath = '//*[@id="newUserModal"]/div/form/div[1]/div[5]/label[1]/div'  # Sin/Con contraseña
        self.gestUsuNUECoXPath = '//*[@id="setPassword"]/div[3]/label[1]/div'  # Envío correo recordar contraseña
        self.gestUsuNUTESTXT = 'Enviar una solicitud de cambio de contraseña por correo electrónico'
        self.gestUsuNUConXPath = '//*[@id="setPassword"]/div[1]/label'
        self.gestUsuNUConTXT = 'Contraseña'
        self.gestUsuNURCoXPath = '//*[@id="setPassword"]/div[2]/label'
        self.gestUsuNURCoTXT = 'Repetir contraseña'
        self.gestUsuNUSCoXPath = '//*[@id="setPassword"]/div[3]/label[2]'
        self.gestUsuNUSCoTXT = 'Solicitar un cambio de contraseña la próxima vez que se inicie sesión'

        # Menú lateral
        self.latPagGestUUsXPath = '//*[@id="lateralmenu"]/ul/li[1]'
        self.latPagGestUUsTXT = 'Usuarios'
        self.latPagGestURoXPath = '//*[@id="lateralmenu"]/ul/li[2]'
        self.latPagGestURoTXT = 'Roles'

        # Desplegable de rol
        self.gestUsuNURoXPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select'
        self.gestUsuNURo1XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[2]'
        self.gestUsuNURo1TXT = 'Administrador'
        self.gestUsuNURo2XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[3]'
        self.gestUsuNURo2TXT = 'Gestor global'
        self.gestUsuNURo3XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[4]'
        self.gestUsuNURo3TXT = 'Gestor global limitado'
        self.gestUsuNURo4XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[5]'
        self.gestUsuNURo4TXT = 'Gestor global con PowerBi'
        self.gestUsuNURo5XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[6]'
        self.gestUsuNURo5TXT = 'Gestor global limitado con PowerBi'
        self.gestUsuNURo6XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[7]'
        self.gestUsuNURo6TXT = 'Gestor de restaurante'
        self.gestUsuNURo7XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[8]'
        self.gestUsuNURo7TXT = 'Gestor de almacén'
        self.gestUsuNURo8XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[9]'
        self.gestUsuNURo8TXT = 'Gestor de ventas'
        self.gestUsuNURo9XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[10]'
        self.gestUsuNURo9TXT = 'Gestor de facturación'
        self.gestUsuNURo10XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[11]'
        self.gestUsuNURo10TXT = 'Gestor de negocio'
        self.gestUsuNURo11XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[12]'
        self.gestUsuNURo11TXT = 'Gestor de usuarios'
        self.gestUsuNURo12XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[13]'
        self.gestUsuNURo12TXT = 'Gestor de sincronización'
        self.gestUsuNURo13XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[14]'
        self.gestUsuNURo13TXT = 'Gestor de restaurantes y stock'
        self.gestUsuNURo14XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[15]'
        self.gestUsuNURo14TXT = 'Gestor de almacén y ventas'
        self.gestUsuNURo15XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[16]'
        self.gestUsuNURo15TXT = 'Almacén-Ventas-Facturación'
        self.gestUsuNURo16XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[17]'
        self.gestUsuNURo16TXT = 'Analista de ventas con PowerBI'
        self.gestUsuNURo17XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[18]'
        self.gestUsuNURo17TXT = 'Área Manager'
        self.gestUsuNURo18XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[19]'
        self.gestUsuNURo18TXT = 'Controller'
        self.gestUsuNURo19XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[20]'
        self.gestUsuNURo19TXT = 'Departamento Financiero'
        self.gestUsuNURo20XPath = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[21]'
        self.gestUsuNURo20TXT = 'Formación'
        # hay más, pero se comprueban los 20 primeros

        # Ordenar columnas
        self.gestUsuColOrdXPath = '//*[@id="userlist-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestUsuCol1elXPath = '//*[@id="userlist-table"]/table/tbody/tr[1]/td[1]'
        self.gestUsuCol1elTXT = 'Comercia'
        self.gestUsuColUelXPath = '//*[@id="userlist-table"]/table/tbody/tr[12]/td[1]'
        self.gestUsuColUelTXT = 'Víctor Vázquez'

        # Opción: Rellenar formulario

        self.gestUsuNUsOKXPath = '//*[@id="newUserModal"]/div/form/div[3]/button[2]'
        self.gestUsuNUsOKTXT = 'Aceptar'
        self.gestUsuNUsKOXPath = '//*[@id="newUserModal"]/div/form/div[3]/button[1]'
        self.gestUsuNUsKOTXT = 'Cancelar'
        self.gestUsuNUsNyAInput = '//*[@id="newUserModal"]/div/form/div[1]/div[1]/label/input'
        self.gestUsuNUsNyAValor = self.QA + '{:%d%m%y%H%M}'.format(self.date)
        self.gestUsuNUsUsuInput = '//*[@id="newUserModal"]/div/form/div[1]/label/input'
        self.gestUsuNUsResMen = '//*[@id="restaurantnew-space"]/label/input[1]'
        self.gestUsuNUsResSel = '//*[@id="restaurantnew-space"]/label/div[2]/div[7]/div[1]/div[1]'
        self.gestUsuNUsExp = '//*[@id="restaurantnew-space"]/label/div[2]/div[1]/span[1]'  # Expandir
        self.gestUsuNUsCon = '//*[@id="restaurantnew-space"]/label/div[2]/div[1]/span[1]'  # Contraer
        self.gestUsuNUsRolInput = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]'
        self.gestUsuNUsRolValor = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[12]'
        self.gestUsuNUsPWDInput = '//*[@id="setPassword"]/div[1]/label/input'
        self.gestUsuNUsPWDValor = 'QANERpwd1!'
        self.gestUsuNUsPWD2Input = '//*[@id="setPassword"]/div[2]/label/input'
        self.gestUsuNUsPWD2Valor = 'QANERpwd1!'
        self.gestUsuNUsSPWDInput = '//*[@id="newUserModal"]/div/form/div[1]/div[5]/label[2]'
        self.gestUsuNUsSPWDInput = 'Enviar una solicitud de cambio de contraseña por correo electrónico'
        self.gestUsuNUsXPath = '//*[@id="userlist-table"]/table/tbody/tr[8]/td[1]'  # Nuevo usuario
        self.gestUsuOpEdiXPath = '//*[@id="userlist-table"]/table/tbody/tr[8]/td[6]/i[1]'  # Opción Editar

        # self.gestUsuEdiTXT = 'Editar'
        self.gestUsuEdiTitXPath = '//*[@id="editUserModal"]/div/div[1]/span'
        self.gestUsuEdiTitTXT = 'MODIFICAR USUARIO'
        self.gestUsuEdiUsDXPath = '//*[@id="editUserModal"]/div/form/div[1]/div[1]/label/div/span'  # Usuario deshabilitado
        self.gestUsuEdiUsDTXT = 'Usuario deshabilitado'
        #self.gestUsuEdiUsITXT = 'Usuario deshabiitado'  # icono
        self.gestUsuEdiNyAXPath = '//*[@id="editUserModal"]/div/form/div[1]/div[2]/label/div'
        self.gestUsuEdiNyATXT = 'Nombre y apellidos*'
        self.gestUsuEdiNUsXPath = '//*[@id="editUserModal"]/div/form/div[1]/div[3]/label/div'
        self.gestUsuEdiNUsTXT = 'Nombre de usuario (email)*'
        self.gestUsuEdiResXPath = '//*[@id="restaurantedit-space"]/label/div[1]'
        self.gestUsuEdiExpXPath = '//*[@id="restaurantedit-space"]/label/div[2]/div[1]/span[1]'
        self.gestUsuEdiConXPath = '//*[@id="restaurantedit-space"]/label/div[2]/div[1]/span[2]'
        self.gestUsuEdiResTXT = 'Restaurantes*'
        self.gestUsuEdiResSel = '//*[@id="restaurantnew-space"]/label/div[2]/div[9]/div[1]/div[1]'
        self.gestUsuEdiRolXPath = '//*[@id="editUserModal"]/div/form/div[1]/div[5]/label/div[1]'
        self.gestUsuEdiRolTXT = 'Rol*'
        self.gestUsuEdiRolSel = '//*[@id="newUserModal"]/div/form/div[1]/div[4]/label/div[2]/select/option[10]'
        self.gestUsuEdiOKXPath = '//*[@id="editUserModal"]/div/form/div[3]/button[2]'
        self.gestUsuEdiOKTXT = 'Aceptar'
        self.gestUsuEdiKOXPath = '//*[@id="editUserModal"]/div/form/div[3]/button[1]'
        self.gestUsuEdiKOTXT = 'Cancelar'
        self.gestUsuEdiNyAInput = '//*[@id="name"]'
        self.gestUsuEdiNyAValor = self.QA + '{:%d%m%y%H%M}'.format(self.date)
        self.gestUsuEdiResInput = '//*[@id="restaurantedit-space"]/label/input[1]'
        self.gestUsuEdiResSel = '//*[@id="restaurantedit-space"]/label/div[2]/div[3]/div[6]/div'
        self.gestUsuEdiResValor = 'LTL Castellana 42' ## falta comprobar este valor
        self.gestUsuEdiRolInput = '//*[@id="editUserModal"]/div/form/div[1]/div[5]/label/div[2]'
        self.gestUsuEdiRolSel = '//*[@id="editUserModal"]/div/form/div[1]/div[5]/label/div[2]/select/option[5]'
        self.gestUsuEdiRolValor = 'Gestor global limitado'

        # Opción: Cambiar contraseña
        self.gestUsuOpCPWDXPath = '//*[@id="userlist-table"]/table/tbody/tr[8]/td[6]/i[2]'
        self.gestUsuCPWDTitXPath = '//*[@id="changePasswordModal"]/div/div[1]/span'
        self.gestUsuCPWDTitTXT = 'CAMBIAR CONTRASEÑA'
        self.gestUsuCPWDOKXPath = '//*[@id="changePasswordModal"]/div/form/div[3]/button[2]'
        self.gestUsuCPWDOKTXT = 'Aceptar'
        self.gestUsuCPWDKOXPath = '//*[@id="changePasswordModal"]/div/form/div[3]/button[1]'
        self.gestUsuCPWDKOTXT = 'Cancelar'
        self.gestUsuOpCPWDmesXPath = '//*[@id="newUserModal"]/div/div[2]/span'
        self.gestUsuOpCPWDmesTXT = 'La contraseña debe tener una longitud de al menos 8 caracteres y contener una mayúscula, una minúscula y un número. Caracteres no permitidos: , ; & |'
        self.gestUsuOpCPWDConXPath = '//*[@id="setPasswordChange"]/div[1]/label'
        self.gestUsuOpCPWDConTXT = 'Contraseña'
        self.gestUsuOpCPWDConInput = '//*[@id="setPasswordChange"]/div[1]/label/input'
        self.gestUsuOpCPWDConValor = 'QANERpwd2!'
        self.gestUsuOpCPWDRCoXPath = '//*[@id="setPasswordChange"]/div[2]/label'
        self.gestUsuOpCPWDRCoTXT = 'Repetir contraseña'
        self.gestUsuOpCPWDRCoInput = '//*[@id="setPasswordChange"]/div[2]/label/input'
        self.gestUsuOpCPWDRCoValor = 'QANERpwd2!'

        # Opción: Eliminar
        self.gestUsuOpDelXPath = '//*[@id="userlist-table"]/table/tbody/tr[8]/td[6]/i[3]'
        self.gestUsuOpDelTitXPath = '//*[@id="deleteUserModal"]/div/div[1]/span'
        self.gestUsuOpDelTitTXT = 'BAJA DE USUARIO'
        self.gestUsuOpDelTi2XPath = '//*[@id="deleteUserModal"]/div/form/div[1]/p'
        self.gestUsuOpDelTi2TXT = '¿Está seguro que desea dar de baja al usuario?'
        self.gestUsuOpDelOKXPath = '//*[@id="deleteUserModal"]/div/form/div[3]/button[2]'
        self.gestUsuOpDelOKTXT = 'Aceptar'
        self.gestUsuOpDelKOXPath = '//*[@id="deleteUserModal"]/div/form/div[3]/button[1]'
        self.gestUsuOpDelKOTXT = 'Cancelar'

        # Roles, PagPrincipal
        self.gestUsuRoltitXPath = '//*[@id="contenttitle"]/div[1]/div'
        self.gestUsuRoltitTXT = 'GESTIÓN DE ROLES'
        self.gestUsuRolCreID = 'newRole'
        self.gestUsuRolCreTXT = 'Crear rol'
        self.gestUsuColSRolXPath = '//*[@id="role-header"]/div/div/label/span'
        self.gestUsuColSRolTXT = 'Rol'
        self.gestUsuColPerXPath = '//*[@id="role-lines"]/table/thead/tr[1]/th[1]/div/span'
        self.gestUsuColPerTXT = 'Permisos'
        self.gestUsuColAcnXPath = '//*[@id="role-lines"]/table/thead/tr[1]/th[2]/div/span'
        self.gestUsuColAcnTXT = 'Acción'
        self.gestUsuColAcsXPath = '//*[@id="role-lines"]/table/thead/tr[1]/th[3]/div/span'
        self.gestUsuColAcsTXT = 'Acciones'

        # Crear rol
        self.gestUsuCreRolTitXPath = '//*[@id="newRoleModal"]/div/div[1]/span'
        self.gestUsuCreRolTitTXT = 'CREAR ROL'
        self.gestUsuCreRolNomXPath = '//*[@id="newRoleModal"]/div/form/div[1]/div[1]/label/div'
        self.gestUsuCreRolNomTXT = 'Nombre*'
        self.gestUsuCreRolNomInput = '//*[@id="newRoleModal"]/div/form/div[1]/div[1]/label/input'
        self.gestUsuCreRolNomValor = self.QA + '{:%d%m%y%H%M}'.format(self.date) + 'rol'
        self.gestUsuCreRolCloXPath = '//*[@id="newRoleModal"]/div/form/div[1]/div[2]/label/div[1]'
        self.gestUsuCreRolCloTXT = 'Clonar desde:*'
        self.gestUsuCreRolCloInput = '//*[@id="roleSelect"]/select/option[17]'
        self.gestUsuCreRolKOXPath = '//*[@id="newRoleModal"]/div/form/div[3]/button[1]'
        self.gestUsuCreRolKOTXT = "Cancelar"
        self.gestUsuCreRolOKXPath = '//*[@id="newRoleModal"]/div/form/div[3]/button[2]'
        self.gestUsuCreRolOKTXT = "Aceptar"
        self.gestUsuNewRolXPath = '//*[@id="role-header"]/div/div[1]/label/div/select/option[41]'
        self.gestUsuNewRolrenXPath = '//*[@id="role-header"]/div/div[1]/label/div/select/option[42]'

        # Roles, seleccionar rol, renombrar rol seleccionado, borrar rol seleccionado
        self.gestUsuRolSelXPath = '//*[@id="role-header"]/div/div/label/div/select' # seleccionar rol
        self.gestUsuRolOKXPath = '//*[@id="role-header"]/div/div[1]/label/div/select/option[18]'
        self.gestUsuRolOKTXT = 'Gerente Local'
        self.gestUsuRolDelID = 'deleteRole'  # Eliminar rol
        self.gestUsuRolDelTXT = "Eliminar"
        self.gestUsuRolRenID = 'editRole'  # Renombrar rol
        self.gestUsuRolRenTXT = "Renombrar"
        self.gestUsuRolRenTitleXPath = '//*[@id="renameRoleModal"]/div/div[1]/span'
        self.gestUsuRolRenTitleTXT = 'RENOMBRAR'
        self.gestUsuRolRenNomXPath = '//*[@id="renameRoleModal"]/div/form/div[1]/div/label/div'
        self.gestUsuRolRenNomTXT = 'Nombre*'
        self.gestUsuRolRenInput = '//*[@id="renameRoleModal"]/div/form/div[1]/div/label/input'
        self.gestUsuRolRenNomKOXPath = '//*[@id="renameRoleModal"]/div/form/div[3]/button[1]'
        self.gestUsuRolRenNomKOTXT = 'Cancelar'
        self.gestUsuRolRenNomOKXPath = '//*[@id="renameRoleModal"]/div/form/div[3]/button[2]'
        self.gestUsuRolRenNomOKTXT = 'Aceptar'
        self.gestUsuRolDelTitleXPath = '//*[@id="deleteRoleModal"]/div/div[1]'
        self.gestUsuRolDelTitleTXT = 'ELIMINAR ROL'
        self.gestUsuRolDelTextXPath = '//*[@id="deleteRoleModal"]/div/form/div[1]/p[1]'
        self.gestUsuRolDelTextTXT = '¿Está seguro de querer eliminar este rol?'
        self.gestUsuRolDelNomXPath = '//*[@id="deleteRoleModal"]/div/form/div[1]/p[2]'
        self.gestUsuRolDelNomKOXPath = '//*[@id="deleteRoleModal"]/div/form/div[3]/button[1]'
        self.gestUsuRolDelNomKOTXT = 'Cancelar'
        self.gestUsuRolDelNomOKXPath = '//*[@id="deleteRoleModal"]/div/form/div[3]/button[2]'
        self.gestUsuRolDelNomOKTXT = 'Aceptar'


        # Roles, página principal con Rol seleccionado
        self.gestUsuMLRSFPXPath = '//*[@id="role-form"]/label/span'
        self.gestUsuMLRSFPTXT = 'Filtrar permisos'
        self.gestUsuMLRSFPInput = '//*[@id="role-form"]/label/div/input'
        self.gestUsuMLRSFPValor = 'S'
        self.gestUsuMLRSPerXpath = '//*[@id="role-form"]/form/label[1]/span'
        self.gestUsuMLRSPerTXT = 'Permiso'
        self.gestUsuMLRSPerID = 'permissionSelect'
        self.gestUsuMLRSPerValor = '//*[@id="permissionSelect"]/select/option[17]'
        self.gestUsuMLRSPerTXT = 'Gestión de Almacén > Recetas > Combos'
        self.gestUsuMLRSAccID = 'actionSelect'
        self.gestUsuMLRSAccTXT = 'Lectura'
        self.gestUsuMLRSAccValor = '//*[@id="actionSelect"]/select/option[3]'
        self.gestUsuMLRSAPInput = '//*[@id="role-form"]/form/input'  # añadir permiso
        self.gestUsuMLRSAPTXT = 'Añadir permiso'
        self.gestUsuMLRSGuaID = 'saveChanges'
        self.gestUsuMLRSGuaXPath = '//*[@id="saveChanges"]'
        self.gestUsuMLRSGuaTXT = 'Guardar cambios'
        self.gestUsuMLRSMRoTitXPath = '//*[@id="saveRoleModal"]/div/div[1]/span'
        self.gestUsuMLRSMRoTitTXT = 'MODIFICAR ROL'
        self.gestUsuMLRSMRoTexXPath = '//*[@id="saveRoleModal"]/div/form/div[1]/p'
        self.gestUsuMLRSMRoTexTXT = '¿Está seguro de querer modificar este rol? Este cambio afectará a todos los usuarios que lo tengan asignado.'
        self.gestUsuMLRSMRoCanXPath = '//*[@id="saveRoleModal"]/div/form/div[3]/button[1]'
        self.gestUsuMLRSMRoCanTXT = 'Cancelar'
        self.gestUsuMLRSMRoModXPath = '//*[@id="saveRoleModal"]/div/form/div[3]/button[2]'
        self.gestUsuMLRSMRoModTXT = 'Modificar'
        self.gestUsuMLRSPAXPath = '//*[@id="role-lines"]/table/tbody/tr[17]/td[1]'  # Rol seleccionado, permiso añadido
        self.gestUsuMLRSPAAXPath = '//*[@id="role-lines"]/table/tbody/tr[17]/td[2]'  # Rol seleccionado, acción del permiso añadido
        self.gestUsuMLRSPAEXPath = '//*[@id="actions"]/i'  # Eliminar Permiso añadido al rol




