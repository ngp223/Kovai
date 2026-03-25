import datetime
import random


class GestionFacturacion:
    def __init__(self):
        super().__init__()
        # Primeras comprobaciones: URL cargada, primer texto, título de la página
        self.url = 'https://tamus.hi-iberia.es/invoicing/clients'
        self.titPagGestFacXPath = '/html/body/div[2]/div[2]/div[1]/div[1]/div'
        self.titPagGestFacTXT = 'LISTADO DE CLIENTES' ## borrar variable está repetida
        self.nomPagGestFac = 'Gestión de Facturación - Listado de clientes'
        self.date = datetime.datetime.today()
        self.QA = 'QANER'

        # Página principal Cabecera ¿¿quitar variables exportarr??
        self.gestFacExpID = 'excelExport'
        self.gestFacExpTXT = 'Exportar'
        self.gestFacNclID = 'newClient'
        self.gestFacNclTXT = 'Nuevo cliente'

        # Columnas
        self.gestFacMCo1XPath = '//*[@id="clients-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestFacMCo2XPath = '//*[@id="clients-table"]/table/thead/tr[1]/th[2]/div/span'
        self.gestFacMCo3XPath = '//*[@id="clients-table"]/table/thead/tr[1]/th[3]/div/span'
        self.gestFacMCo4XPath = '//*[@id="clients-table"]/table/thead/tr[1]/th[4]/div/span'
        self.gestFacMCo5XPath = '//*[@id="clients-table"]/table/thead/tr[1]/th[5]/div/span'
        self.gestFacMCo6XPath = '//*[@id="clients-table"]/table/thead/tr[1]/th[6]/div/span'
        self.gestFacMCo7XPath = '//*[@id="clients-table"]/table/thead/tr[1]/th[7]/div/span'
        self.gestFacMCo8XPath = '//*[@id="clients-table"]/table/thead/tr[1]/th[8]/div/span'
        self.gestFacMCo9XPath = '//*[@id="clients-table"]/table/thead/tr[1]/th[9]/div/span'
        self.gestFacMCo10XPath ='//*[@id="clients-table"]/table/thead/tr[1]/th[10]/div/span'
        self.gestFacMCoNIFTXT = 'NIF/CIF'
        self.gestFacMCoNomTXT = 'Nombre'
        self.gestFacMCoEmaTXT = 'Email'
        self.gestFacMCoTelTXT = 'Teléfono'
        self.gestFacMCoDirTXT = 'Dirección'
        self.gestFacMCoCiuTXT = 'Ciudad'
        self.gestFacMCoProTXT = 'Provincia'
        self.gestFacMCoCPTXT = 'C.P.'
        self.gestFacMCoPaiTXT = 'País'
        self.gestFacMCoAccTXT = 'Acciones'

        # Buscar, más columnas
        self.gestFacBusXPath = '//*[@id="clients-action"]/div[1]'
        self.gestFacBusTXT = 'Buscar:'
        self.gestFacPalTXT = 'bloom'  # palabra a buscar
        self.gestFacBusClass = 'searchInput'
        self.gestFacIt1XPAth = '//*[@id="clients-action"]/div[2]/span[1]'
        self.gestFacIt1TXT = "1"
        self.gestFacItnXPAth = '//*[@id="clients-action"]/div[2]/span[2]'
        self.gestFacItnTXT = "2"
        self.gestFacCol1elXPath = '//*[@id="clients-table"]/table/tbody/tr[1]/td[2]/span'
        self.gestFacCol1elTXT = 'BLOOM CONSULTING'
        self.gestFacColUelXPath = '//*[@id="clients-table"]/table/tbody/tr[2]/td[2]/span'
        self.gestFacColUelTXT = 'Bloom Effi SL'
        self.gestFacResXPath = '//*[@id="clients-action"]/div[2]'
        self.gestFacResTXT = 'Mostrando del1al2de2clientes'
        self.gestFacRes1XPath = '//*[@id="clients-table"]/table/tbody/tr[1]/td[2]'
        self.gestFacRes2XPath = '//*[@id="clients-table"]/table/tbody/tr[2]/td[2]'

        # Opción: mostrar más columnas
        self.gestFacMCoXPath = '//*[@id="clients-table"]/div[2]/label/div'  # Mostrar mas columnas
        self.gestFacMCoTXT = 'Mostrar más columnas'
        self.gestFacMMCConXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/i'  # configuración Mostrar más columnas
        self.gestFacMMCNomXPath = '//*[@id="columnsModal"]/div/form/div[1]/div[1]/div[1]/label/div'
        self.gestFacMMCGuaXPath = '//*[@id="columnsModal"]/div/form/div[3]/button[2]'  # Guardar cambios en Mas columnas
        self.gestFacMMCCanXPath = '//*[@id="columnsModal"]/div/form/div[3]/button[1]'  # Cancelar cambios en Mas columnas

        # Formulario Nuevo cliente
        self.gestFacNCFTitXPath = '//*[@id="newClientModal"]/div/div[1]'
        self.gestFacNCFTitTXT = 'NUEVO CLIENTE'
        self.gestFacNCFNomXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[1]/label/div'
        self.gestFacNCFNomTXT = 'Nombre*'
        self.gestFacNCFNIFXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[2]/div[1]/label/div'
        self.gestFacNCFNIFTXT = 'NIF/CIF*'
        self.gestFacNCFTelXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[2]/div[2]/label'
        self.gestFacNCFTelTXT = 'Teléfono'
        self.gestFacNCFEmaXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[3]/label'
        self.gestFacNCFEmaTXT = 'Email'
        self.gestFacNCFDirXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[4]/label/div'
        self.gestFacNCFDirTXT = 'Dirección*'
        self.gestFacNCFCiuXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[5]/div[1]/div'
        self.gestFacNCFCiuTXT = 'Ciudad*'
        self.gestFacNCFProXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[5]/div[2]/div'
        self.gestFacNCFProTXT = 'Provincia*'
        self.gestFacNCFCPXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[6]/div[1]/label/div'
        self.gestFacNCFCPTXT = 'Código postal*'
        self.gestFacNCFPaiXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[6]/div[2]/label/div[1]'
        self.gestFacNCFPaiTXT = 'País*'
        self.gestFacNCFConXPath ='//*[@id="newClientModal"]/div/form/div[1]/div[7]/label'
        self.gestFacNCFConTXT = 'Contabilidad'
        self.gestFacNCFOKXPath = '//*[@id="newClientModal"]/div/form/div[3]/button[2]'
        self.gestFacNCFOKTXT = 'Aceptar'
        self.gestFacNCFKOXPath = '//*[@id="newClientModal"]/div/form/div[3]/button[1]'
        self.gestFacNCFKOTXT = 'Cancelar'

        # Rellenar Formulario Nuevo Cliente
        self.gestFacNCFNomInput =  '//*[@id="newClientModal"]/div/form/div[1]/div[1]/label/input'
        self.gestFacNCFNomValor = self.QA + '{:%d%m%y%H%M}'.format(self.date) + '_nombre'
        self.gestFacNCFNIFInput = '//*[@id="newClientModal"]/div/form/div[1]/div[2]/div[1]/label/input'
        self.gestFacNCFNIFValor = '45772264X'
        self.gestFacNCFTelInput = '//*[@id="newClientModal"]/div/form/div[1]/div[2]/div[2]/label/input'
        self.gestFacNCFTelValor = '983112233'
        self.gestFacNCFEmaInput = '//*[@id="newClientModal"]/div/form/div[1]/div[3]/label/input'
        self.gestFacNCFEmaValor = self.gestFacNCFNomValor + '@email.es'
        self.gestFacNCFDirInput = '//*[@id="newClientModal"]/div/form/div[1]/div[4]/label/input'
        self.gestFacNCFDirValor = 'Dirección de ' + self.QA
        self.gestFacNCFCiuInput = '//*[@id="newClientModal"]/div/form/div[1]/div[5]/div[1]/div/input'
        self.gestFacNCFCiuValor = 'Fuensaldaña'
        self.gestFacNCFProInput = '//*[@id="newClientModal"]/div/form/div[1]/div[5]/div[2]/div/input'
        self.gestFacNCFProValor = 'Valladolid'
        self.gestFacNCFCPInput = '//*[@id="newClientModal"]/div/form/div[1]/div[6]/div[1]/label/input'
        self.gestFacNCFCPValor = '47123'
        self.gestFacNCFSePXPath = '//*[@id="newClientModal"]/div/form/div[1]/div[6]/div[2]/label/div[2]/select'
        self.gestFacNCFPaiInput = '//*[@id="newClientModal"]/div/form/div[1]/div[6]/div[2]/label/div[2]/select/option[1]'
        self.gestFacNCFPaiValor = 'España'
        self.gestFacNCFConInput = '//*[@id="newClientModal"]/div/form/div[1]/div[7]/label/input'
        self.gestFacNCFConValor = 'Contabilidad de ' + self.QA


        # Menú lateral
        self.latPagGestFClXPath = '//*[@id="lateralmenu"]/ul/li[1]'
        self.latPagGestFClTXT = 'Clientes'
        self.latPagGestFFaXPath = '//*[@id="lateralmenu"]/ul/li[2]/div'
        self.latPagGestFFaTXT = 'Facturas'
        self.latPagGestFFSXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[1]'
        self.latPagGestFFSTXT = 'Facturas simplificadas'
        self.latPagGestFFCXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[2]'
        self.latPagGestFFCTXT = 'Facturas completas'
        self.latPagGestFFJXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[3]'
        self.latPagGestFFJTXT = 'Facturas de canje'
        self.latPagGestFFRXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[4]'
        self.latPagGestFFRTXT = 'Facturas rectificativas'
        self.latPagGestFFPXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[5]'
        self.latPagGestFFPTXT = 'Facturas recapitulativas'
        self.latPagGestFFEXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[6]'
        self.latPagGestFFETXT = 'Entregas a cuenta'

        # Avanzar/retroceder página
        self.gestFacAvPXPath = '//*[@id="clients-table"]/div[1]/div/div/ul/li[13]/a'
        # self.gestFacAvPTXT = '>>'
        self.gestFacRePXPath = '//*[@id="clients-table"]/div[1]/div/div/ul/li[1]/a'
        # self.gestFacRePTXT = '<<'
        self.gestFacPg5XPath = '//*[@id="clients-table"]/div[1]/div/div/ul/li[6]/a'
        self.gestFacPg5TXT = '5'
        self.gestFacPg1XPath = '//*[@id="clients-table"]/div[1]/div/div/ul/li[2]/a'
        self.gestFacPg1TXT = '1'
        self.gestFacMosXPath = '//*[@id="clients-action"]/div[2]'
        self.gestFacMP1TXT = 'Mostrando del1al20de8034clientes'
        self.gestFacMP2TXT = 'Mostrando del21al40de8034clientes'
        self.gestFacMP3TXT = 'Mostrando del41al60de8034clientes'
        self.gestFacMP4TXT = 'Mostrando del61al80de8034clientes'
        self.gestFacMP5TXT = 'Mostrando del81al100de8034clientes'
        self.gestFacRePXPath = '//*[@id="clients-table"]/div[1]/div/div/ul/li[1]/a'

        # EXPORTAR --> Variables en Commons
        self.gestFacExpDesNFTXT = 'Listado%20de%20clientes_'  # Descarga de la exportacion del Nuevo Fichero
        self.gestFacExpDesLisTXT = 'Listado de clientes'

