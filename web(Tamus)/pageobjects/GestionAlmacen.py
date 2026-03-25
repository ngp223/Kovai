import datetime
import random
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta

class GestionAlmacen:
    def __init__(self):
        super().__init__()
        # Primeras comprobaciones: URL cargada, primer texto, título de la página
        self.url = 'https://tamus.hi-iberia.es/stock/provider'
        self.QA = 'QANER'
        self.proveedor = '1QANER_NOBORRAR'  # proveedor creado fijo para trabajar con el
        self.datetime = datetime.datetime.today()
        self.diasem = self.datetime.weekday() # devuelve 0 para el lunes
        self.hoy = '{:%d/%m/%Y}'.format(self.datetime)
        #self.hoymas2 = self.datetime + timedelta(minutes=2)
        #.self.ajustehoy = '{:%d/%m/%Y %H:%M}'.format(self.hoymas2) # ajuste del desfase horario de la máquina
        self.hoymenos15d = self.datetime + timedelta(days=-15)
        self.ajustequincena = '{:%d/%m/%Y}'.format(self.hoymenos15d)
        self.hoymas7d = self.datetime + timedelta(days=7)
        self.ajustesemana = '{:%d/%m/%Y}'.format(self.hoymas7d)
        self.hoymenos1mes = self.datetime + relativedelta(months=-1)
        self.menos1mes = '{:%d/%m/%Y}'.format(self.hoymenos1mes)
        self.hoymenos3mes = self.datetime + relativedelta(months=-3)
        self.menos3mes = '{:%d/%m/%Y}'.format(self.hoymenos3mes)

        self.gestAlmFec1Valor = self.menos3mes + ' - ' + self.hoy
        self.gestAlmFec2Valor = self.menos1mes + ' - ' + self.hoy
        self.gestAlmFec3Valor = self.ajustequincena + ' - ' + self.ajustesemana

        self.titPagGestAlmXPath = '/html/body/div[2]/div[2]/div[1]/div[1]/div'
        self.gestAlmBusInput = '//*[@id="rawproduct-action"]/div[1]/div[1]/input'  # Input Buscar
        self.gestAlmLisTitXPath = '//*[@id="contenttitle"]/div[1]/div[1]' #Listado de Almacenes, Inventarios, Unidades, Traspasos y salidas, Descuadres,Pedidos,Albaranes..
        self.gestAlmTitCreXPath = '//*[@id="contenttitle"]/div[1]/div[2]'  # título de: CREACION DE CATÁLOGO/STOCK EN ALMACÉN/Inventario/PEDIDO/ALBARÁN
        self.gestALPEDTitXPath = '//*[@id="contenttitle"]/div[1]/div' # COMPRAS EXTERNAS, RECETAS..
        self.gestAlmCSGKOXPath = '//*[@id="unsavedModal"]/div/form/div[3]/button[1]' # Cancelar'
        self.gestAlmVSGXPath = '//*[@id="unsavedModal"]/div/form/div[3]/button[2]' # Aceptar/Volversinguardar
        self.gestAlmGVXPath = '//*[@id="unsavedModal"]/div/form/div[3]/button[3]'  # Guardar y volver
        self.gestAlmCSGTit2XPath = '//*[@id="unsavedModal"]/div/form/div[1]/p' #Hay cambios sin guardar. ¿Está seguro que desea salir de la página/volver sin guardar?
        self.gestAlmCSGTit2SPTXT = 'Hay cambios sin guardar. ¿Está seguro que desea salir de la página?'
        self.gestAlmCSGTit2VSGTXT = 'Hay cambios sin guardar. ¿Está seguro que desea volver sin guardar?'
        self.nomPagGestAlm = 'Gestión de Almacén - Listado de proveedores'
        self.titPagGestAlmTXT = 'LISTADO DE PROVEEDORES'
        self.gestAlmFProvTitTXT = 'LISTADO DE FACTURAS DE PROVEEDOR'
        self.gestAlmFProdTitTXT = 'LISTADO DE PRODUCTOS'
        self.gestAlmCAtTitTXT = 'LISTADO DE CATÁLOGOS'
        self.gestAlmIngTitTXT = 'LISTADO DE INGREDIENTES'
        self.gestAlmCategTitTXT = 'LISTADO DE CATEGORÍAS'
        self.gestAlmUnitTitTXT = 'LISTADO DE UNIDADES'
        self.gestAlmAlmTitTXT = 'LISTADO DE ALMACENES'
        self.gestAlmInvTitTXT = 'LISTADO DE INVENTARIOS'

        self.gestAlmNProvID = 'newProvider'
        self.gestAlmNItemID = 'newRawProduct' # Nuevo producto/ingrediente
        self.gestAlmGItemID = 'saveRawproduct'
        self.gestAlmMPCatNewID = 'newCatalogue'
        self.gestAlmMPCategNewID = 'newCategory'
        self.gestAlmFPNueFacID = 'newInvoice' # Nueva factura
        self.gestAlmNInvID = 'newInventory' # Nuevo inventario
        self.gestAlmPEDNPedID = 'newDelivery'
        self.gestAlmNPedOKID ='summaryPurchaseOrder' # Nuevo pedido
        self.gestAlmNCEOKID = '' # Compra externa
        self.gestAlmNProvTXT = 'Nuevo proveedor'
        self.gestAlmNProdTXT = 'Nuevo producto'
        self.gestAlmPEDNPedTXT = 'Nuevo pedido'
        self.gestAlmPEDNAlbTXT = 'Nuevo albarán'
        self.gestAlmAllTXT = 'Todas'
        self.gestAlmMarTXT = 'Marcas'
        self.gestAlmMar2TXT = 'Marcas:'
        self.gestAlmConTXT = 'Contabilidad'
        self.gestAlmCatTXT = 'Catálogos'
        self.gestAlmCat2TXT = 'Catálogo'
        self.gestAlmCategTXT = 'Categoría'
        self.gestAlmCateg2TXT = 'Categoría*'
        self.gestAlmMCoTXT = 'Mostrar más columnas'
        self.gestAlmIngTXT = 'INGREDIENTES'
        self.gestAlmIng2TXT = 'Ingredientes'
        self.gestAlmIng3TXT = 'Ingrediente:'
        self.gestAlmIng4TXT = 'Ingrediente'
        self.gestAlmSRecTXT = 'SUBRECETAS'
        self.gestAlmSRec2TXT = 'Subrecetas'
        self.gestAlmVarTXT = 'Variación'
        self.gestAlmVar2TXT = 'Variación (%)'
        self.gestAlmVarMTXT = 'Variación media'
        self.gestAlmVarM2TXT = 'Variación media (%)'
        self.gestAlmStCan1TXT = 'Cancelado'
        self.gestAlmStCan2TXT = 'Cancelados'
        self.gestAlmStDevTXT = 'Devolución'
        self.gestAlmStEntTXT = 'Entrega'
        self.gestAlmStOtrosTXT = 'Otros'
        self.gestAlmStRechTXT = 'Rechazado'
        self.gestAlmStBorTXT = 'Borradores'
        self.gestAlmStBor2TXT = 'Borrador'
        self.gestAlmStPteTXT = 'Pendiente'
        self.gestAlmStEPTXT = 'En proceso'
        self.gestAlmStComTXT = 'Completado'
        self.gestAlmMP1TXT = 'Materias primas'
        self.gestAlmMP2TXT = 'Materias primas:'
        self.gestAlmPedTXT = 'PEDIDO'
        self.gestAlmCrePorTXT = 'Creado por'
        self.gestAlmFecIniTXT = 'Fecha inicio*'
        self.gestAlmFecFinTXT = 'Fecha fin*'
        self.gestAlMERAISFFTXT = 'Fecha fin*'
        self.gestAlmSelTXT = 'LTL Fleming'
        self.gestAlmSel2TXT = '(9) LTL Fleming'
        self.gestAlmAOriTXT = 'Almacen origen'
        self.gestAlmADesTXT = 'Almacen destino'
        self.gestAlPEDSubTValor = '70.74 €'

        # Búsqueda avanzada
        self.gestAlmBATitXPath = '//*[@id="advancedSearchModal"]/div/div[1]/span' # BÚSQUEDA AVANZADA
        self.gestAlmFIXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[1]/div[1]/label/div' # Fecha inicio*
        self.gestAlmFFXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[1]/div[2]/label/div'  # Fecha fin*
        self.gestAlmC1XPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[2]/div[1]/label' # Creado por/Almacén/Almacén Origen
        self.gestAlmC2XPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[2]/div[2]/label' # Estado/Proveedor/Tipo de categoría/Almacen destino
        self.gestAlmMPBARefXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[1]/div[1]/label' # Ref., Nombre
        self.gestAlmMPBAKOXPath = '//*[@id="advancedSearchModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlmMPBAOKXPath  = '//*[@id="advancedSearchModal"]/div/form/div[3]/button[2]' # Buscar
        self.gestAlmMPBACIAXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[1]/div[2]/label' # Controlar inventario,Ingrediente,Almacén
        self.gestAlmMPBIngRefInput = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[1]/div[1]/label/input'
        self.gestAlmMPBAIngInput = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[1]/div[2]/label/input' # para rellenar ingrediente
        self.gestAlmMPBACategNomXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[1]/label'
        self.gestAlmMPBACategTypXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[2]/label'
        self.gestAlmMPBACategConXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[3]/label'
        self.gestAlMERIATPBEXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[3]/div[1]/label' # Almacén/Tipo de movimiento/Buscar/Estado
        self.gestAlMERIUbECPCXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[3]/div[2]/label' # Ubicación/Estado/Creado por/Cancelar
        self.gestAlMERIBusAvdStXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[2]/div[2]/label/div/select/option[4]'  # Estado: Completado
        self.gestAlMERTSBASAXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[2]/div[1]/label/div/select'
        self.gestAlMERTSBAASXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[2]/div[1]/label/div/select/option[10]' # LTL Fleming
        self.gestAlMERTSBABMXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[3]/div[1]/label/div/select' # Tipo de movimiento
        self.gestAlMERTSBATMBMXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[3]/div[1]/label/div/select/option[3]'  # Buffet merma/albarán estado Pediente de Validar
        self.gestAlMERTSBAOrdXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[3]/div[1]/label/div/select/option[7]'  # Pedido completado
        self.gestAlPEDBAProvXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[4]/div[1]/label' # Proveedor
        self.gestAlPEDBAPProvXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[4]/div[2]/label' # Producto de proveedor
        self.gestAlPEDBAPProvTXT = 'Producto de proveedor'
        self.gestAlPEDBATotXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[5]/label' # Total

        self.gestAlmMosProdXPath = '//*[@id="rawproduct-action"]/div[2]' # Mostrando..productos,ingredientes
        self.gestAlmMosCatXPath = '//*[@id="catalogue-action"]/div[2]' # Mostrando..catálogos
        self.gestAlmMosFacPXPath = '//*[@id="invoice-action"]/div[2]' # Mostrando..facturas proveedor
        self.gestAlmMosUnitXPath = '//*[@id="unit-action"]/div/div[3]'  # Mostrando..unidades
        self.gestAlmMosProAlmXPath = '//*[@id="warehouse-action"]/div[3]' # Mostrando productos en almacén..
        self.gestAlmMosMovXPath = '//*[@id="stockmovement-action"]/div[2]'  # Mostrando del0al0de0movimientos
        self.gestAlmMosDesXPath = '//*[@id="decrease-action"]/div[2]' # Mostrando ..mermas
        self.gestAlmMosPedXPath = '//*[@id="purchaseOrder-action"]/div[2]' # Mostrando del..pedidos
        self.gestAlmMosAlbXPath = '//*[@id="delivery-action"]/div[2]'  # Mostrando del..albaranes
        self.gestAlmMosRCXPath = '//*[@id="recipe-action"]/div[2]' # Mostrando del..recetas de carta


        self.gestAlmMERAMos1TXT = 'Mostrando del1al1de1Productos'
        self.gestAlmMos1TXT = 'Mostrando del1al20de2419proveedores' # En Edge, para que salgan 20 se redimensiona la pantalla
        self.gestAlmMos2TXT = 'Mostrando del21al40de2419proveedores'
        self.gestAlmMos3TXT = 'Mostrando del41al60de2419proveedores'
        self.gestAlmMos4TXT = 'Mostrando del61al80de2419proveedores'
        self.gestAlmMos5TXT = 'Mostrando del81al100de2419proveedores'
        self.gestAlmFPMosTXT = 'Mostrando del0al0de0facturas de proveedor'
        self.gestAlmMPPMosTXT = 'Mostrando del1al20de6793productos'
        self.gestAlmMPPMUPTXT = 'Mostrando del1al20de6793productos'  # con uso de personal seleccionado
        self.gestAlmMPPMURTXT = 'Mostrando del1al8de8productos'  # con uso en receta seleccionado
        self.gestAlmMPPMURPTXT = 'Mostrando del0al0de0productos'  # con uso en receta y de personal seleccionado
        self.gestAlmPCaMosTXT = 'Mostrando del1al20de105catálogos'
        self.gestAlmPInMosTXT = 'Mostrando del1al20de4712ingredientes'
        self.gestAlmPUnitM1TXT = 'Mostrando del1al20de1475unidades'
        self.gestAlmPUnitM2TXT = 'Mostrando del21al40de1475unidades'
        self.gestAlmPUnitM3TXT = 'Mostrando del41al60de1475unidades'
        self.gestAlmPUnitM4TXT = 'Mostrando del61al80de1475unidades'
        self.gestAlmPUnitM5TXT = 'Mostrando del81al100de1475unidades'
        self.gestAlmMERAMosTXT = 'Mostrando del1al20de2093Productos'
        self.gestAlmMos6TXT = 'Mostrando del0al0de0inventarios'
        #self.gestAlmMos7TXT = 'Mostrando del1al20de60movimientos'
        #self.gestAlmMos8TXT = 'Mostrando del1al20de21056mermas'
        #self.gestAlmMos9TXT = 'Mostrando del1al2de2pedidos'
        #self.gestAlmMos10TXT = 'Mostrando del1al2de2pedidos' # deseleccionado ocultar franquicias
        #self.gestAlmMos11TXT = 'Mostrando del1al2de2albaranes'
        #self.gestAlmMos12TXT = 'Mostrando del0al0de0albaranes'
        self.gestAlmMos13TXT = 'Mostrando del0al0de0pedidos'   # Pedidos de clientes
        self.gestAlmMos14TXT = 'Mostrando del0al0de0compra'  # Compras externas
        self.gestAlmMos15TXT = 'Mostrando del1al20de4849recetas de carta'
        self.gestAlmMos16TXT = 'Mostrando del21al40de4849recetas de carta'
        self.gestAlmMos17TXT = 'Mostrando del41al60de4849recetas de carta'
        self.gestAlmMos18TXT = 'Mostrando del61al80de4849recetas de carta'
        self.gestAlmMos19TXT = 'Mostrando del81al100de4849recetas de carta'# Recetas de carta


        # Avanzar/retroceder página almacen
        self.gestAlmAvPXPath = '//*[@id="provider-table"]/div[1]/div/div/ul/li[13]/a'
        #self.gestAlmAvPTXT = '>>'
        self.gestAlmRePXPath = '//*[@id="provider-table"]/div[1]/div/div/ul/li[1]/a'
        #self.gestAlmRePTXT = '<<'
        self.gestAlmPg5XPath = '//*[@id="provider-table"]/div[1]/div/div/ul/li[6]/a'
        self.gestAlmPg5TXT = '5'
        self.gestAlmPg1XPath = '//*[@id="provider-table"]/div[1]/div/div/ul/li[2]/a'
        self.gestAlmPg1TXT = '1'
        self.gestAlmMosProvXPath = '//*[@id="provider-action"]/div[2]'

        # Opciones  --> Variables en Commons: Exportar, ExportaciónExitosa, Descargar..
        self.gestAlmExpDesLPrTXT = 'Listado%20de%20proveedores_'  # Descarga de la exportacion del Nuevo Fichero
        self.gestAlmExpDesFMPProdTXT = 'Listado%20de%20productos_'
        self.gestAlmExpDesFMPCTXT = 'Listado%20de%20cat%C3%A1logos_'
        self.gestAlmExpDesFMPITXT = 'Listado%20de%20ingredientes_'
        self.gestAlmExpDesFMPCategTXT = 'Listado%20de%20categor%C3%ADas_'
        self.gestAlmExpDesFMPUnitsTXT = 'Listado%20de%20unidades_'  # Listado de unidades_20241230_08372040.xlsx
        self.gestAlmExpDesFMerInvTXT = 'Listado%20de%20inventarios_'
        self.gestAlmExpDesLTSTXT = 'Traspasos%20y%20Salidas_'
        self.gestAlmExpDesLDesTXT = 'Listado%20de%20descuadres_'
        self.gestAlmExpDesLPedTXT = 'Lista%20de%20pedidos%20a%20proveedor_'
        self.gestAlmExpDesLAlbETXT = 'Listado%20de%20albaranes%20de%20entrada_'
        self.gestAlmExpDesLAlbSTXT = 'Listado%20de%20albaranes%20de%20salida_'
        self.gestAlmExpDesLCETXT = 'Compras%20externas_'
        self.gestAlmExpDesLRCTXT = 'Relaci%C3%B3n%20de%20productos%20de%20carta%20y%20escandallos_'

        self.gestAlmExpFMPProvTXT = 'Listado de proveedores'
        self.gestAlmExpFMPPTXT = 'Listado de productos'# Descarga Fichero Materias Primas,
        self.gestAlmExpFMPCatTXT = 'Listado de catálogos'  # Descarga Fichero Materias Primas, Catálogos
        self.gestAlmExpFMPIngTXT = 'Listado de ingredientes'  # Descarga Fichero Materias Primas, Ingredientes
        self.gestAlmExpFMPCategTXT = 'Listado de categorías'  # Descarga Fichero Materias Primas, Categorias
        self.gestAlmExpFMPUnitsTXT = 'Listado de unidades'   # Descarga Fichero Materias Primas, Unidades
        self.gestAlmExpFMerInvTXT = 'Listado de inventarios' # Descarga Fichero Mercancías, Inventario
        self.gestAlmExpFTSTXT = 'Traspasos y Salidas'  # Descarga Fichero Mercancías, Transpasos y Salidas
        self.gestAlmExpFDesTXT = 'Listado de descuadres'
        self.gestAlmExpFPedTXT = 'Lista de pedidos a proveedor'
        self.gestAlmExpFAlbETXT = 'Listado de albaranes de entrada'
        self.gestAlmExpFAlbSTXT = 'Listado de albaranes de salida'
        self.gestAlmExpFCETXT = 'Compras externas'
        self.gestAlmExpFRCTXT = 'Relación de productos de carta y escandallos'

        # Buscar
        self.gestAlmMPPBusXPath = '//*[@id="rawproduct-action"]/div' # Localización texto Buscar: Producto
        self.gestAlmMPUBusXPath = '//*[@id="unit-action"]/div/span'  # Localización texto Buscar: Unidades
        self.gestAlmMERABusXPath = '//*[@id="storage-action"]/div[1]/span' # # Localización texto Buscar: Almacén
        self.gestAlmProvBusXPath = '//*[@id="provider-action"]/div[1]'  # Localización texto Buscar: Proveedor
        self.gestAlmBusProInput = '//*[@id="provider-action"]/div[1]/div/input'  # Buscar proveedor
        self.gestAlmBusAlmInput = '//*[@id="storage-action"]/div[1]/div[1]/input' # Buscar en un almacen
        self.gestAlmBusProValor = '//*[@id="provider-table"]/table/tbody/tr/td[1]'# posicion del nuevo elemento en la tabla
        self.gestAlmBusIngValor = '//*[@id="rawproduct-table"]/table/tbody/tr[1]/td[1]' # posicion del nuevo elemento en la tabla

        # Validar formulario: Nuevo proveedor
        self.gestAlmNPGuaID = 'saveProvider'
        self.gestAlmNPRefXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[1]/div[1]/label/div' # Referencia
        self.gestAlmNPCifXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[1]/div[2]/label'
        self.gestAlmNPCifTXT = 'CIF'
        self.gestAlmNPTelXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/label'
        self.gestAlmNPTelTXT = 'Teléfono'
        self.gestAlmNPTel2XPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/label'
        self.gestAlmNPTel2TXT = 'Teléfono 2'
        self.gestAlmNPNomXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[2]/label/div'
        self.gestAlmNPEmaXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[2]/label'
        self.gestAlmNPEmaTXT = 'Email'
        self.gestAlmNPEma2XPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[2]/label'
        self.gestAlmNPEma2TXT = 'Email 2'
        self.gestAlmNPRSoXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[3]/label/div'
        self.gestAlmNPRSoTXT = 'Razón social*'
        self.gestAlmNPEmaCXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[3]/label'
        self.gestAlmNPEmaCTXT = 'Email comercial'
        self.gestAlmNPFaxXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[3]/label'
        self.gestAlmNPFaxTXT = 'Fax'
        self.gestAlmNPDirXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[4]/label'
        self.gestAlmNPDirTXT = 'Dirección'
        self.gestAlmNPPIntXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[2]/label/div/span'
        self.gestAlmNPPIntTXT = 'Proveedor interno'
        self.gestAlmNPPISocXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[3]/label/div[1]'
        self.gestAlmNPPISocTXT = 'Sociedad'
        self.gestAlmNPPIAlmXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[4]/label/div[1]'
        self.gestAlmNPConXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[5]/label'
        self.gestAlmNPDAlXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[6]/div[1]/div/label'
        self.gestAlmNPDAlTXT = 'Descuento albarán (%)*'
        self.gestAlmNPRapXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[6]/div[2]/div/label/div'
        self.gestAlmNPRapTXT = 'Rappel (%)*'
        self.gestAlmNPPedXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[7]/h4'
        self.gestAlmNPPedTXT = 'Pedidos'
        self.gestAlmNPInPXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[7]/h4/i' # interrogación pedidos
        self.gestAlmNPCIPXPath = '//*[@id="purchaseorderModalInfo"]/div/form/div[3]/button' # cancelar interrogación pedidos
        self.gestAlmNPEmPXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[8]/div[1]/label/div' # email pedidos
        self.gestAlmNPEmPTXT = 'Email pedidos*'
        self.gestAlmNPPeMXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[8]/div[2]/label/div' # pedido mínimo
        self.gestAlmNPPeMTXT = 'Pedido mínimo (€)*'
        self.gestAlmNPDEPXPath = '//*[@id="deliveryDaysLabel"]/div[1]' # días emisión pedidos
        self.gestAlmNPDEPTXT = 'Días de emisión de pedidos*'
        self.gestAlmNPTEnTXT = 'Tiempo de entrega (Días naturales)'  # frase común para los siete días de la semana
        self.gestAlmNPLunXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[1]/div[1]/label/div'
        self.gestAlmNPLunTXT = 'Lunes'
        self.gestAlmNPTELXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[1]/div[2]/label'  # Tiempo entrega
        self.gestAlmNPMarXPath =' //*[@id="deliveryDaysLabel"]/div[2]/div[2]/div[1]/label/div'
        self.gestAlmNPMarTXT = 'Martes'
        self.gestAlmNPTEMXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[2]/div[2]/label'  # Tiempo entrega
        self.gestAlmNPMieXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[3]/div[1]/label/div'
        self.gestAlmNPMieTXT = 'Miércoles'
        self.gestAlmNPTEXXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[3]/div[2]/label'  # Tiempo entrega
        self.gestAlmNPJueXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[4]/div[1]/label/div'
        self.gestAlmNPJueTXT = 'Jueves'
        self.gestAlmNPTEJXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[4]/div[2]/label'  # Tiempo entrega
        self.gestAlmNPVieXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[5]/div[1]/label/div'
        self.gestAlmNPVieTXT = 'Viernes'
        self.gestAlmNPTEVXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[5]/div[2]/label'  # Tiempo entrega
        self.gestAlmNPSabXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[6]/div[1]/label/div'
        self.gestAlmNPSabTXT = 'Sábado'
        self.gestAlmNPTESXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[6]/div[2]/label'  # Tiempo entrega
        self.gestAlmNPDomXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[7]/div[1]/label/div'
        self.gestAlmNPDomTXT = 'Domingo'
        self.gestAlmNPTEDXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[7]/div[2]/label'

        # Rellenar formulario: Nuevo proveedor
        self.gestAlmNPRefInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[1]/div[1]/label/input'  # Referencia para proveedor
        self.gestAlmNPRefValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime)
        #  el cif se rellena automaticamente al escoger almacen
        self.gestAlmNPNomInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[2]/label/input'
        self.gestAlmNPNomValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '_nombre'
        self.gestAlmNPRSoInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[3]/label/input'
        self.gestAlmNPRSoValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '_razonsocial'
        self.gestAlmNPDirInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[4]/label/input'
        self.gestAlmNPDirValor = 'Dirección de  ' + self.QA
        self.gestAlmNPConInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[5]/label/input'
        self.gestAlmNPConValor = 'Contabilidad de ' + self.QA
        self.gestAlmNPDAlInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[6]/div[1]/div/label/input'
        self.gestAlmNPDAlValor = format(random.randint(1, 9))
        self.gestAlmNPRapInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[6]/div[2]/div/label/input'
        self.gestAlmNPRapValor = format(random.randint(1, 9))
        self.gestAlmNPEmPInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[8]/div[1]/label/input'
        self.gestAlmNPEmPValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '@emailpedido.de'
        self.gestAlmNPPeMInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[8]/div[2]/label/input'
        self.gestAlmMCoXPath = '//*[@id="provider-table"]/div[2]/label/div'
        self.gestAlmMCoPeMTXT = 'Pedido mínimo'
        self.gestAlmNPPeMValor = format(random.randint(1, 9))
        self.gestAlmNPLuCInput = '//*[@id="gapmon"]'
        self.gestAlmNPLuCValor = format(random.randint(1, 9))
        self.gestAlmNPMaCInput = '//*[@id="gaptue"]'
        self.gestAlmNPMaCValor = format(random.randint(1, 9))
        self.gestAlmNPMiCInput = '//*[@id="gapwed"]'
        self.gestAlmNPMiCValor = format(random.randint(1, 9))
        self.gestAlmNPJuCInput = '//*[@id="gapthu"]'
        self.gestAlmNPJuCValor = format(random.randint(1, 9))
        self.gestAlmNPViCInput = '//*[@id="gapfri"]'
        self.gestAlmNPViCValor = format(random.randint(1, 9))
        self.gestAlmNPSaCInput = '//*[@id="gapsat"]'
        self.gestAlmNPSaCValor = format(random.randint(1, 9))
        self.gestAlmNPDoCInput = '//*[@id="gapsun"]'
        self.gestAlmNPDoCValor = format(random.randint(1, 9))
        self.gestAlmNPTelInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/label/input'
        self.gestAlmNPTelValor = '666111111'
        self.gestAlmNPEmaInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[2]/label/input'
        self.gestAlmNPEmaValor = self.gestAlmNPNomValor + '@email.de'
        self.gestAlmNPEmCInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[3]/label/input'
        self.gestAlmNPEmCValor = self.gestAlmNPNomValor + '@email1.de'
        self.gestAlmNPTe2Input = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/label/input'
        self.gestAlmNPTe2Valor = '666222222'
        self.gestAlmNPEm2Input = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[2]/label/input'
        self.gestAlmNPEm2Valor = self.gestAlmNPNomValor + '@email2.de'
        self.gestAlmNPFaxInput = '//*[@id="provider-space"]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[3]/label/input'
        self.gestAlmNPFaxValor = 'FAX6090000'
        self.gestAlmNPPISocSelID = 'internalCorporation'
        self.gestAlmNPPISocSelXPath = '//*[@id="internalCorporation"]/select/option[34]' # LATERAL FLEMING, S.L
        self.gestAlmNPPISocOKTXT = 'LATERAL FLEMING, S.L.' # proveedor interno, sociedad seleccionada
        self.gestAlmNPPIAlmSelID = 'internalWarehouse'
        self.gestAlmNPPIAlmOKXPath = '//*[@id="internalWarehouse"]/select/option[18]'
        self.gestAlmNPPIAlmOKTXT = 'LTL Strachan'  # proveedor interno, almacén seleccionado
        self.gestAlmNPDAVXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[6]/div[1]/div/label/input'
        self.gestAlmNPRaVXPath = '//*[@id="provider-space"]/div[3]/div[2]/div/div[1]/div[6]/div[2]/div/label/input'
        self.gestAlmNPDSPXPath = '//*[@id="deliveryDaysLabel"]/div[2]/div[2]/div[1]/label/div/span' # des-selecciona martes

        # Mostrar más columnas
        self.gestAlmMCo1XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlmMCo2XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlmMCo3XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[3]/div/span'
        self.gestAlmMCo4XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[4]/div/span'
        self.gestAlmMCo5XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[5]/div/span'
        self.gestAlmMCo6XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[6]/div/span'
        self.gestAlmMCo7XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[7]/div/span'
        self.gestAlmMCo8XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[8]/div/span'
        self.gestAlmMCo9XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[9]/div/span'
        self.gestAlmMCo10XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[10]/div/span'
        self.gestAlmMCo11XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[11]/div/span'
        self.gestAlmMCo12XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[12]/div/span'
        self.gestAlmMCo13XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[13]/div/span'
        self.gestAlmMCo14XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[14]/div/span'
        self.gestAlmMCo15XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[15]/div/span'
        self.gestAlmMCo16XPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[16]/div/span'
        self.gestAlmMCoCodTXT = 'Cód. Interno'
        self.gestAlmMCoCIFTXT = 'CIF'
        self.gestAlmMCoTelTXT = 'Teléfono'
        self.gestAlmMCoTe2TXT = 'Teléfono 2'
        self.gestAlmMCoTe3TXT = 'Teléfono 3'
        self.gestAlmMCoEmaTXT = 'Email'
        self.gestAlmMCoEm2TXT = 'Email 2'
        self.gestAlmMCoEmCTXT = 'Email comercial'
        self.gestAlmMCoEmPTXT = 'Email pedidos'
        self.gestAlmMCoPeMTXT = 'Pedido mínimo'
        self.gestAlmMCoDTOTXT = 'Desc. albarán'
        self.gestAlmMCoRapTXT = 'Rappel'
        self.gestAlmMCoIntTXT = 'Interno'

        # selección / deselección de columnas
        self.gestAlmMCoConXPath = '//*[@id="provider-table"]/div[2]/i'
        self.gestAlmMCoSelXPath ='//*[@id="columnsModal"]/div/form/div[1]/div[3]/div[2]/label/div/span' #Teléfono 2
        self.gestAlmMCoSelTXT = 'Teléfono 2'
        self.gestAlmMCoSAcXPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[5]/div/span'
        self.gestAlmMCoDesXPath ='//*[@id="columnsModal"]/div/form/div[1]/div[7]/div[1]/label/div/span'
        self.gestAlmMCoDesTXT = 'Rappel'
        self.gestAlmMCoOKXPath = '/html/body/div[19]/div/form/div[3]/button[2]'
        self.gestAlmMCoKOXPath = '/html/body/div[19]/div/form/div[3]/button[1]'
        self.gestAlmMCoOK2XPath = '/html/body/div[21]/div/form/div[3]/button[2]'
        self.gestAlmMCoKO1XPath = '/html/body/div[21]/div/form/div[3]/button[1]'

        # Guardar proveedor
        self.gestAlmProOKXPath = '/html/body/div[2]/div[2]/div[1]/div[2]/button[5]' # Guardar

        # Buscar
        self.gestAlmBusPalTXT = 'HIGIENE'  # palabra a buscar
        self.gestAlmIt1XPath = '//*[@id="provider-action"]/div[2]/span[1]' # 1
        self.gestAlmIt1TXT = "1"
        self.gestAlmItnXPath = '//*[@id="provider-action"]/div[2]/span[2]'
        self.gestAlmItnTXT = "3"
        self.gestAlmRes1XPath = '//*[@id="provider-table"]/table/tbody/tr[1]/td[2]/span'
        self.gestAlmRes2XPath = '//*[@id="provider-table"]/table/tbody/tr[2]/td[2]/span'
        self.gestAlmRes3XPath = '//*[@id="provider-table"]/table/tbody/tr[3]/td[2]/span'
        # Ordenar columnas
        self.gestAlmColOrdXPath = '//*[@id="provider-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlmCol1elXPath = '//*[@id="provider-table"]/table/tbody/tr[1]/td[2]/span'
        self.gestAlmCol1elTXT = 'ADIS HIGIENE S.L.'
        self.gestAlmColUelTXT = 'ZAMBU-HIGIENE SL'

        # Borrar proveedor
        self.gestAlmDelProXPath = '//*[@id="provider-table"]/table/tbody/tr[1]/td[8]/i[2]' # icono borrar
        self.gestAlmDelOKXPath = '//*[@id="deleteProviderModal"]/div/form/div[3]/button[2]'  # Aceptar
        self.gestAlmDelKOXPath = '//*[@id="deleteProviderModal"]/div/form/div[3]/button[1]'  # Cancelar

        # Menú lateral
        self.latPagGestProvXPath = '//*[@id="lateralmenu"]/ul/li[1]/div'
        self.latPagGestLPrXPath = '//*[@id="lateralmenu"]/ul/li[1]/ul/li[1]'
        self.latPagGestFPrXPath = '//*[@id="lateralmenu"]/ul/li[1]/ul/li[2]'
        self.latPagGestFPrTXT = 'Facturas de proveedor'
        self.latPagGestMatXPath = '//*[@id="lateralmenu"]/ul/li[2]/div'
        self.latPagGestMPrXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[1]'
        self.latPagGestMPrTXT = 'Productos de proveedor'
        self.latPagGestMCaXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[2]'
        self.latPagGestMInXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[3]' # Ingredientes
        self.latPagGestMCateXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[4]'
        self.latPagGestMCateTXT= 'Categorías'
        self.latPagGestMUnXPath = '//*[@id="lateralmenu"]/ul/li[2]/ul/li[5]'
        self.latPagGestMerXPath = '//*[@id="lateralmenu"]/ul/li[3]/div'
        self.latPagGestMerTXT = 'Mercancía'
        self.latPagGestMeAXPath = '//*[@id="lateralmenu"]/ul/li[3]/ul/li[1]'
        self.latPagGestMeIXPath = '//*[@id="lateralmenu"]/ul/li[3]/ul/li[2]'
        self.latPagGestMeITXT = 'Inventario'
        self.latPagGestMeTXPath = '//*[@id="lateralmenu"]/ul/li[3]/ul/li[3]'
        self.latPagGestMeTTXT = 'Traspasos y Salidas'
        self.latPagGestMeDXPath = '//*[@id="lateralmenu"]/ul/li[3]/ul/li[4]'
        self.latPagGestMeDTXT = 'Descuadres'
        self.latPagGestPedXPath = '//*[@id="lateralmenu"]/ul/li[4]/div'
        self.latPagGestPedTXT = 'Pedidos'
        self.latPagGestPePXPath = '//*[@id="lateralmenu"]/ul/li[4]/ul/li[1]'
        self.latPagGestPePTXT = 'Pedidos a proveedor'
        self.latPagGestPAEXPath = '//*[@id="lateralmenu"]/ul/li[4]/ul/li[2]'
        self.latPagGestPAETXT = 'Albarán de entrada'
        self.latPagGestPeCXPath = '//*[@id="lateralmenu"]/ul/li[4]/ul/li[3]'
        self.latPagGestPeCTXT = 'Pedidos de cliente'
        self.latPagGestPASXPath = '//*[@id="lateralmenu"]/ul/li[4]/ul/li[4]'
        self.latPagGestPASTXT = 'Albarán de salida'
        self.latPagGestCEXPath = '//*[@id="lateralmenu"]/ul/li[4]/ul/li[5]'
        self.latPagGestCETXT = 'Compras externas'
        self.latPagGestRecXPath = '//*[@id="lateralmenu"]/ul/li[5]/div'
        self.latPagGestRecTXT = 'Receta'
        self.latPagGestReCXPath = '//*[@id="lateralmenu"]/ul/li[5]/ul/li[1]'
        self.latPagGestReCTXT = 'Recetas de carta'
        self.latPagGestReEXPath = '//*[@id="lateralmenu"]/ul/li[5]/ul/li[2]'
        self.latPagGestReETXT = 'Escandallos'
        self.latPagGestReSXPath = '//*[@id="lateralmenu"]/ul/li[5]/ul/li[3]'
        self.latPagGestRCoXPath = '//*[@id="lateralmenu"]/ul/li[5]/ul/li[4]'
        self.latPagGestRCoTXT = 'Combos'
        self.latPagGestReMXPath = '//*[@id="lateralmenu"]/ul/li[5]/ul/li[5]'
        self.latPagGestReMTXT = 'Modificadores'
        self.latPagGestInCXPath = '//*[@id="lateralmenu"]/ul/li[6]'
        self.latPagGestInCTXT = 'Informes de compra'
        self.latPagGestInSXPath = '//*[@id="lateralmenu"]/ul/li[7]'
        self.latPagGestInSTXT = 'Informes de stock'

        # facturas de proveedor --> FP
        self.gestAlmFPTitXPath = '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]'
        self.gestAlmFPBusXPath = '//*[@id="invoice-action"]/div[1]/span'
        self.gestAlmFPFec1XPath = '//*[@id="invoice-action"]/div[1]/div[2]/div/span[2]'
        self.gestAlmFPNueFacTXT = 'Nueva factura'
        self.gestAlmFPFecXPath = '//*[@id="invoice-action"]/div[1]/div[2]/div/span[1]' # Fecha:
        self.gestAlmFPFec2XPath = '//*[@id="invoice-action"]/div[1]/div[2]/div/span[2]' # Valor de fecha
        #self.gestAlmFPBusInput = '//*[@id="invoice-action"]/div[1]/div[1]/input' no existe ninguna factura a buscar
        #self.gestAlmFPBusValor = 'A'
        self.gestAlmFPMosXPath = '//*[@id="invoice-action"]/div[2]'
        self.gestAlmFPTitTotXPath = '//*[@id="invoice-table"]/div[2]/span[1]'
        self.gestAlmFPCanTotXPath = '//*[@id="invoice-table"]/div[2]/span[2]'
        self.gestAlmFPCanTotTXT = '0.00 €'
        self.gestAlmFPc1XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlmFPc2XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlmFPc3XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[3]/div/span'
        self.gestAlmFPc4XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[4]/div/span'
        self.gestAlmFPc5XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[5]/div/span'
        self.gestAlmFPc6XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[6]/div/span'
        self.gestAlmFPc7XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[7]/div/span'
        self.gestAlmFPc8XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[8]/div/span'
        self.gestAlmFPc9XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[9]/div/span'
        self.gestAlmFPc10XPath = '//*[@id="invoice-table"]/table/thead/tr[1]/th[10]/div/span'
        self.gestAlmFPNFPTXT = 'Nº de factura de proveedor'
        self.gestAlmFPBTTXT = 'Base total'
        self.gestAlmFPTITXT = 'Total impuestos'

# productos--> MPP
        self.gestAlMPPTitXPath = '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]'
        self.gestAlmMPPFilXPath = '//*[@id="rawproduct-action"]/div[1]/div[2]/div/span' # Filtros
        self.gestAlmMPPFURXPath = '//*[@id="rawproduct-action"]/div[1]/div[2]/div/div[1]'
        self.gestAlmMPPFURTXT = 'Uso en receta'
        self.gestAlmMPPFUPXPath = '//*[@id="rawproduct-action"]/div[1]/div[2]/div/div[2]'
        self.gestAlmMPPFUPTXT = 'Uso de personal'
        self.gestAlmMPPCloID = 'cloneRawProducts'
        self.gestAlmMPPCloTXT = 'Clonar productos'
        self.gestAlmMPPCo1XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlmMPPCo2XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlmMPPCo3XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[3]/div/span'
        self.gestAlmMPPCo4XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[4]/div/span'
        self.gestAlmMPPCo5XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[5]/div/span'
        self.gestAlmMPPCo6XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[6]/div/span'
        self.gestAlmMPPCo7XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[7]/div/span'
        self.gestAlmMPPCo8XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[8]/div/span'
        self.gestAlmMPPCo9XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[9]/div/span'
        self.gestAlmMPPCo10XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[10]/div/span'
        self.gestAlmMPPCo11XPath = '//*[@id="rawproduct-table"]/table/thead/tr[1]/th[11]/div/span'
        self.gestAlmMPPCExtTXT = 'Cód. Externo'
        self.gestAlmMPPProTXT = 'Producto'
        self.gestAlmMPPPUnTXT = 'Precio por unidad (€)'
        self.gestAlmMPPMCoXPath = '//*[@id="rawproduct-table"]/div[2]/label/div/span'  # 'Mostrar más columnas'

        # materias primas, más columnas
        self.gestAlmMPMasColNewXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/thead/tr[1]/th[11]/div/span'
        self.gestAlmMPMasColNewTXT = 'Alérgenos'
        self.gestAlmMPMasColConfXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[2]/i'  # ajustes mas columnas
        self.gestAlmMPMasColSelXPath = '/html/body/div[24]/div/form/div[1]/div[2]/div[1]/label/div/span'
        self.gestAlmMPMasColOKXPath = '/html/body/div[24]/div/form/div[3]/button[2]'
        self.gestAlmMPMasColKOXPath = '/html/body/div[24]/div/form/div[3]/button[1]'

        # materias primas, busqueda avanzada--> MPBA

        # Busqueda avanzada proveedor
        self.gestAlmMPBAProInput = '//*[@id="searchProvider"]/select'
        self.gestAlmMPBAProvValor = '//*[@id="searchProvider"]/select/option[74]' # MAHOU, S.A.
        self.gestAlmMPBAProvNombre = 'MAHOU, S.A.'


        # Busqueda avanzda productos, resultado
        self.gestAlmMPBACatResXPath ='//*[@id="rawproduct-action"]/div[1]/div[2]/div[3]/span[2]'# Cervezas
        #self.gestAlmMPBAProvResXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr/td[3]'   (en la tabla)

        self.gestAlmMPBAProvResXPath = '//*[@id="rawproduct-action"]/div[1]/div[2]/div[4]/span[2]'# MAHOU, S.A.

        # Busqueda avanzada ingredientes

        self.gestAlmMPBAIngValor = 'ALHAMBRA'

        # Busqueda avanzada categorías
        self.gestAlmMPBACatInput = '//*[@id="searchCategory"]/select'
        self.gestAlmMPBACatValor = '//*[@id="searchCategory"]/select/option[13]'
        self.gestAlmMPBACatNombre = 'Cervezas'

        self.gestAlmMPBACategNomInput = '/html/body/div[13]/div/form/div[1]/div[1]/label/input'
        self.gestAlmMPBACategResXPath = '//*[@id="rawproduct-table"]/table/tbody/tr/td[2]/span' # Resultado busqueda categoría

        # materias primas, Clonar--> MPC, clone, delete
        self.gestAlmMPCTitXPath = '//*[@id="cloneRawproductsModal"]/div/div[1]'
        self.gestAlmMPCTitTXT = 'CLONAR PRODUCTOS'
        self.gestAlmMPCPOXPath = '//*[@id="cloneRawproductsModal"]/div/form/div[1]/div/div[1]/label/div[1]'
        self.gestAlmMPCPOTXT = 'Proveedor origen*'
        self.gestAlmMPCPDXPath = '//*[@id="cloneRawproductsModal"]/div/form/div[1]/div/div[2]/label/div[1]'
        self.gestAlmMPCPDTXT = 'Proveedor destino*'
        self.gestAlmMPCOKTXT = 'Clonar'
        self.gestAlmMPCPOInput = '/html/body/div[19]/div/form/div[1]/div/div[1]/label/div[2]/select' # Proveedor Origen
        self.gestAlmMPCPOValor = '/html/body/div[19]/div/form/div[1]/div/div[1]/label/div[2]/select/option[4]' # 3 BARRICAS, S.A
        self.gestAlmMPCPONomValor = '3 BARRICAS, S.A'
        self.gestAlmMPCPDInput = '/html/body/div[19]/div/form/div[1]/div/div[2]/label/div[2]/select'
        self.gestAlmMPCPDValor = '/html/body/div[19]/div/form/div[1]/div/div[2]/label/div[2]/select/option[2]' # 1QANER_NOBORRAR
        self.gestAlmMPCPSelPXPath = '//*[@id="clone-table"]/table/tbody/tr[4]/td[1]/input'
        self.gestAlmMPCPrvClXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[3]'  # Proveedor Clonado
        self.gestAlmMPCPrdClXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[2]' # Producto Clonado: Tombu Rosado (c/ 6 botellas)
        self.gestAlmMPCPrdClTXT = 'Tombu Rosado (c/ 6 botellas)'
        self.gestAlmMPCBusXPath = '/html/body/div[2]/div[2]/div[3]/div/div[1]/div[1]/div[1]/input'
        self.gestAlmMPCProvEncXPath = '//*[@id="rawproduct-table"]/table/tbody/tr[1]/td[3]' # Buscar: 1QANER_NOBORRAR
        self.gestAlmMPCDelXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[6]/i[4]'

        self.gestAlmMPCDelTitXPath = '/html/body/div[20]/div/div[1]/span'
        self.gestAlmMPCBusXPath = '/html/body/div[2]/div[2]/div[3]/div/div[1]/div[1]/div[1]/input'

        self.gestAlmMPCDelTitTXT = 'ELIMINAR PRODUCTO'
        self.gestAlmMPCDelTit2XPath = '//*[@id="deleteRawProductModal"]/div/form/div[1]/p[1]'
        self.gestAlmMPCDelTit2TXT = '¿Está seguro de eliminar este producto?'
        self.gestAlmMPCDelKOXPath ='//*[@id="deleteRawProductModal"]/div/form/div[3]/button[1]'
        self.gestAlmMPCDelOKXPath = '//*[@id="deleteRawProductModal"]/div/form/div[3]/button[2]'

#producto
        self.gestAlmMPPTABLA = '//*[@id="rawproduct-table"]/table/tbody/tr[1]/td[2]/span'
        self.gestAlmMPCreTitXPath = '/html/body/div[2]/div[2]/div[1]/div[1]/div[2]'
        self.gestAlmMPCreTitTXT = 'PRODUCTO DE PROVEEDOR'
        self.gestAlmMPCreRefXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/label/div'
        self.gestAlmMPCreCBXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/label'
        self.gestAlmMPCreCBTXT = 'Código de barras'
        self.gestAlmMPCrePCIXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[1]/label/div'
        self.gestAlmMPCrePCITXT = 'Producto para consumo interno'
        self.gestAlmMPCreNAlXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[2]/label/div'
        self.gestAlmMPCreNAlTXT = 'Nombre comercial de albarán*'
        self.gestAlmMPCreNInXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[2]/label/div[1]'
        self.gestAlmMPCreNInTXT = 'Nombre de ingrediente*'
        self.gestAlmMPCreProXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[3]/label/div[1]'
        self.gestAlmMPCreCatXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[3]/label'
        self.gestAlmMPCreDAlXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/label'
        self.gestAlmMPCreDAlTXT = 'Descuento albarán (%)'
        self.gestAlmMPCreRapXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/label'
        self.gestAlmMPCreRapTXT = 'Rappel (%)'
        self.gestAlmMPCreSob1XPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/label/div'
        self.gestAlmMPCreSobTXT = 'Sobreescribir'
        self.gestAlmMPCreSob2XPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/label/div'
        self.gestAlmMPCreUdXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[2]/h4'

        self.gestAlmMPCreUCXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[1]/label/div[1]'
        self.gestAlmMPCreUCTXT = 'Unidad de Compra*'
        self.gestAlmMPCreCon1XPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[2]/label/div'
        self.gestAlmMPCreConTXT = 'Conversión*'
        self.gestAlmMPCreUAXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[3]/label/div[1]'
        self.gestAlmMPCreUATXT = 'Unidad de Almacenamiento*'
        self.gestAlmMPCreCon2XPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[4]/label/div'
        self.gestAlmMPCreURXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[5]/label/div'
        self.gestAlmMPCreURTXT = 'Unidad de receta*'
        self.gestAlmMPCrePrXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[4]/h4'
        self.gestAlmMPCrePrUXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[5]/div[1]/label/div'
        self.gestAlmMPCrePrUTXT = 'Precio por unidad (€)*'
        self.gestAlmMPCreIVAXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[5]/div[2]/label/div[1]'
        self.gestAlmMPCreIVATXT = 'IVA*'
        self.gestAlmMPCrePrUnXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[5]/div[3]/label'
        self.gestAlmMPCrPrUnTXT = 'Precio unitario (€)'
        self.gestAlmMPCreKOXPath = '/html/body/div[2]/div[2]/div[1]/div[2]/button[3]'
        self.gestAlmMPCreKOTXT = 'Volver'
        self.gestAlmMPCreOKXPath = '/html/body/div[2]/div[2]/div[1]/div[2]/button[6]'
        self.gestAlmMPCreRefInput = '//*[@id="rawproduct-space"]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/label/input'
        self.gestAlmMPCreRefValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime)
        self.gestAlmMPCreCBInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/label/input'
        self.gestAlmMPCreCBValor = format(random.randint(1, 9))+'-'+format(random.randint(100000, 999999))+'-'+format(random.randint(100000, 999999))
        self.gestAlmMPCreNAlInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[2]/label/input'
        self.gestAlmMPCreNAlValor = self.QA + ' Producto ' + '{:%d%m%y%H%M}'.format(self.datetime)
        self.gestAlmMPCreProInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[3]/label/div[2]/select'  # Proveedor
        self.gestAlmMPCreProValor = '//*[@id="rawproduct-space"]/div[3]/div[2]/div[1]/div[1]/div[3]/label/div[2]/select/option[3]' # 3 BARRICAS, S.A
        self.gestAlmMPCreNInInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[2]/label/div[2]/select'
        self.gestAlmMPCreNInValor = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[2]/label/div[2]/select/option[19]'

        # proveedor, usar los de materias primas, Clonar--> MPC, clone, delete
        #self.gestAlmMPCreCatInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[3]/label/input'  (relleno automático)
        self.gestAlmMPCreDAlInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/label/input'
        self.gestAlmMPCreDAlValor = '1'
        self.gestAlmMPCreRapInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/label/input'
        self.gestAlmMPCreRapValor = '3'
        self.gestAlmMPCreUCInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[1]/label/div[2]/select'  # Unidad de compra
        self.gestAlmMPCreUCValor = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[1]/label/div[2]/select/option[2]'
        self.gestAlmMPCreCon1Input = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[2]/label/input'  # Conversión
        self.gestAlmMPCreCon1Valor = '90'
        self.gestAlmMPCreUAInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[3]/label/div[2]/select'
        self.gestAlmMPCreUAValor = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[3]/label/div[2]/select/option[2]'
        self.gestAlmMPCreCon2Input = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[3]/div[4]/label/input'
        self.gestAlmMPCreCon2Valor = '10'
        self.gestAlmMPCrePrUInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[5]/div[1]/label/input'
        self.gestAlmMPCrePrUValor = '20.77'
        self.gestAlmMPCreIVAInput = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[5]/div[2]/label/div[2]/select'
        self.gestAlmMPCreIVAValor = '/html/body/div[2]/div[2]/div[3]/div/div[3]/div[2]/div[5]/div[2]/label/div[2]/select/option[6]'
        self.gestAlmMPNProXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[2]' # posicion en la tabla del nuevo producto

        # materias primas, acciones--> MPA, Borrar(Del)
        self.gestAlmMPProDelXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[6]/i[4]'
        self.gestAlmMPProDelKOXPath = '/html/body/div[20]/div/form/div[3]/button[1]'
        self.gestAlmMPProDelOKXPath = '/html/body/div[20]/div/form/div[3]/button[2]'

        # materias primas, acciones--> MPA, Historico de Precios(HP)
        self.gestAlmMPAHPXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[6]/i[1]'
        self.gestAlmMPAHPTitXPath = '/html/body/div[17]/div/div[1]/span'
        self.gestAlmMPAHPTitTXT = 'HISTÓRICO DE PRECIO'
        self.gestAlmMPAHPFecXPath = '/html/body/div[17]/div/form/div[1]/div/div/div/table/thead/tr[1]/th[1]/div/span'
        self.gestAlmMPAHPFecTXT = 'Fecha'
        self.gestAlmMPAHPPreXPath = '/html/body/div[17]/div/form/div[1]/div/div/div/table/thead/tr[1]/th[2]/div/span'
        self.gestAlmMPAHPPreTXT = 'Precio'
        self.gestAlmMPAHPVar1XPath = '/html/body/div[17]/div/form/div[1]/div/div/div/table/thead/tr[1]/th[3]/div/span'
        self.gestAlmMPAHPVar2XPath = '/html/body/div[17]/div/form/div[1]/div/div/div/table/thead/tr[1]/th[4]/div/span'
        self.gestAlmMPAHPCerXPath = '/html/body/div[17]/div/form/div[3]/button'

        # materias primas, acciones--> MPA, Distribuidor(D)
        self.gestAlmMPADXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[6]/i[2]'
        self.gestAlmMPADTitXPath = '/html/body/div[21]/div/div[1]/span'
        self.gestAlmMPADTitTXT = 'DISTRIBUIDOR'
        self.gestAlmMPADInput = '/html/body/div[21]/div/form/div[1]/div[2]/div/select'
        self.gestAlmMPADValor = '/html/body/div[21]/div/form/div[1]/div[2]/div/select/option[3]'
        self.gestAlmMPADKOXPath = '/html/body/div[21]/div/form/div[3]/button[1]'

#Alérgenos(A)
        self.gestAlmMPAAXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[6]/img'
        self.gestAlmMPAATitXPath = '//*[@id="allergenModal"]/div/div[1]/span'
        self.gestAlmMPAATitTXT = 'ALÉRGENOS: '
        self.gestAlmMPAATit2XPath = '/html/body/div[25]/div/form/div[1]/div/div[1]/label/div/span'
        self.gestAlmMPAATit2TXT = 'Producto libre de alérgenos'
        self.gestAlmMPAAAddXPath = '/html/body/div[25]/div/form/div[1]/div/div[2]/div/button/span'
        self.gestAlmMPAAAddTXT = 'Añadir alérgeno'
        self.gestAlmMPAANomXPath = '/html/body/div[25]/div/form/div[1]/div/div[3]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlmMPAAAcrXPath = '/html/body/div[25]/div/form/div[1]/div/div[3]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlmMPAAAcroTXT = 'Acrónimo'
        self.gestAlmMPAANivXPath = '/html/body/div[25]/div/form/div[1]/div/div[3]/table/thead/tr[1]/th[3]/div/span'
        self.gestAlmMPAANivTXT = 'Nivel'
        self.gestAlmMPAAAccXPath = '/html/body/div[25]/div/form/div[1]/div/div[3]/table/thead/tr[1]/th[4]/div/span'
        self.gestAlmMPAAspaXPath = '//*[@id="allergenModal"]/div/div[1]/i' # Aspa
        self.gestAlmMPAAKOXPath = '/html/body/div[25]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlmMPAAOKXPath = '/html/body/div[25]/div/form/div[3]/button[2]'
        self.gestAlmMPAAEleInput = '//*[@id="allergen-actions"]/div/div[1]/select'
        self.gestAlmMPAAEle2Input = '/html/body/div[25]/div/form/div[1]/div/div[2]/div/div[2]/select'
        self.gestAlmMPAAEleValor = '/html/body/div[25]/div/form/div[1]/div/div[2]/div/div[1]/select/option[8]'
        self.gestAlmMPAAEle2Valor = '/html/body/div[25]/div/form/div[1]/div/div[2]/div/div[2]/select/option[1]'
        self.gestAlmMPAAEleTXT = 'Gluten'
        self.gestAlmMPAAEle2TXT = 'Trazas'
        self.gestAlmMPAAEleAddXPath = '//*[@id="allergen-table"]/table/tbody/tr/td[1]'  # Elemento Gluten añadido
        self.gestAlmMPAA2EleValor = '/html/body/div[25]/div/form/div[1]/div/div[2]/div/div[1]/select/option[9]'
        self.gestAlmMPAA2Ele2Valor = '/html/body/div[25]/div/form/div[1]/div/div[2]/div/div[2]/select/option[2]'
        self.gestAlmMPAA2EleTXT = 'Huevos'
        self.gestAlmMPAA2Ele2TXT = 'Contiene'
        self.gestAlmMPAEXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[6]/i[3]' # Accion: Editar
        self.gestAlmMPADEXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr/td[6]/i[5]' # Accion: Deshabilitar
        self.gestAlmMPADEPXPath = '//*[@id="disableProductModal"]/div/form/div[1]/p[2]'
        self.gestAlmMPADEKOXPath = '/html/body/div[23]/div/form/div[3]/button[1]'
        self.gestAlmMPADEOKXPath = '/html/body/div[23]/div/form/div[3]/button[2]'
        self.gestAlmMPADEOKTXT = 'Deshabilitar'

# catálogos, Creacion(C)
        self.gestAlmMPCatTABLA = '//*[@id="catalogue-table"]/table/tbody/tr[1]/td[1]'
        self.gestAlMPCatTitXPath = '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]'
        self.gestAlMPCatBusXPath = '//*[@id="catalogue-action"]/div[1]'
        self.gestAlMPCatBusInput = '/html/body/div[2]/div[2]/div[3]/div/div[1]/div[1]/div[1]/div/input'
        self.gestAlMPCatBusValor = 'QA'
        self.gestAlMPCatNewTXT = 'Nuevo catálogo'
        self.gestAlmPCaMosXPath = '//*[@id="catalogue-action"]/div[2]'
        self.gestAlmPCaCo1XPath = '//*[@id="catalogue-table"]/table/thead/tr[1]/th[1]'
        self.gestAlmPCaCo2XPath = '//*[@id="catalogue-table"]/table/thead/tr[1]/th[2]'
        self.gestAlmPCaCo3XPath = '//*[@id="catalogue-table"]/table/thead/tr[1]/th[3]'
        self.gestAlmPCaCo4XPath = '//*[@id="catalogue-table"]/table/thead/tr[1]/th[4]'
        self.gestAlMPCatCTitTXT = 'CREACIÓN DE CATÁLOGO'
        self.gestAlMPCatCPas1XPath = '//*[@id="catalogue-space"]/div[2]/div[1]/div[1]/div[1]'
        self.gestAlMPCatCPas1TXT = 'Información básica'
        self.gestAlMPCatCPas2XPath = '//*[@id="catalogue-space"]/div[2]/div[1]/div[1]/div[2]'
        self.gestAlMPCatCPas2TXT = 'Añadir Productos de Proveedor'
        self.gestAlMPCatCPas3XPath = '//*[@id="catalogue-space"]/div[2]/div[1]/div[1]/div[3]'
        self.gestAlMPCatCPas3TXT = 'Añadir Almacenes'
        self.gestAlMPCatCAntXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/button[1]'
        self.gestAlMPCatCAntTXT = 'Anterior'
        self.gestAlMPCatCSigXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/button[2]'
        self.gestAlMPCatCSigTXT = 'Siguiente'
        self.gestAlMPCatCNomXPath = '//*[@id="catalogue-space"]/div[2]/div[2]/div/div[1]'
        self.gestAlMPCatCNomInput = '//*[@id="catalogue-space"]/div[2]/div[2]/div/div[1]/label/input'
        self.gestAlMPCatCNomValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '_Nombre'
        self.gestAlMPCatCDesXPath = '//*[@id="catalogue-space"]/div[2]/div[2]/div/div[2]'
        self.gestAlMPCatCDesInput = '//*[@id="catalogue-space"]/div[2]/div[2]/div/div[2]/label/input'
        self.gestAlMPCatCDesValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '_Descripción'
        self.gestAlMPCatCTab11XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlMPCatCTab12XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlMPCatCTab13XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/table/thead/tr[1]/th[3]/div/span'
        self.gestAlMPCatCTab21XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlMPCatCTab22XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/table/thead/tr[1]/th[3]/div/span'
        self.gestAlMPCatCTab23XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/table/thead/tr[1]/th[4]/div/span'
        self.gestAlMPCatCBus1XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/div[1]/div/input' # busco producto

        self.gestAlMPCatCBus2XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/div[1]/div/input' # busco producto en añadidos
        self.gestAlMPCatCBus3XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[4]/div/div[1]/div[1]/div/input' # busco almacén
        self.gestAlMPCatCAddXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/div[1]/button/span' # Añade el listado completo
        self.gestAlMPCatCAddTXT = 'Añadir listado'
        self.gestAlMPCatCAddOKXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[1]/td[4]' # Añado el primero
        self.gestAlMPCatCAdd2XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[1]/td[4]' # flecha para añadir
        self.gestAlMPCatCAdd2OKXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[4]'
        self.gestAlMPCatCQuiXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/div[1]/button/span'
        self.gestAlMPCatCQuiTXT = 'Quitar listado'
        self.gestAlMPCatCAdd2OKTXT = '3 BARRICAS, S.A'
        self.gestAlMPCatCAdd2KOXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/table/tbody/tr/td[1]/i'
        self.gestAlMPCatCAddAXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[4]/div/div[1]/table/tbody/tr/td[2]/i' # añadir almacén
        self.gestAlMPCatCAddAOKXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[4]/div/div[2]/table/tbody/tr/td[2]'
        self.gestAlMPCatCTab31XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[4]/div/div[1]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlMPCatCTab41XPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[4]/div/div[2]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlMPCatCTOKXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/button[2]/span'
        self.gestAlMPCDelXPath = '//*[@id="catalogue-table"]/table/tbody/tr/td[4]/div/i[3]' # Botón Borrar Catálogo
        self.gestAlMPCatDelXPath = '/html/body/div[14]/div/form/div[1]/p[2]'  # Catálogo buscado
        self.gestAlMPCatNewDelKOXPath = '//*[@id="deleteCatalogueModal"]/div/form/div[3]/button[1]'
        self.gestAlMPCatNewDelOKXPath = '//*[@id="deleteCatalogueModal"]/div/form/div[3]/button[2]'

# ingredientes--> MPI
        self.gestAlMPIngTitXPath = '/html/body/div[2]/div[2]/div[1]/div[1]/div'
        self.gestAlMPIngNewTXT = 'Nuevo ingrediente'
        self.gestAlMPIngURTXT = 'Unidad de receta'
        self.gestAlMPIngPETXT = 'Precio elegido'
        self.gestAlMPIngPMaxTXT = 'Precio máx.'
        self.gestAlMPIngPMinTXT = 'Precio mín.'
        self.gestAlMPIngPMedTXT = 'Precio medio'
        self.gestAlMPIngPMPTXT = 'Precio medio ponderado'
        self.gestAlMPIngCITXT = 'Controlar en inventario'
        self.gestAlMPIMCCIXPath = '/html/body/div[21]/div/form/div[1]/div[1]/div[1]/label/div' #  más columnas, codigo interno
        self.gestAlMPIMCURXPath = '/html/body/div[21]/div/form/div[1]/div[2]/div[2]/label/div' #  más columnas, unidad receta
        self.gestAlMPINITitXPath = '/html/body/div[14]/div/div[1]/span' #  Nuevo ingrediente
        self.gestAlMPINITitTXT = 'NUEVO INGREDIENTE'
        self.gestAlMPININomXPath = '/html/body/div[14]/div/form/div[1]/div[1]/label/div'
        self.gestAlMPININomInput = '/html/body/div[14]/div/form/div[1]/div[1]/label/input'
        self.gestAlMPININomValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '_Ingrediente'
        self.gestAlMPINIUReXPath = '//*[@id="newRecipeProductModal"]/div/form/div[1]/div[2]/label/div[1]' # Unidad de receta*
        self.gestAlMPINIUReSel = '/html/body/div[14]/div/form/div[1]/div[2]/label/div[2]/select'
        self.gestAlMPINIUReInput = '/html/body/div[14]/div/form/div[1]/div[2]/label/div[2]/select/option[4]'  # Listado unidad de receta
        self.gestAlMPINICatXPath = '/html/body/div[14]/div/form/div[1]/div[3]/div[1]/label/div[1]'
        self.gestAlMPINICatSel = '/html/body/div[14]/div/form/div[1]/div[3]/div[1]/label/div[2]/select'
        self.gestAlMPINICatInput = '/html/body/div[14]/div/form/div[1]/div[3]/div[1]/label/div[2]/select/option[3]'
        self.gestAlMPINITipCatXPath = '/html/body/div[14]/div/form/div[1]/div[3]/div[2]/label/div[1]'
        self.gestAlMPINITipCatTXT = 'Tipo de categoría*'
        self.gestAlMPINITipCatInput = '/html/body/div[14]/div/form/div[1]/div[3]/div[2]/label/div[2]/select'
        self.gestAlMPINITipCatValor = 'Bebida'
        self.gestAlMPINIContXPath = '//*[@id="newRecipeProductModal"]/div/form/div[1]/div[4]/label' # Contabilidad
        self.gestAlMPINIAlertXPath = '/html/body/div[14]/div/form/div[1]/div[5]/div[1]/label/div'
        self.gestAlMPINIAlertTXT = 'Mostrar alerta de stock bajo con cantidad inferior a*'
        self.gestAlMPINIAlertInput = '//*[@id="newRecipeProductModal"]/div/form/div[1]/div[5]/div[1]/label/input'
        self.gestAlMPINIAlertValor = '10'
        self.gestAlMPINIConInvXPath = '/html/body/div[14]/div/form/div[1]/div[5]/div[2]/label/label/div/span'
        self.gestAlMPINIConInvTXT = 'Controlar en inventario'
        self.gestAlMPINIConInvInput = '/html/body/div[14]/div/form/div[1]/div[5]/div[2]/label/label/div/i'
        self.gestAlMPINIMarXPath = '/html/body/div[14]/div/form/div[1]/div[6]/div[1]/label' # Marcas
        self.gestAlMPINIMarID = 'newBrandsMultiselect'  # Listado marcas
        self.gestAlMPINIMarValor = '/html/body/div[14]/div/form/div[1]/div[6]/div[1]/label/div/ul/li[4]'  # Lobrador
        self.gestAlMPINIKOXPath = '/html/body/div[14]/div/form/div[3]/button[1]'
        self.gestAlMPINIOKXPath = '/html/body/div[14]/div/form/div[3]/button[2]'
        self.gestAlMPINIOKTXT = 'Crear ingrediente'
        self.gestAlMPIBusXPath = '//*[@id="rawproduct-table"]/table/tbody/tr/td[1]'
        self.gestAlmPIDelXPath = '//*[@id="rawproduct-table"]/table/tbody/tr/td[10]/i[2]' # Botón eliminar, 1er elemento tabla
        self.gestAlMPINIDelKOXPath = '//*[@id="deleteRecipeProductModal"]/div/form/div[3]/button[1]'
        self.gestAlMPINIDelOKXPath = '//*[@id="deleteRecipeProductModal"]/div/form/div[3]/button[2]'
        self.gestAlMPIngEditXPath = '//*[@id="rawproduct-table"]/table/tbody/tr[1]/td[10]/i[1]' # Acción: Editar
        self.gestAlMPIngETitXPath = '//*[@id="editRecipeProductModal"]/div/div[1]/span'
        self.gestAlMPIngETitTXT = 'MODIFICAR PRODUCTO'
        self.gestAlMPIngENomXPath = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[1]/label/div' # Nombre*
        self.gestAlMPIngEURXPath = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[2]/label/div[1]' # Unidad de receta*
        self.gestAlMPIngECatXPath = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[3]/div[1]/label/div[1]' # Categoría*
        self.gestAlMPIngETCaXPath = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[3]/div[2]/label/div[1]' # Tipo de categoría*
        self.gestAlMPIngEContXPath = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[4]/label' # Contabilidad
        self.gestAlMPIngEAlertXPath = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[5]/div[1]/label/div' # Mostrar alerta de stock bajo con cantidad inferior a*
        self.gestAlMPIngEMarXPath = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[7]/div[1]/label' # Marcas
        self.gestAlMPIngEConInvXPath = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[5]/div[2]/label/label/div/span' # Controlar en inventario
        self.gestAlMPIngEKOXPath = '//*[@id="editRecipeProductModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlMPIngEOKXPath = '//*[@id="editRecipeProductModal"]/div/form/div[3]/button[2]' # Modificar
        self.gestAlMPIngENomInput = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[1]/label/input' # Nombre
        self.gestAlMPIngECatSel = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[3]/div[1]/label/div[2]/select/option[8]'# categoría
        self.gestAlMPIngECatInput = '//*[@id="editRecipeProductModal"]/div/form/div[1]/div[3]/div[1]/label/div[2]/select/option[8]'

# categorias --> MPCATEG
        self.gestAlMPCategTABLA = '//*[@id="rawproduct-table"]/table/tbody/tr[1]/td[1]'
        self.gestAlMPCategTitXPath = '/html/body/div[2]/div[2]/div[1]/div[1]/div'
        self.gestAlMPCategBusXPath = '//*[@id="rawproduct-action"]/div/span'
        self.gestAlMPCategBusInput = '//*[@id="rawproduct-action"]/div/div[1]/input'
        self.gestAlMPCategNewTXT = 'Nueva categoría'
        self.gestAlMPCategTipCatTXT = 'Tipo de categoría'
        self.gestAlMPCategIngGenTXT = 'Ingredientes genéricos'
        self.gestAlMPCategTypeInput = '/html/body/div[13]/div/form/div[1]/div[2]/label/div/select/option[2]'# Tipo de categoría, Bebida
        self.gestAlMPCategType2Input = '/html/body/div[14]/div/form/div[1]/div[2]/label/div[2]/select/option[2]'  # Tipo de categoría, Bebida
        self.gestAlMPCategNewTitXPath = '//*[@id="newCategoryModal"]/div/div[1]/span'
        self.gestAlMPCategNewTitTXT = 'NUEVA CATEGORÍA'
        self.gestAlMPCategNewNomXPath = '//*[@id="newCategoryModal"]/div/form/div[1]/div[1]/label/div'
        self.gestAlMPCategNewTCXPath = '//*[@id="newCategoryModal"]/div/form/div[1]/div[2]/label/div[1]'
        self.gestAlMPCategNewContXPath = '//*[@id="newCategoryModal"]/div/form/div[1]/div[3]/label'
        self.gestAlMPCategNewInput = '//*[@id="newCategoryModal"]/div/form/div[1]/div[1]/label/input'
        self.gestAlMPCategNewValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '_Categ'
        self.gestAlMPCategNewContInput = '//*[@id="newCategoryModal"]/div/form/div[1]/div[3]/label/input'
        self.gestAlMPCategNewContValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '_contabilidad'
        self.gestAlMPCategNewKOXPath = '//*[@id="newCategoryModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlMPCategNewOKXPath = '//*[@id="newCategoryModal"]/div/form/div[3]/button[2]' # Aceptar
        self.gestAlMPCategIGenXPath = '//*[@id="newCategoryModal"]/div/form/div[1]/div[4]/label/div/span'
        self.gestAlmBusCategValor = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr/td[2]'  # posicion del nuevo elemento en la tabla
        self.gestAlMPCategAEXPath = '//*[@id="rawproduct-table"]/table/tbody/tr/td[6]/i[1]' # accion:editar
        self.gestAlMPCategAETitXPath ='//*[@id="editCategoryModal"]/div/div[1]/span'
        self.gestAlMPCategEdiTitTXT = 'EDITAR CATEGORÍA'
        self.gestAlMPCategAENomXPath = '//*[@id="editCategoryModal"]/div/form/div[1]/div[1]/label/div'
        self.gestAlMPCategAETCXPath = '//*[@id="editCategoryModal"]/div/form/div[1]/div[2]/label/div[1]'
        self.gestAlMPCategAEContXPath = '//*[@id="editCategoryModal"]/div/form/div[1]/div[3]/label'
        self.gestAlMPCategAEIGenXPath = '//*[@id="editCategoryModal"]/div/form/div[1]/div[4]/label/div'
        self.gestAlMPCategAEKOXPath = '//*[@id="editCategoryModal"]/div/form/div[3]/button[1]'
        self.gestAlMPCategAEOKXPath = '//*[@id="editCategoryModal"]/div/form/div[3]/button[2]'
        self.gestAlMPCategADelXPath = '//*[@id="rawproduct-table"]/table/tbody/tr/td[6]/i[2]'  # accion: eliminar
        self.gestAlMPCategADelKOXPath = '//*[@id="deleteCategoryModal"]/div/form/div[3]/button[1]'
        self.gestAlMPCategADelOKXPath = '//*[@id="deleteCategoryModal"]/div/form/div[3]/button[2]'
        self.gestAlMPCategAENomInput = '//*[@id="editCategoryModal"]/div/form/div[1]/div[1]/label/input'
        self.gestAlMPCategAETypInput = '/html/body/div[15]/div/form/div[1]/div[2]/label/div[2]/select/option[3]'
        self.gestAlMPCategAEContInput = '//*[@id="editCategoryModal"]/div/form/div[1]/div[3]/label/input'

#unidades --> MPUNIT
        self.gestAlMPUnitTABLA = '//*[@id="unit-table"]/table/tbody/tr/td[1]'
        self.gestAlMPUFilXPath = '//*[@id="unit-action"]/div/div[2]/div/span' # Filtros
        self.gestAlMPUnitComXPath = '//*[@id="unit-action"]/div/div[2]/div/div[1]'
        self.gestAlMPUnitComTXT = 'Compra'
        self.gestAlMPUnitAlmXPath = '/html/body/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div[2]'
        self.gestAlMPUnitAlmTXT = 'Almacenamiento'
        self.gestAlMPUnitRecXPath = '//*[@id="unit-action"]/div/div[2]/div/div[3]'
        self.gestAlMPUnitRecTXT = 'Receta'
        self.gestAlMPUnitNewID = 'newUnit'
        self.gestAlMPUnitNewTXT = 'Nueva unidad'

        # Avanzar/retroceder página unidades
        self.gestAlMPUnitAvPXPath = '//*[@id="unit-table"]/div/div/div/ul/li[13]/a'
        self.gestAlMPUnitRePXPath = '//*[@id="unit-table"]/div/div/div/ul/li[1]/a'
        self.gestAlMPUnitPg5XPath = '//*[@id="unit-table"]/div/div/div/ul/li[6]/a/span'
        self.gestAlMPUnitPg5TXT = '5'
        self.gestAlMPUnitPg1XPath = '//*[@id="unit-table"]/div/div/div/ul/li[2]/a/span'
        self.gestAlMPUnitPg1TXT = '1'

        # Nueva unidad
        self.gestAlMPUnitNewTitXPath = '//*[@id="newUnitModal"]/div/div[1]/span'
        self.gestAlMPUnitNewTitTXT = 'NUEVA UNIDAD'
        self.gestAlMPUnitNewNomXPath = '//*[@id="newUnitModal"]/div/form/div[1]/div[1]/label/div' # Nombre*
        self.gestAlMPUnitNewAbrXPath = '//*[@id="newUnitModal"]/div/form/div[1]/div[2]/label' # Abreviatura
        self.gestAlMPUnitAbrTXT = 'Abreviatura'
        self.gestAlMPUnitNewComXPath = '//*[@id="newUnitModal"]/div/form/div[1]/div[3]/label[1]/div/span' # Compra
        self.gestAlMPUnitNewAlmXPath = '//*[@id="newUnitModal"]/div/form/div[1]/div[3]/label[2]/div/span' # Almacenamiento
        self.gestAlMPUnitNewRecXPath = '//*[@id="newUnitModal"]/div/form/div[1]/div[3]/label[3]/div/span' # Receta
        self.gestAlMPUnitNewKOXPath = '//*[@id="newUnitModal"]/div/form/div[3]/button[1]'
        self.gestAlMPUnitNewOKXPath = '//*[@id="newUnitModal"]/div/form/div[3]/button[2]'
        self.gestAlMPUnitNewNomInput = '//*[@id="newUnitModal"]/div/form/div[1]/div[1]/label/input'
        self.gestAlMPUnitNewNomValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '_UNIT'
        self.gestAlMPUnitNewAbrInput = '//*[@id="newUnitModal"]/div/form/div[1]/div[2]/label/input'
        self.gestAlMPUnitNewAbrValor = self.QA + '{:%d%m%y%H%M}'.format(self.datetime) + '_ABREV'
        self.gestAlmBusUnitInput = '/html/body/div[2]/div[2]/div[3]/div/div[1]/div/div[1]/input'
        self.gestAlmBusUnitValor = '/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr/td[2]/span'# posicion del nuevo elemento en la tabla
        self.gestAlMPUnitEditXPath = '//*[@id="unit-table"]/table/tbody/tr[1]/td[5]/i[1]'
        self.gestAlMPUnitModTitXPath = '//*[@id="editUnitModal"]/div/div[1]/span'
        self.gestAlMPUnitModTitTXT = 'MODIFICAR UNIDAD'
        self.gestAlMPUnitModNomXPath = '//*[@id="editUnitModal"]/div/form/div[1]/div[1]/label/div'
        self.gestAlMPUnitModAbrXPath = '//*[@id="editUnitModal"]/div/form/div[1]/div[2]/label'
        self.gestAlMPUnitModNomInput = '//*[@id="editUnitModal"]/div/form/div[1]/div[1]/label/input'
        self.gestAlMPUnitModNomValor = self.gestAlMPUnitNewNomValor + '_MODIF'
        self.gestAlMPUnitModAbrInput = '//*[@id="editUnitModal"]/div/form/div[1]/div[2]/label/input'
        self.gestAlMPUnitModAbrValor = self.gestAlMPUnitNewAbrValor + '_MODIF'
        self.gestAlMPUnitDelXPath = '//*[@id="unit-table"]/table/tbody/tr/td[5]/i[2]'
        self.gestAlMPUnitEditKOXPath = '//*[@id="editUnitModal"]/div/form/div[3]/button[1]'
        self.gestAlMPUnitEditOKXPath = '//*[@id="editUnitModal"]/div/form/div[3]/button[2]'
        self.gestAlMPUnitDelKOXPath = '//*[@id="deleteUnitModal"]/div/form/div[3]/button[1]'
        self.gestAlMPUnitDelOKXPath = '//*[@id="deleteUnitModal"]/div/form/div[3]/button[2]'

        # Mercancía,almacén
        self.gestAlMERATABLA = '/html/body/div[2]/div[2]/div[3]' # Almacenes cargados
        self.gestAlMERAIngXPath = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div[1]/div[1]/span' # INGREDIENTES
        self.gestAlMERAIng2Path = '/html/body/div[2]/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]' # Ingredientes
        self.gestAlMERASReXPath = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div[1]/span'  # SUBRECETAS
        self.gestAlMERASRe2XPath = '/html/body/div[2]/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]'  # Subrecetas
        self.gestAlMERAProdXPath = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div[1]/span'  # PRODUCTOS
        self.gestAlMERAProd2XPath = '/html/body/div[2]/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]'  # Producto
        self.gestAlMERATit2XPath = '//*[@id="warehouse-main"]/h2[1]'
        self.gestAlMERATit2TXT = 'ALMACENES INTERMEDIOS'
        self.gestAlMERATit3XPath  = '//*[@id="warehouse-main"]/div[1]/div'
        self.gestAlMERATit3TXT  = 'No hay almacenes intermedios'
        self.gestAlMERATit4XPath  = '//*[@id="warehouse-main"]/h2[2]'
        self.gestAlMERATit4TXT = 'ALMACENES DE RESTAURANTE'
        self.gestAlMERAlmXPath = '//*[@id="warehouse-main"]/div[2]/div[9]/div[2]/div[1]' # Almacén:(9) LTL Fleming
        self.gestAlMERAIc1XPath = '//*[@id="warehouse-main"]/div[2]/div[9]/div[1]/div[1]' # Circulo restaurante
        self.gestAlMERAIc2XPath = '//*[@id="warehouse-main"]/div[2]/div[9]/div[1]/div[2]' # icono email restaurante
        self.gestAlMERAVUbXPath = '//*[@id="warehouse-main"]/div[2]/div[9]/div[2]/div[3]' # Ver ubicaciones
        self.gestAlMERAVUbTXT = 'Ver ubicaciones'
        self.gestAlMERAEEmXPath = '//*[@id="mailModal"]/div/div[1]/span'
        self.gestAlMERAEEmTXT = 'EDITAR EMAIL'
        self.gestAlMERAEEmInput = '//*[@id="mailModal"]/div/form/div[1]/div/label/input'
        self.gestAlMERAETitXPath = '//*[@id="mailModal"]/div/form/div[1]/div/label'
        self.gestAlMERAETitTXT= 'Email'
        self.gestAlMERAEKOXPath = '//*[@id="mailModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlMERAEOKXPath = '//*[@id="mailModal"]/div/form/div[3]/button[2]' # Aceptar
        self.gestAlMERAUTitXPath = '//*[@id="contenttitle"]/div[1]/div[3]'
        self.gestAlMERAUTitTXT = 'UBICACIONES EN ALMACÉN - LTL FLEMING'
        self.gestAlMERAUIc1XPath = '//*[@id="storage-list"]/div/div[1]/div[1]/div' # icono1
        self.gestAlMERAUEdiXPath = '//*[@id="storage-list"]/div/div[1]/div[1]/i[1]' # editar ubicación1
        self.gestAlMERAUETitXPath = '//*[@id="editStorageModal"]/div/div[1]/span'
        self.gestAlMERAUETitTXT = 'EDITAR UBICACIÓN'
        self.gestAlMERAUENomXPath = '//*[@id="editStorageModal"]/div/form/div[1]/div/label/div'
        self.gestAlMERAUENomInput = '//*[@id="editStorageModal"]/div/form/div[1]/div/label/input'
        self.gestAlMERAUEKOXPath ='//*[@id="editStorageModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlMERAUEOKXPath ='//*[@id="editStorageModal"]/div/form/div[3]/button[2]' # Aceptar
        self.gestAlMERAUDTitXPath = '//*[@id="deleteStorageModal"]/div/div[1]/span'
        self.gestAlMERAUDTitTXT = 'ELIMINAR UBICACIÓN'
        self.gestAlMERAUDTit2XPath = '//*[@id="deleteStorageModal"]/div/form/div[1]/p[1]'
        self.gestAlMERAUDTit2TXT = '¿Está seguro de querer eliminar esta ubicación?'
        self.gestAlMERAUDSelXPath = '//*[@id="deleteStorageModal"]/div/form/div[1]/p[2]'
        self.gestAlMERAUDSelTXT = 'Congelado'
        self.gestAlMERAUDelXPath = '//*[@id="storage-list"]/div/div[1]/div[1]/i[2]' # borrar ubicacion1
        self.gestAlMERAUub1XPath = '//html/body/div[2]/div[2]/div[3]/div/div/div/div[1]/div[2]/div' # Congelado
        self.gestAlMERAUDKOXPath ='//*[@id="deleteStorageModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlMERAUDOKXPath ='//*[@id="deleteStorageModal"]/div/form/div[3]/button[2]' # Eliminar
        self.gestAlMERAUub1TXT = '(87) Congelado' # Nombre1
        self.gestAlMERAUub2XPath = '//*[@id="storage-list"]/div/div[2]/div[2]/div' # Texto2
        self.gestAlMERAUub2TXT = '(88) Refrigerado' # Nombre2
        self.gestAlMERAUub3XPath = '//*[@id="storage-list"]/div/div[3]/div[2]/div' # Texto3
        self.gestAlMERAUub3TXT = '(89) Sala' # Nombre3
        self.gestAlMERAUub4XPath = '//*[@id="storage-list"]/div/div[4]/div[2]/div' # Texto4
        self.gestAlMERAUub4TXT = '(90) Seco' # Nombre4

        self.gestAlMERASelTXT = 'STOCK EN ALMACÉN - LTL FLEMING'
        self.gestAlMERABusXPath = '//*[@id="warehouse-action"]/div[1]/span' # Buscar
        self.gestAlMERAMarXPath = '//*[@id="warehouse-action"]/div[1]/div[2]/span' # Marcas:
        self.gestAlMERABusInput = '//*[@id="warehouse-action"]/div[1]/div[1]/input'  # Buscar producto en almacen
        self.gestAlMERABusValor = 'CERVEZA HEINEKEN'
        self.gestAlMERACodIXPath = '//*[@id="warehouse-table"]/table/thead/tr[1]/th[1]/div/span' # Cod. Interno
        self.gestAlMERACodSelXPath = '//*[@id="warehouse-table"]/table/tbody/tr/td[1]'
        self.gestAlMERACodValor = '3848'
        self.gestAlMERAIngrXPath = '/html/body/div[2]/div[2]/div[3]/div/div[2]/div/table/thead/tr[1]/th[2]/div/span' # Ingrediente
        self.gestAlMERAIngSelXPath = '//*[@id="warehouse-table"]/table/tbody/tr/td[2]/span[1]'
        self.gestAlMERAIngValor = 'CERVEZA HEINEKEN (CAÑERO)'
        self.gestAlMERAIngSel2XPath = '//*[@id="warehouse-table"]/table/tbody/tr/td[2]/span[2]'
        self.gestAlMERAIng2Valor = '[LTL,PPZ,SGB,MQM]'
        self.gestAlMERACanXPath = '//*[@id="warehouse-table"]/table/thead/tr[1]/th[3]/div/span' # Cantidad
        self.gestAlMERACanSelXPath = '//*[@id="warehouse-table"]/table/tbody/tr/td[3]'
        #self.gestAlMERACanValor = '234.84'
        self.gestAlMERAUniSelXPath = '//*[@id="warehouse-table"]/table/tbody/tr/td[4]/div/select/option'
        self.gestAlMERAUniXPath = '//*[@id="warehouse-table"]/table/thead/tr[1]/th[4]/div/span' # Unidad
        self.gestAlMERAUniSelXPath = '//*[@id="warehouse-table"]/table/tbody/tr/td[4]/div/select'
        self.gestAlMERAUniValor = 'L'

        # consultar ubicación seleccionada
        self.gestAlMERAISTitXPath = '//*[@id="graphModal"]/div/div[1]/span'
        self.gestAlMERAISTitTXT = 'VISUALIZACIÓN DE STOCK'
        self.gestAlMERAISFIXPath = '//*[@id="graphModal"]/div/form/div[1]/div[1]/div[1]/label/div'
        self.gestAlMERAISFFXPath = '//*[@id="graphModal"]/div/form/div[1]/div[1]/div[2]/label/div'
        self.gestAlMERAISGrafID = 'chart'
        self.gestAlMERAISGraf2ID = 'canvas'
        self.gestAlMERAISOKXPath = '//*[@id="graphModal"]/div/form/div[3]/button' # Cerrar
        self.gestAlMERAISAspaXPath = '//*[@id="graphModal"]/div/div[1]/i' # Aspa
        self.gestAlMERAPrefTITXPath = '//*[@id="contenttitle"]/div[1]/div[4]' # 'PREFERENCIAS DE UBICACIÓN - CONGELADO'
        self.gestAlMERAPrefTITTXT ='PREFERENCIAS DE UBICACIÓN - CONGELADO'
        self.gestAlMERAPrefFilXPath ='//*[@id="storage-action"]/div[1]/div[2]/div/span'
        self.gestAlMERAVolID = 'backToStorage'
        self.gestAlMERAPrefSReXPath = '//*[@id="storage-action"]/div[1]/div[2]/div/div[2]'# Subrecetas
        self.gestAlMERAPrefProdXPath = '//*[@id="storage-action"]/div[1]/div[2]/div/div[3]' # Productos
        self.gestAlMERAPrefCPTXPath = '//*[@id="storage-action"]/div[2]/span' # Cambiar para todos:
        self.gestAlMERAPrefCPTTXT = 'Cambiar para todos:'
        self.gestAlMERAPTab1XPath = '//*[@id="storage-table"]/table/thead/tr[1]/th[1]/div/span'# Ingredientes, subrecetas y productos de carta
        self.gestAlMERAPTab1TXT = 'Ingredientes, subrecetas y productos de carta'
        self.gestAlMERAPTab2XPath = '//*[@id="storage-table"]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlMERAPTab2TXT = 'Mostrar'
        self.gestAlMERAPTab2OffTXT = '//*[@id="storage-table"]/table/tbody/tr/td[2]/label/div'
        self.gestAlMERAPRes1XPath = '//*[@id="storage-table"]/table/tbody/tr[1]/td[1]/span[2]' # ALHAMBRA
        self.gestAlMERAPRes1TXT = 'ALHAMBRA'
        self.gestAlMERAPResUltXPath = '//*[@id="storage-table"]/table/tbody/tr[9]/td[1]/span[2]' # P Alhambra Reservar
        self.gestAlMERAPResUlt2TXT = '1/3 Alhambra Reserva'
        self.gestAlMERAPResUltTXT = 'P Alhambra Reservar'
        self.gestAlMERAPrefDesIngXPath = '//*[@id="storage-table"]/table/tbody/tr[7]/td[2]' # no está al desactivar ingredientes
        self.gestAlMERAPrefDesProXPath = '//*[@id="storage-table"]/table/tbody/tr[4]/td[2]'  # no está al desactivar ingredientes
        self.gestAlMERAPrefCTTitXPath = '//*[@id="modifyAllStorageModal"]/div/div[1]/span'
        self.gestAlMERAPrefCTTitTXT = 'CAMBIAR TODOS'
        self.gestAlMERAPrefCTAspaXPath = '//*[@id="modifyAllStorageModal"]/div/div[1]/i' # aspa
        self.gestAlMERAPrefCTTit2XPath = '//*[@id="modifyAllStorageModal"]/div/form/div[1]/p[2]'
        self.gestAlMERAPrefCTTit2TXT = '¿Está seguro que quiere activar todos los ingredientes, subrecetas y productos para esta ubicación? (No se puede deshacer)'
        self.gestAlMERAPrefCTKOXPath = '//*[@id="modifyAllStorageModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlMERAPrefCTOKXPath = '//*[@id="modifyAllStorageModal"]/div/form/div[3]/button[2]' # Cambiar
        self.gestAlMERAPrefCTOKTXT = 'Cambiar'

    # INVENTARIO
        self.gestAlMERINIID = 'newInventory'
        self.gestAlMERINITXT = 'Nuevo inventario'
        self.gestAlMERIBusXPath = '//*[@id="inventory-action"]/div[1]/span' # Buscar
        self.gestAlMERIMarXPath = '//*[@id="inventory-action"]/div[1]/div[2]/span' # Marcas
        self.gestAlMERIAllXPath = '//*[@id="inventory-action"]/div[1]/div[2]/div/div/select/option[1]' # Todas
        self.gestAlMERIFilXPath = '//*[@id="inventory-action"]/div[1]/div[3]/div[1]/span' # Filtros
        self.gestAlMERIBorXPath = '//*[@id="inventory-action"]/div[1]/div[3]/div[1]/div[1]' # Borrador
        self.gestAlMERIProXPath = '//*[@id="inventory-action"]/div[1]/div[3]/div[1]/div[2]' # Programado
        self.gestAlMERIProTXT = 'Programado'
        self.gestAlMERIComXPath = '//*[@id="inventory-action"]/div[1]/div[3]/div[1]/div[3]' # Completado
        self.gestAlMERIFecXPath = '//*[@id="inventory-action"]/div[1]/div[3]/div[2]/span[1]' # Fecha
        self.gestAlMERIFec2XPath = '//*[@id="inventory-action"]/div[1]/div[3]/div[2]/span[2]'  # Valor de fecha
        self.gestAlMERIMosXPath = '//*[@id="inventory-action"]/div[2]'
        self.gestAlMERIFecInvXPath = '//*[@id="inventory-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlMERIFecInvTXT = 'Fecha de inventario'
        self.gestAlMERIFecCreXPath = '//*[@id="inventory-table"]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlMERIAlmXPath = '//*[@id="inventory-table"]/table/thead/tr[1]/th[3]/div/span'
        self.gestAlMERIUbiXPath = '//*[@id="inventory-table"]/table/thead/tr[1]/th[4]/div/span'
        self.gestAlMERIEstXPath = '//*[@id="inventory-table"]/table/thead/tr[1]/th[5]/div/span'
        self.gestAlMERICreXPath = '//*[@id="inventory-table"]/table/thead/tr[1]/th[6]/div/span'
        self.gestAlMERIAccXPath = '//*[@id="inventory-table"]/table/thead/tr[1]/th[7]/div/span'  # Acciones
        self.gestAlMERIFIInput = '//*[@id="dp1737972274766"]' # Fecha inicio, no va
        self.gestAlMERIFFInput = '//*[@id="dp1737972274767"]' # Fecha fin, no va
        self.gestAlMERIAlInput = '//*[@id="warehouseSearch"]/select/option[11]'  # LTL Fleming
        self.gestAlMERIUbInput = '//*[@id="locationSearch"]/select/option[2]'  # Congelado

        # Busqueda avanzada

        self.gestAlMERIBusAvdAlXPath = '//*[@id="warehouseSearch"]/select/option[10]'  # Almacén: LTL Fleming
        self.gestAlMERIBAResAlXPath = '//*[@id="inventory-table"]/table/tbody/tr/td[3]' # LTL Fleming
        #'/html/body/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr/td[3]'
        self.gestAlMERIBAResUbXPath = '//*[@id="inventory-table"]/table/tbody/tr/td[4]' # Congelado
        # Descargar plantilla
        self.gestAlMERIDPTitXPath = '//*[@id="downloadTemplateModal"]/div/div[1]/span'
        self.gestAlMERIDPTitTXT = 'DESCARGAR PLANTILLA'
        self.gestAlMERIDPAspaXPath ='//*[@id="downloadTemplateModal"]/div/div[1]/i' # Aspa
        self.gestAlMERIDPAlmXPath = '//*[@id="downloadTemplateModal"]/div/form/div[1]/div[1]/label' # Almacén
        self.gestAlMERIDPAlmInput ='//*[@id="downloadTemplateModal"]/div/form/div[1]/div[1]/label/div/select/option[12]'
        self.gestAlMERIDPUbiXPath = '//*[@id="downloadTemplateModal"]/div/form/div[1]/div[2]/label' # Ubicación
        self.gestAlMERIDPRITXPath = '//*[@id="downloadTemplateModal"]/div/form/div[1]/div[3]/label[1]/div/span' # Realizar inventario total
        self.gestAlMERIDPRITTXT = 'Realizar inventario total'
        self.gestAlMERIDPKOXPath = '//*[@id="downloadTemplateModal"]/div/form/div[3]/button[1]'
        self.gestAlMERIDPOKXPath = '//*[@id="downloadTemplateModal"]/div/form/div[3]/button[2]'
        # Nuevo inventario
        self.gestAlMERINTitTXT = 'INVENTARIO'
        self.gestAlMERINFEIXPath = '//*[@id="inventory-search"]/label[1]' # Fecha estimada de inventario
        self.gestAlMERINFEITXT = 'Fecha estimada de inventario'
        self.gestAlMERINAlmXPath = '//*[@id="inventory-search"]/label[2]' # Almacén
        self.gestAlMERINMUXPath = '//*[@id="inventory-search"]/label[3]'# Mostrar ubicaciones
        self.gestAlMERINMUTXT = 'Mostrar ubicaciones'
        self.gestAlMERINMUSelXPath = '//*[@id="whlocSelect"]/select'
        self.gestAlMERINMUSelTXT = 'Todos'
        self.gestAlMERINInfID = 'inventory-info'
        self.gestAlMERINInfTXT = 'Información: Los inventarios se procesan y aplican en horario nocturno. Hasta el día siguiente no verá el resultado del mismo en Tamus.'
        self.gestAlMERINFecXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/label[1]/input'  # Fecha: 1/2/2025
        self.gestAlMERINFec1Valor = '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[6]' # Fecha: 1/2/2025, 1/03/025
        self.gestAlMERINFec2Valor ='//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[1]' # Fecha: 10/X/2025
        self.gestAlMERINFec3Valor = '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[1]' # Fecha: 17/X/2025
        self.gestAlMERINFec4Valor = '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[1]' # Fecha: 24/2/2025
        self.gestAlMERINFec5Valor = '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[2]' # Fecha: 1/4/2025
        self.gestAlMERINFec6Valor = '//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[1]' # Fecha: 7/4/2025
        self.gestAlMERINFec7Valor = '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[7]'  # Fecha: 1/6/2025

        self.gestAlMERINSAXPath = '//*[@id="warehouseSelect"]/select'
        self.gestAlMERINASXPath = '//*[@id="warehouseSelect"]/select/option[12]' # LTL Fleming
        self.gestAlMERINGBID = 'saveInventory' # Guardar borrador
        self.gestAlMERINGBTXT = 'Guardar borrador'
        self.gestAlMERINRIID = 'summaryInventory'# Resumen del inventario
        self.gestAlMERINRITXT =  'Resumen del inventario'
        self.gestAlMERINAddIXPath = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div[1]/div[1]/div[1]/i'  # Añadir ingrediente
        self.gestAlMERINAddIUbiXPath = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[1]'  # Ubicación
        self.gestAlMERINAddIIngXPath = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[2]'  # Ingrediente:
        self.gestAlMERINAddIUniXPath = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[3]'  # Unidad
        self.gestAlMERINAddICanXPath = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[4]'  # Cantidad
        self.gestAlMERINAddIUbIValor = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[1]/div/select/option[4]' # Ubicación ingrediente: Sala
        self.gestAlMERINAddIUbI2Valor = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[1]/div/select/option[5]'  # Ubicación ingrediente: Seco
        self.gestAlMERINAddISelIInput ='//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input[1]' # Ingrediente
        self.gestAlMERINAddISelIValor = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[2]/div/ul/li[19]'# APEROL
        self.gestAlMERINAddISelInput = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input[1]' # desplegable ingrediente
        self.gestAlMERINAddISelI2Valor = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div[1]/div[2]/div/div[1]/form/div[2]/div/ul/li[3]'  # A MIM GAS NATURAL VR50
        self.gestAlMERINAddIUniInput = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[3]/div/select'
        self.gestAlMERINAddIUniValor = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[3]/div/select/option[2]' # BOTELLA (1000 ML)
        self.gestAlMERINAddIUni2Valor = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div[1]/div[2]/div/div[1]/form/div[3]/div/select/option[2]' # CAJA 20 BOTELLA
        self.gestAlMERINAddICanIInput = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[4]/input'
        self.gestAlMERINAddIOKXPath = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[5]/button' # Añadir producto
        self.gestAlMERINAddIOKTXT = 'Añadir producto'
        self.gestAlMERINAddIUbSRXPath = '//*[@id="inventory-accordion"]/div/div[2]/div[1]/span' # Subrecetas
        self.gestAlMERINAddIUbSRValor = '//*[@id="inventory-accordion"]/div/div[2]/div[2]/div/div[1]/form/div[1]/div/select/option[4]'  # Ubicación subreceta: Sala
        self.gestAlMERINAddISelSRInput = '//*[@id="inventory-accordion"]/div/div[2]/div[2]/div/div[1]/form/div[2]/div/input[1]'
        self.gestAlMERINAddISelValor = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[2]/div/ul' #menu ingrediente
        self.gestAlMERINAddISelSRValor = '//*[@id="inventory-accordion"]/div/div[2]/div[2]/div/div[1]/form/div[2]/div/ul/li[5]'  # AQUARIUS LIMON BAG-IN-BOX
        self.gestAlMERINAddICanSRInput = '//*[@id="inventory-accordion"]/div/div[2]/div[2]/div/div[1]/form/div[3]/input'
        self.gestAlMERINAddISROKXPath = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div[2]/div/div[1]/form/div[5]/button'  # Añadir producto
        self.gestAlMERINAddISROKTXT = 'Añadir subreceta'
        self.gestAlMERINAddIUbPXPath = '//*[@id="inventory-accordion"]/div/div[3]/div[1]/span' # Productos
        self.gestAlMERINAddIUbPValor = '//*[@id="inventory-accordion"]/div/div[3]/div[2]/div/div[1]/form/div[1]/div/select/option[4]'  # Ubicación producto: Sala
        self.gestAlMERINAddISelPInput = '//*[@id="inventory-accordion"]/div/div[3]/div[2]/div/div[1]/form/div[2]/div/input[1]'
        self.gestAlMecInput = '//*[@id="inventory-table"]/table/tbody/tr/td[1]' # Fecha inventario
        self.gestAlMERINAddISelPValor = '//*[@id="inventory-accordion"]/div/div[3]/div[2]/div/div[1]/form/div[2]/div/ul/li[2]' # 1/2 Mojito
        self.gestAlMERINAddICanPInput = '//*[@id="inventory-accordion"]/div/div[3]/div[2]/div/div[1]/form/div[3]/input'
        self.gestAlMERINAddIPOKXPath = '//*[@id="inventory-accordion"]/div/div[3]/div[2]/div/div[1]/form/div[4]/button'  # Añadir
        self.gestAlMERIBusInput = '//*[@id="inventory-action"]/div[1]/div[1]/input' # Buscar inventario
        self.gestAlMERIFecInput = '//*[@id="inventory-table"]/table/tbody/tr/td[1]' # Fecha inventario
        self.gestAlMERISelDelXPath = '//*[@id="inventory-table"]/table/tbody/tr/td[6]'
        self.gestAlMERSelIDelTXT = 'qa@tamus.io'
        self.gestAlMERIDelXPath = '//*[@id="inventory-table"]/table/tbody/tr/td[7]/i[3]' # icono borrar
        self.gestAlMERIDelTitXPath = '//*[@id="disableInventoryModal"]/div/div[1]/span' # ELIMINAR INVENTARIO
        self.gestAlMERIDelTitTXT = 'ELIMINAR INVENTARIO'
        self.gestAlMERIDelTit2XPath = '//*[@id="disableInventoryModal"]/div/form/div[1]/p[1]' # ¿Está seguro de...
        self.gestAlMERIDelTit2TXT = '¿Está seguro de querer eliminar este inventario?'
        self.gestAlMERIDelSelXPath = '//*[@id="disableInventoryModal"]/div/form/div[1]/p[2]'
        self.gestAlMERIDelKOXPath = '//*[@id="disableInventoryModal"]/div/form/div[3]/button[1]'
        self.gestAlMERIDelOKXPath = '//*[@id="disableInventoryModal"]/div/form/div[3]/button[2]'
        self.gestAlMERISeeXPath = '//*[@id="inventory-table"]/table/tbody/tr/td[7]/i[1]' # Ver inventario
        self.gestAlMERISeeIXPath = '//*[@id="inventory-accordion"]/div/div[1]/div[1]/span[2]' # (1 ingredientes),(2 ingredientes)
        self.gestAlMERISee1ITXT = '(1 ingredientes)'
        self.gestAlMERISee2ITXT = '(2 ingredientes)' # tiene q ser en minúscula
        self.gestAlMERISee1XPath = '//*[@id="inventory-accordion"]/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]' # APEROL
        self.gestAlMERISee1TXT = 'APEROL'
        self.gestAlMERISee2XPath = '//*[@id="inventory-accordion"]/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td[2]' # AQUARIUS LIMON BAG-IN-BOX
        self.gestAlMERISee2TXT = 'AQUARIUS LIMON BAG-IN-BOX'
        self.gestAlMERISee3XPath = '//*[@id="inventory-accordion"]/div/div[3]/div[2]/div/div[2]/table/tbody/tr/td[2]' # 1/2 Mojito
        self.gestAlMERISee3TXT = '1/2 Mojito'
        self.gestAlMERISeeAXPath = '/html/body/div[2]/div[2]/div[3]/div/div[3]/label[2]/div/select/option[11]' # Almacén: LTL Fleming
        self.gestAlMERISeeEditXPath = '//*[@id="inventory-table"]/table/tbody/tr/td[7]/i[2]' # Editar inventario
        self.gestAlMERISeeETitXPath = '//*[@id="editInventoryModal"]/div/div[1]/span'
        self.gestAlMERISeeETitTXT = 'EDITAR INVENTARIO'
        self.gestAlMERISeeETit2XPath = '//*[@id="editInventoryModal"]/div/form/div[1]/div[1]/h4'
        self.gestAlMERISeeETit2TXT = 'Escoge la ubicación de almacén que desea modificar'
        self.gestAlMERISeeEUbXPath = '//*[@id="editInventoryModal"]/div/form/div[1]/div[2]/label' # Ubicación
        self.gestAlMERISeeEUbValor = '//*[@id="editInventoryModal"]/div/form/div[1]/div[2]/label/div/select/option[3]' # Refrigerado
        self.gestAlMERISeeEAccXPath = '//*[@id="editInventoryModal"]/div/form/div[1]/div[4]/label' # Acción
        self.gestAlMERISeeEAccTXT = 'Acción'
        self.gestAlMERISeeEAccValor = '//*[@id="editInventoryModal"]/div/form/div[1]/div[4]/label/div/select/option[2]' # Añadir
        self.gestAlMERISeeEAddTXT = 'Añadir'
        self.gestAlMERISeeEKOXPath = '//*[@id="editInventoryModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlMERISeeEOKXPath = '//*[@id="editInventoryModal"]/div/form/div[3]/button[2]' # Aceptar

    # TRANSPASOS Y SALIDAS
        self.gestAlMERTSTitTXT = 'TRASPASOS Y SALIDAS'
        self.gestAlMERTSBusXPath = '//*[@id="stockmovement-action"]/div[1]/span'
        self.gestAlMERTSMarXPath = '//*[@id="stockmovement-action"]/div[1]/div[2]/span'
        self.gestAlMERTSAllXPath = '//*[@id="stockmovement-action"]/div[1]/div[2]/div/div/select/option[1]'
        self.gestAlMERTSCodIntXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlMERTSCodIntTXT = 'Cód. Interno'
        self.gestAlMERTSFecMovXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlMERTSFecMovTXT = 'Fecha del movimiento'
        self.gestAlMERTSFecCreXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[3]/div/span'
        self.gestAlMERTSNomXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[4]/div/span'
        self.gestAlMERTSCanXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[5]/div/span'
        self.gestAlMERTSUniXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[6]/div/span'
        self.gestAlMERTSAOriXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[7]/div/span'
        self.gestAlMERTSADesXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[8]/div/span'
        self.gestAlMERTSTMXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[9]/div/span'
        self.gestAlMERTSTMTXT = 'Tipo de movimiento'
        self.gestAlMERTSStXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[10]/div/span'
        self.gestAlMERTSAccXPath = '//*[@id="stockmovement-table"]/table/thead/tr[1]/th[11]/div/span'

        # Nuevo movimiento
        self.gestAlMERTSNMID = 'newStockMovement'
        self.gestAlMERTSNMTXT = 'Nuevo movimiento'
        self.gestAlMERTSNMOKID = 'submitInventory'
        self.gestAlMERTSNMOKTXT = 'Generar movimiento de stock'
        self.gestAlMERTSNMTitXPath = '//*[@id="newStockMovementModal"]/div/div[1]/span'
        self.gestAlMERTSNMTitTXT = 'NUEVO MOVIMIENTO'
        self.gestAlMERTSNMTit2XPath = '//*[@id="newStockMovementModal"]/div/form/div[1]/p'
        self.gestAlMERTSNMTit2TXT = '¿Qué tipo de movimiento de stock desea realizar?'
        self.gestAlMERTSNMT1XPath = '//*[@id="newStockMovementModal"]/div/form/div[1]/div/label/div[2]/label[1]/div/span'
        self.gestAlMERTSNMT1TXT = 'Traspaso entre almacenes'
        self.gestAlMERTSNMT2XPath = '//*[@id="newStockMovementModal"]/div/form/div[1]/div/label/div[2]/label[2]/div/span'
        self.gestAlMERTSNMT2TXT = 'Merma'
        self.gestAlMERTSNMT3XPath = '//*[@id="newStockMovementModal"]/div/form/div[1]/div/label/div[2]/label[3]/div/span'
        self.gestAlMERTSNMT3TXT = 'Comida de familia'
        self.gestAlMERTSNMT4XPath = '//*[@id="newStockMovementModal"]/div/form/div[1]/div/label/div[2]/label[4]/div/span'
        self.gestAlMERTSNMT4TXT = 'Consumo de ingredientes genéricos'
        self.gestAlMERTSNMT5XPath = '//*[@id="newStockMovementModal"]/div/form/div[1]/div/label/div[2]/label[5]/div/span'
        self.gestAlMERTSNMT5TXT = 'Buffet consumo'
        self.gestAlMERTSNMT6XPath = '//*[@id="newStockMovementModal"]/div/form/div[1]/div/label/div[2]/label[6]/div/span'
        self.gestAlMERTSNMT6TXT = 'Buffet merma'
        self.gestAlMERTSNMKOXPath = '//*[@id="newStockMovementModal"]/div/form/div[3]/button[1]'
        self.gestAlMERTSNMOKXPath = '//*[@id="newStockMovementModal"]/div/form/div[3]/button[2]'

    # BUFFET MERMA
        self.gestAlMERTSNMBMTitXPath = '//*[@id="contenttitle"]/div[1]/div[7]'
        self.gestAlMERTSNMBMTitTXT = 'BUFFET MERMA'
        self.gestAlMERTSNMBMTit2XPath = '//*[@id="stockmovement-search"]/label[1]'
        self.gestAlMERTSNMBMTit2TXT = 'Fecha de la variacion de stock'
        self.gestAlMERTSNMBMTit3XPath = '//*[@id="stockmovement-search"]/label[2]'
        self.gestAlMERTSNMBMSAXPath = '//*[@id="warehouseSourceSelect"]/select'
        self.gestAlMERTSNMBMASXPath = '//*[@id="warehouseSourceSelect"]/select/option[10]' # LTL Fleming
        self.gestAlMERTSNMBMPieXPath = '/html/body/div[2]/div[2]/div[3]/div/h4'
        self.gestAlMERTSNMBMPieTXT = 'Coste total: 0.00000 €'
        self.gestAlMERTSNMBMCol1XPath = '//*[@id="stockmovement-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[1]' # Ingrediente:
        self.gestAlMERTSNMBMCol1Input = '//*[@id="stockmovement-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input[1]'
        self.gestAlMERTSNMBMCol1Valor = '//*[@id="stockmovement-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[1]/div/ul/li[64]' # ALBAHACA
        self.gestAlMERTSNMBMCol2XPath = '//*[@id="stockmovement-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[2]' # Unidad
        self.gestAlMERTSNMBMCol2Input = '//*[@id="stockmovement-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[2]/div/select'
        self.gestAlMERTSNMBMCol2Valor = '//*[@id="stockmovement-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[2]/div/select/option[1]'
        self.gestAlMERTSNMBMCol3XPath = '//*[@id="stockmovement-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[3]' # Cantidad:
        self.gestAlMERTSNMBMCol3Input = '//*[@id="stockmovement-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[3]/input[1]'
        self.gestAlMERTSNMBMAddXPath = '//*[@id="stockmovement-accordion"]/div/div[1]/div[2]/div/div[1]/form/div[4]/button'
        self.gestAlMERTSNMBMTitOK1XPath = '//*[@id="confirmationModal"]/div/div[1]/span'
        self.gestAlMERTSNMBMTitOK1TXT = 'GENERAR MOVIMIENTO DE STOCK'
        self.gestAlMERTSNMBMTitOK2XPath = '//*[@id="confirmationModal"]/div/form/div[1]/p[1]'
        self.gestAlMERTSNMBMTitOK2TXT = '¿Está seguro de generar el movimiento de stock en esta fecha?'
        self.gestAlMERTSNMBMTitOK3XPath = '//*[@id="confirmationModal"]/div/form/div[1]/p[2]'
        self.gestAlMERTSNMBMKOXPath ='//*[@id="confirmationModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlMERTSNMBMOKXPath ='//*[@id="confirmationModal"]/div/form/div[3]/button[2]' # Aceptar
        self.gestAlMERTSNMBMXPath = '//*[@id="stockmovement-table"]/table/tbody/tr/td[1]'  # Buffet merma
        self.gestAlMERTSNMBMTXT = 'Buffet merma'
        self.gestAlMERTSNMFecXPath = '//*[@id="stockmovement-table"]/table/tbody/tr[1]/td[3]' # Fecha de creación
        self.gestAlMERTSNMFecMovXPath = '//*[@id="stockmovement-table"]/table/tbody/tr[1]/td[2]' # Fecha de movimiento
        self.gestAlMERTSNMBMStatusXPath = '//*[@id="stockmovement-table"]/table/tbody/tr[5]/td[10]/i' # Estado movimiento
        self.gestAlMERTSMBMKO2XPath = '//*[@id="stockmovement-table"]/table/tbody/tr[1]/td[11]/i' # Desactivar movimiento
        self.gestAlMERTSMBMKO2Tit1XPath = '//*[@id="unsavedModal"]/div/div[1]/span' # CAMBIOS SIN GUARDAR
        self.gestAlMERTSMBMKO2Tit1TXT = 'CAMBIOS SIN GUARDAR'
        self.gestAlMERTSMBMTitKOXPath = '//*[@id="confirmationCancelModal"]/div/div[1]/span'  # CANCELAR MOVIMIENTO DE STOCK
        self.gestAlMERTSMBMTitKOTXT = 'CANCELAR MOVIMIENTO DE STOCK'
        self.gestAlMERTSMBMTitKO2XPath = '//*[@id="confirmationCancelModal"]/div/form/div[1]/p'  # ¿Estás seguro que desea cancelar este movimiento de stock?
        self.gestAlMERTSMBMTitKO2TXT = '¿Estás seguro que desea cancelar este movimiento de stock?'
        self.gestAlMERTSMBMKOXPath = '//*[@id="confirmationCancelModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestAlMERTSMBMOKXPath = '//*[@id="confirmationCancelModal"]/div/form/div[3]/button[2]' # Aceptar

        self.gestAlMERTSBATMFDXPath = '//*[@id="stockmovement-table"]/table/tbody/tr[1]/td[2]' # Valor del campo Fecha del movimiento

    # DESCUADRES
        self.gestAlMERDesTitTXT = 'LISTADO DE DESCUADRES'
        self.gestAlMERDesBusXPath = '//*[@id="decrease-action"]/div[1]/span' # Buscar:
        self.gestAlMERDesMarXPath = '//*[@id="decrease-action"]/div[1]/div[2]/span' # Marcas:
        self.gestAlMERDesMarValor = '//*[@id="decrease-action"]/div[1]/div[2]/div/div/select/option[1]' # Todas
        self.gestAlMERDesFecXPath = '//*[@id="decrease-action"]/div[1]/div[3]/div/span[1]' # Fecha:
        self.gestAlMERDesFecValor = '//*[@id="decrease-action"]/div[1]/div[3]/div/span[2]'
        self.gestAlMERDesCol1XPath = '//*[@id="decrease-table"]/table/thead/tr[1]/th[1]/div/span'
        self.gestAlMERDesCol2XPath = '//*[@id="decrease-table"]/table/thead/tr[1]/th[2]/div/span'
        self.gestAlMERDesCol3XPath = '//*[@id="decrease-table"]/table/thead/tr[1]/th[3]/div/span'
        self.gestAlMERDesCol4XPath = '//*[@id="decrease-table"]/table/thead/tr[1]/th[4]/div/span'
        self.gestAlMERDesCol5XPath = '//*[@id="decrease-table"]/table/thead/tr[1]/th[5]/div/span'
        self.gestAlMERDesCol6XPath = '//*[@id="decrease-table"]/table/thead/tr[1]/th[6]/div/span'
        self.gestAlMERDesCol7XPath = '//*[@id="decrease-table"]/table/thead/tr[1]/th[7]/div/span'
        self.gestAlMERDesCol8XPath = '//*[@id="decrease-table"]/table/thead/tr[1]/th[8]/div/span'
        self.gestAlMERDesCol9XPath = '//*[@id="decrease-table"]/table/thead/tr[1]/th[9]/div/span'
        self.gestAlMERDesBASIXPath = '//*[@id="searchRawproduct"]/select'
        self.gestAlMERDesBAISXPath = '//*[@id="searchRawproduct"]/select/option[14]' # A MIM GAS CARBONATADA ALUMINIO
        self.gestAlMERDesBASAXPath = '//*[@id="searchWarehouse"]/select'
        self.gestAlMERDesBAASXPath = '//*[@id="searchWarehouse"]/select/option[10]'
        self.gestAlMERDesBAResXPath ='//*[@id="decrease-action"]/div[1]/div[3]/div[2]/span[1]' # Materias primas
        self.gestAlMERDesBARes1XPath = '//*[@id="decrease-action"]/div[1]/div[3]/div[2]/span[2]'  # A MIM GAS CARBONATADA ALUMINIO
        self.gestAlMERDesBARes1TXT = 'A MIM GAS CARBONATADA ALUMINIO'

    # PEDIDOS A PROVEEDOR / PEDIDOS DE CLIENTE
        self.gestALPEDProvTitTXT = 'LISTA DE PEDIDOS A PROVEEDOR'
        self.gestAlPEDBusXPath = '//*[@id="purchaseOrder-action"]/div[1]/span'
        self.gestAlPEDMarXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[2]/span'
        self.gestAlPEDMarValor = '//*[@id="purchaseOrder-action"]/div[1]/div[2]/div/div/select' # Todas
        self.gestAlPEDMarValorSel ='//*[@id="purchaseOrder-action"]/div[1]/div[2]/div/div/select/option[8]' # Volapié
        self.gestAlPEDFilXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[1]/span'
        self.gestAlPEDStCanXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[1]/div[1]' # Cancelados
        self.gestAlPEDStBorXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[1]/div[2]' # Borradores
        self.gestAlPEDStPteXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[1]/div[3]' # Pendientes
        self.gestAlPEDStEPXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[1]/div[4]' # En proceso
        self.gestAlPEDStComXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[1]/div[5]' # Completado
        self.gestAlPEDStIncXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[1]/div[6]' # Incidencias
        self.gestAlPEDStIncTXT = 'Incidencias'
        self.gestAlPEDFecXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[2]/span[1]' # Fecha
        self.gestAlPEDFecValor = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[2]/span[2]'  # Valor de fecha
        self.gestAlPEDPie1XPath = '//*[@id="purchaseOrder-table"]/div[2]/label[1]/div/span' # Mostrar totales entregados
        self.gestAlPEDPie1TXT = 'Mostrar totales entregados'
        self.gestAlPEDPie2XPath = '//*[@id="purchaseOrder-table"]/div[2]/label[2]/div/span' # Ocultar franquicias
        self.gestAlPEDPie2TXT = 'Ocultar franquicias'
        self.gestAlPEDPie3XPath = '//*[@id="purchaseOrder-table"]/div[3]' # Subtotal:X.XX €
        self.gestAlPEDPie3TXT = 'Subtotal:720.58 €'
        self.gestAlPEDPie4TXT =  'Subtotal:0.00 €'
        self.gestAlPEDSubEntXPath = '//*[@id="purchaseOrder-table"]/table/thead/tr[1]/th[7]/div/span' # Marcando, mostrar totales entregados
        self.gestAlPEDSubEntTXT = 'Subtotal (Entregado)' # Marcando, mostrar totales entregados

        # Nuevo pedido
        self.gestAlPEDN1FecXPath = '//*[@id="purchaseorder-header"]/div[1]/div[1]/label/span' # Fecha
        self.gestAlPEDN1AlmXPath = '//*[@id="purchaseorder-header"]/div[1]/div[2]/label/span' # Almacen
        self.gestAlPEDN1CrePorXPath = '//*[@id="purchaseorder-header"]/div[2]/div/label/span'  # Creado por
        self.gestAlPEDSubtXPath = '//*[@id="purchaseorder-total"]/div/span[1]' # Subtotal
        self.gestAlPEDSubtValor = '//*[@id="purchaseorder-total"]/div/span[2]' # 70.74 €
        self.gestAlPEDN1SAXPath = '//*[@id="warehouseSelect"]/select'
        self.gestAlPEDN1ASXPath = '//*[@id="warehouseSelect"]/select/option[10]' # LTL Fleming
        self.gestAlPEDN1BusXPath = '//*[@id="purchaseorderlines-action"]/div[1]'  # Buscar
        self.gestAlPEDN1CatXPath = '//*[@id="purchaseorderlines-action"]/div[2]'  #
        self.gestAlPEDN1BusInput = '//*[@id="purchaseorderlines-action"]/div[1]/div/input'
        self.gestAlPEDCol1XPath = '//*[@id="linesTable"]/thead/tr[1]/th[1]/div/span' # Ref.
        self.gestAlPEDCol2XPath = '//*[@id="linesTable"]/thead/tr[1]/th[2]/div/span' # Descripción
        self.gestAlPEDCol3XPath = '//*[@id="linesTable"]/thead/tr[1]/th[3]/div/span' # Unidad/Cantidad pedida
        self.gestAlPEDCol4XPath = '//*[@id="linesTable"]/thead/tr[1]/th[4]/div/span' # Proveedor/Cantidad enviada
        self.gestAlPEDCol5XPath = '//*[@id="linesTable"]/thead/tr[1]/th[5]/div/span' # Cantidad/Cantidad recibida
        self.gestAlPEDCol6XPath = '//*[@id="linesTable"]/thead/tr[1]/th[6]/div/span' # Precio/Cantidad devuelta
        self.gestAlPEDCol7XPath = '//*[@id="linesTable"]/thead/tr[1]/th[7]/div/span' # Importe/Unidad
        self.gestAlPEDN1SUXPath = '//*[@id="unitRppSelect"]/select' # Unidad
        self.gestAlPEDN1USXPath ='//*[@id="unitRppSelect"]/select/option[2]' # UD (50 L)
        self.gestAlPEDN1CanInput = '//*[@id="linesTable"]/tbody/tr/td[5]/input'
        self.gestAlPEDN1PreTXPath = '//*[@id="linesTable"]/tbody/tr/td[6]' # Precio resultante
        self.gestAlPEDN1ImpTXPath = '//*[@id="linesTable"]/tbody/tr/td[7]' # Importe resultante
        self.gestAlPEDN1SubTXPath = '//*[@id="purchaseorder-total"]/div/span[2]' # Subtotal resultante
        self.gestAlPEDN1MosPedXPath = '//*[@id="selectedCheckbox"]/label/div/span' # Mostrar ingredientes pedidos
        self.gestAlPEDN1MosPedTXT = 'Mostrar ingredientes pedidos'
        self.gestAlPEDN1PriEleXPath = '//*[@id="linesTable"]/tbody/tr/td[2]' # CERVEZA HEINEKEN (CAÑERO)
        self.gestAlPEDN1SegEleXPath ='//*[@id="linesTable"]/tbody/tr[1]/td[2]' # 7UP 20cl
        self.gestAlPEDN1ResPedTXT = 'Resumen del pedido'
        self.gestAlPEDN2STitXPath = '//*[@id="contenttitle"]/div[1]/div[3]' # RESUMEN DEL PEDIDO'
        self.gestAlPEDN2STitTXT = 'RESUMEN DEL PEDIDO'
        self.gestAlPEDN2SAlmXPath = '//*[@id="purchaseOrder-space"]/div[4]/h4' # Almacén: LTL Fleming
        self.gestAlPEDN2SAlmTXT = 'Almacén: LTL Fleming'
        self.gestAlPEDN2ProvSelXPath = '//*[@id="confirmationProvider"]/h3'
        self.gestAlPEDN2ProvSelTXT = 'HEINEKEN ESPAÑA, S.A.'
        self.gestAlPEDN2UdSelTXT = 'UD(50l)'
        self.gestAlPEDN2UdSel2TXT = 'UD (50 L)'
        self.gestAlPEDN2FPXPath = '//*[@id="minimumImport"]/h4'
        self.gestAlPEDN2FPTXT = 'Fecha de pedido: ' + self.hoy
        self.gestAlPEDN2DesXPath = '//*[@id="confirmationProvider"]/table/tbody/tr[1]/th[1]' # Descripción
        self.gestAlPEDN2UdXPath = '//*[@id="confirmationProvider"]/table/tbody/tr[1]/th[2]' # Unidad
        self.gestAlPEDN2ProvXPath = '//*[@id="confirmationProvider"]/table/tbody/tr[1]/th[3]'# Proveedor
        self.gestAlPEDN2CanXPath = '//*[@id="confirmationProvider"]/table/tbody/tr[1]/th[4]'# Cantidad
        self.gestAlPEDN2PreXPath = '//*[@id="confirmationProvider"]/table/tbody/tr[1]/th[5]'# Precio
        self.gestAlPEDN2ImpXPath = '//*[@id="confirmationProvider"]/table/tbody/tr[1]/th[6]'# Importe
        self.gestAlPEDN2DesValor = '//*[@id="confirmationProvider"]/table/tbody/tr[2]/td[1]' # CERVEZA HEINEKEN(CAÑERO)
        self.gestAlPEDN2UdValor = '//*[@id="confirmationProvider"]/table/tbody/tr[2]/td[2]' # UD(50l)
        self.gestAlPEDN2ProvValor = '//*[@id="confirmationProvider"]/table/tbody/tr[2]/td[3]' # HEINEKEN ESPAÑA, S.A.
        self.gestAlPEDN2CanValor = '//*[@id="confirmationProvider"]/table/tbody/tr[2]/td[4]' # 1
        self.gestAlPEDN2PreValor = '//*[@id="confirmationProvider"]/table/tbody/tr[2]/td[5]' # 70.74 €
        self.gestAlPEDN2ImpValor = '//*[@id="confirmationProvider"]/table/tbody/tr[2]/td[6]' # 70.74 €
        self.gestAlPEDN2NotasXPath = '//*[@id="notes"]/textarea'
        self.gestAlPEDN2NotasTXT = 'Notas para el proveedor'
        self.gestAlPEDN2Subt1XPath = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div/div[2]/div[2]/div/span[1]' # Subtotal
        self.gestAlPEDN2Subt2XPath = '/html/body/div[2]/div[2]/div[3]/div/div[4]/div/div/div[2]/div[2]/div/span[2]' # 70.74 €
        self.gestAlPEDN2ConfPedID = 'confirmPurchaseorder'
        self.gestAlPEDN2ConfPedTXT = 'Confirmar pedido'
        self.gestAlPEDOp2XPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr[1]/td[11]/i[2]' # Generar albarán de entrada(folio)

        # Búsqueda avanzada, pedidos
        self.gestAlPEDBAXPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr/td[3]'
        self.gestAlPED1XPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr[1]/td[3]'
        self.gestAlPED2XPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr[2]/td[3]'
        self.gestAlPED3XPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr[3]/td[3]'
        #self.gestAlPED1TXT = 'P2507/198572'
        #self.gestAlPED2TXT = 'P2524/198573'
        #self.gestAlPED3TXT = 'P2509/198577'

        self.gestAlPEDBAEPXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[1]/div[5]' # En proceso
        self.gestAlPEDBAComXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[3]/div[1]/div[5]'  # Completado
        self.gestAlPEDseaXPath = '//*[@id="purchaseOrder-action"]/div[1]/div[1]/input' # Buscar pedido
        self.gestAlPEDseeXPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr/td[11]/i[1]' # ojo
        self.gestAlPEDExpXPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr[1]/td[11]' # imprimir pedido,exportar
        self.gestAlPEDTitExpXPath ='//*[@id="printPurchaseOrderModal"]/div/div[1]/span' # EXPORTAR
        self.gestAlPEDTit2ExpXPath = '//*[@id="modalMessage"]/p'
        self.gestAlPEDTit2ExpTXT = '¿Desea incluir los precios de cada producto en el PDF?'
        self.gestAlPEDKOExpXPath = '//*[@id="printPurchaseOrderModal"]/div/form/div[3]/button[1]'
        self.gestAlPEDKOExTXT = 'Cancelar'
        self.gestAlPEDOKExpXPath = '//*[@id="printPurchaseOrderModal"]/div/form/div[3]/button[2]'
        self.gestAlPEDOKExpTXT = 'Valorado'
        self.gestAlPEDNVExpXPath = '//*[@id="printPurchaseOrderModal"]/div/form/div[3]/button[3]'
        self.gestAlPEDNVExpTXT = 'NO valorado'
        self.gestAlPEDPed1XPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr[1]/td[3]'
        self.gestAlPEDPed2XPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr[2]/td[3]'
        self.gestAlPEDPed3XPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr[3]/td[3]'
        self.gestAlPEDseeFecXPath = '//*[@id="purchaseorder-header"]/div[1]/div[1]/label/span' # Fecha
        self.gestAlPEDseeCPXPath = '//*[@id="purchaseorder-header"]/div[2]/div[1]/label/span' # Creado por
        self.gestAlPEDseeRefXPath = '//*[@id="purchaseorder-header"]/div[1]/div[2]/label/span' # Referencia
        self.gestAlPEDseeStaXPath = '//*[@id="purchaseorder-header"]/div[2]/div[2]/label/span' # Estado
        self.gestAlPEDseeAlmXPath = '//*[@id="purchaseorder-header"]/div[1]/div[3]/label/span'  # Almacén
        self.gestAlPEDseeNotXPath = '//*[@id="purchaseorder-header"]/div[2]/div[3]/label/span' # Notas
        self.gestAlPEDseeProvXPath = '//*[@id="providerInput"]/label/span'  # Proveedor
        self.gestAlPEDseeCanPedTXT = 'Cantidad pedida'
        self.gestAlPEDseeCanEnvTXT = 'Cantidad enviada'
        self.gestAlPEDseeCanRecTXT = 'Cantidad recibida'
        self.gestAlPEDseeCanDevTXT = 'Cantidad devuelta'
        self.gestAlPEDseeASXPath = '//*[@id="warehouseSelect"]/select/option[9]' # LTL Fleming
        self.gestAlPEDCol8XPath = '//*[@id="linesTable"]/thead/tr[1]/th[8]/div/span'  # Precio
        self.gestAlPEDCol9XPath = '//*[@id="linesTable"]/thead/tr[1]/th[9]/div/span'  # Importe
        self.gestAlPEDCol10XPath = '//*[@id="linesTable"]/thead/tr[1]/th[10]/div/span' # Notas
        self.gestAlPEDCol1Value = '//*[@id="linesTable"]/tbody/tr/td[1]'
        self.gestAlPEDCol1Valor = '37'
        self.gestAlPEDCol2Value = '//*[@id="linesTable"]/tbody/tr/td[2]'
        self.gestAlPEDCol2Valor = 'Heineken Barril 50 L.'
        self.gestAlPEDCol3Value = '//*[@id="linesTable"]/tbody/tr/td[3]'
        self.gestAlPEDCol4Value = '//*[@id="linesTable"]/tbody/tr/td[4]'
        self.gestAlPEDCol5Value = '//*[@id="linesTable"]/tbody/tr/td[5]'
        self.gestAlPEDCol6Value = '//*[@id="linesTable"]/tbody/tr/td[6]'
        self.gestAlPEDCol7Value = '//*[@id="linesTable"]/tbody/tr/td[7]'
        self.gestAlPEDCol8Value = '//*[@id="linesTable"]/tbody/tr/td[8]'
        self.gestAlPEDCol9Value = '//*[@id="linesTable"]/tbody/tr/td[8]'
        # Búsqueda por marca, pedidos
        self.gestAlPEDMarProXPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr/td[5]'
        self.gestAlPEDMarProTXT = 'OMS Y VIñAS SL'
        self.gestAlPEDMarAlmXPath = '//*[@id="purchaseOrder-table"]/table/tbody/tr/td[6]'
        self.gestAlPEDMarAlmTXT = 'TDV Sanchinarro'

    # PEDIDOS, ALBARÁN DE ENTRADA/SALIDA
        self.gestALPEDAlbTitTXT = 'LISTADO DE ALBARANES DE ENTRADA'
        self.gestALPEDAlbTit2TXT = 'LISTADO DE ALBARANES DE SALIDA'
        self.gestAlPEDAlbBusXPath = '//*[@id="delivery-action"]/div[1]/span' # Buscar:
        self.gestAlPEDAlbBusInput = '//*[@id="delivery-action"]/div[1]/div[1]/input' # Buscar:
        self.gestAlPEDAlbBusValue = '//*[@id="delivery-table"]/table/tbody/tr/td[2]' # Primera referencia de la tabla
        self.gestAlPEDAlbBus2Value = '//*[@id="delivery-table"]/table/tbody/tr[1]/td[2]' # Primera referencia de la tabla
        self.gestAlPEDAlbOjoXPath = '//*[@id="delivery-table"]/table/tbody/tr[1]/td[10]/i[1]' # Ojo primer albarán entrada
        self.gestAlPEDAlbOjo2XPath = '//*[@id="delivery-table"]/table/tbody/tr/td[11]/i[1]'  # Ojo primer albarán salida
        self.gestAlPEDAlbMarXPath = '//*[@id="delivery-action"]/div[1]/div[2]/span' # Marcas:
        self.gestAlPEDAlbMarAllXPath = '//*[@id="delivery-action"]/div[1]/div[2]/div/div/select/option[1]' # Todas
        self.gestAlPEDAlbFecXPath = '//*[@id="delivery-action"]/div[1]/div[3]/div/span[1]' # Fecha: en albarán de entrada
        self.gestAlPEDAlbFec2XPath = '//*[@id="delivery-action"]/div[1]/div[3]/div[2]/span[1]' # Fecha: en albarán de salida
        self.gestAlPEDAlbFilXPath = '//*[@id="delivery-action"]/div[1]/div[3]/div[1]/span' # Filtros:
        self.gestAlPEDAlbFecValor = '//*[@id="delivery-action"]/div[1]/div[3]/div/span[2]'
        self.gestAlPEDAlbSta1XPath = '//*[@id="delivery-action"]/div[1]/div[3]/div[1]/div[1]' # Devolución
        self.gestAlPEDAlbSta2XPath = '//*[@id="delivery-action"]/div[1]/div[3]/div[1]/div[2]' # Entrega
        self.gestAlPEDAlbSta3XPath = '//*[@id="delivery-action"]/div[1]/div[3]/div[1]/div[3]' # Otros
        self.gestAlPEDAlbCol1XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[1]/div/span' # Cód. Interno
        self.gestAlPEDAlbCol2XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[2]/div/span'  # Referencia
        self.gestAlPEDAlbCol3XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[3]/div/span'  # Fecha
        self.gestAlPEDAlbCol4XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[4]/div/span'  # Proveedor
        self.gestAlPEDAlbCol5XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[5]/div/span'  # Almacén
        self.gestAlPEDAlbCol6XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[6]/div/span'  # Subtotal
        self.gestAlPEDAlbCol7XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[7]/div/span' # Estado
        self.gestAlPEDAlbCol8XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[8]/div/span'  # Pedido
        self.gestAlPEDAlbCol9XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[9]/div/span'  # Creado por
        self.gestAlPEDAlbCol10XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[10]/div/span'  # Acciones/Motivo
        self.gestAlPEDAlbCol11XPath = '//*[@id="delivery-table"]/table/thead/tr[1]/th[11]/div/span'  # Acciones
        self.gestAlPEDAlbCol10TXT = 'Motivo'
        self.gestAlPEDAlbPie1XPath = '//*[@id="delivery-table"]/div[2]/span[1]'  # Subtotal:
        self.gestAlPEDAlbPie2XPath = '//*[@id="delivery-table"]/div[2]/span[2]'  # 70.74 €
        #self.gestAlPEDAlbPie1TXT = '181.74 €'
        #self.gestAlPEDAlbPie2TXT = '74.00 €'
        self.gestAlPEDAlbPie3TXT = '0.00 €'
        self.gestALAlbBAFIXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[2]/div[1]/label' # Fecha inicio*
        self.gestALAlbBAFFXPath = '//*[@id="advancedSearchModal"]/div/form/div[1]/div[2]/div[2]/label' # Fecha fin*
        #Nuevo albarán
        self.gestALPEDNAlbTitTXT ='ALBARÁN DE ENTRADA'
        self.gestALPEDNAlbTit2TXT ='ALBARÁN DE SALIDA'
        self.gestALPEDNAlbFecXPath = '//*[@id="delivery-header"]/div[1]/div[1]/label/span' # Fecha
        self.gestALPEDNAlbRefXPath = '//*[@id="delivery-header"]/div[1]/div[2]/label/span' # Referencia
        self.gestALPEDNAlbAlmXPath = '//*[@id="delivery-header"]/div[1]/div[3]/label/span' # Almacén
        self.gestALPEDNAlbProvXPath = '//*[@id="delivery-header"]/div[1]/div[4]/label/span' # Proveedor
        self.gestALPEDNAlbCPXPath = '//*[@id="delivery-header"]/div[2]/div/label/span' # Creado por
        self.gestALPEDNAlbB1XPath = '//*[@id="delivery-form"]/form/label[1]/span' # Ref.
        self.gestALPEDNAlbB2XPath = '//*[@id="delivery-form"]/form/label[2]/span' # Descripción
        self.gestALPEDNAlbB3XPath = '//*[@id="delivery-form"]/form/label[3]/span' # Cantidad
        self.gestALPEDNAlbB4XPath = '//*[@id="delivery-form"]/form/label[4]/span' # Unidad
        self.gestALPEDNAlbB5XPath = '//*[@id="delivery-form"]/form/label[5]/span' # Precio
        self.gestALPEDNAlbB6XPath = '//*[@id="delivery-form"]/form/label[6]/span' # Descuento
        self.gestALPEDNAlbB7XPath = '//*[@id="delivery-form"]/form/label[7]/span' # Importe
        self.gestALPEDNAlbB8XPath = '//*[@id="delivery-form"]/form/label[8]/span' # Importe desc.
        self.gestALPEDNAlbC1XPath = '//*[@id="delivery-lines"]/table/thead/tr[1]/th[1]/div/span' # Ref.
        self.gestALPEDNAlbC2XPath = '//*[@id="delivery-lines"]/table/thead/tr[1]/th[2]/div/span'  # Descripción
        self.gestALPEDNAlbC3XPath = '//*[@id="delivery-lines"]/table/thead/tr[1]/th[3]/div/span'  # Cantidad
        self.gestALPEDNAlbC4XPath = '//*[@id="delivery-lines"]/table/thead/tr[1]/th[4]/div/span'  # Unidad
        self.gestALPEDNAlbC5XPath = '//*[@id="delivery-lines"]/table/thead/tr[1]/th[5]/div/span'  # Precio
        self.gestALPEDNAlbC6XPath = '//*[@id="delivery-lines"]/table/thead/tr[1]/th[6]/div/span'  # Descuento
        self.gestALPEDNAlbC7XPath = '//*[@id="delivery-lines"]/table/thead/tr[1]/th[7]/div/span'  # Importe
        self.gestALPEDNAlbC8XPath = '//*[@id="delivery-lines"]/table/thead/tr[1]/th[8]/div/span'  # Importe desc.
        self.gestALPEDNAlbC9XPath = '//*[@id="delivery-lines"]/table/thead/tr[1]/th[9]/div/span'  # Acciones
        self.gestALPEDNAlbPie1XPath = '//*[@id="delivery-total"]/div/span[1]' # Subtotal
        self.gestALPEDNAlbPie2XPath = '//*[@id="delivery-total"]/div/span[2]' #  €
        self.gestALPEDNAlbAddInput = '//*[@id="delivery-form"]/form/input' # Botón: Añadir,Modificar
        self.gestALPEDNAlbErrorTitXPath = '//*[@id="missingLinesModal"]/div/div[1]/span' # FALTAN LíNEAS
        self.gestALPEDNAlbErrorTitTXT = 'FALTAN LÍNEAS'
        self.gestALPEDNAlbErrorTit2XPath = '//*[@id="missingLinesModal"]/div/form/div[1]/p' # Para guardar o enviar el albarán, tiene que contener al menos una línea.
        self.gestALPEDNAlbErrorTit2TXT = 'Para guardar o enviar el albarán, tiene que contener al menos una línea.'
        self.gestALPEDNAlbErrorOKXPath = '//*[@id="missingLinesModal"]/div/form/div[3]/button' # Cerrar
        self.gestALPEDNAlbRefInput = '//*[@id="delivery-header"]/div[1]/div[2]/label/input' # Referencia
        self.gestALPEDNAlbMotXPath = '//*[@id="delivery-header"]/div[2]/div[2]/label/span' # Motivo, albarán de salida
        self.gestALPEDNAlbMotTXT = 'Motivo'
        self.gestALPEDNAlbMotInput = '//*[@id="deliveryReasonSelect"]/select/option[3]' # Entrega a cliente
        self.gestALPEDNAlbAlmInput = '//*[@id="warehouseSelect"]/select' # Almacén
        self.gestALPEDNAlbAlmValor = '//*[@id="warehouseSelect"]/select/option[10]' # LTL Fleming
        self.gestALPEDNAlbProvInput = '//*[@id="providerSelect"]/select' # Proveedor
        self.gestALPEDNAlbProvValor = '//*[@id="providerSelect"]/select/option[7]' # MAHOU, S.A.
        self.gestALPEDNAlbProv2Valor = '//*[@id="providerSelect"]/select/option[38]' # MAHOU, S.A.
        self.gestALPEDNAlbRef2Input = '//*[@id="referenceSelect"]/select' # Referencia
        self.gestALPEDNAlbRefValor = '//*[@id="referenceSelect"]/select/option[4]' # 235 BT
        self.gestALPEDNAlbRefValor2 = '//*[@id="referenceSelect"]/select/option[5]' # 235 BT
        self.gestALPEDNAlbRef2Valor = '//*[@id="referenceSelect"]/select/option[4]' #
        self.gestALPEDNAlbRef2Valor2 = '//*[@id="referenceSelect"]/select/option[5]' #
        self.gestALPEDNAlbEditXPath = '//*[@id="delivery-lines"]/table/tbody/tr/td[9]/i[1]' # Botón: Editar
        self.gestALPEDNAlbDelXPath = '//*[@id="delivery-lines"]/table/tbody/tr[2]/td[9]/i[2]' # Botón: Borrar
        self.gestALPEDAlbRecTit1XPath = '//*[@id="rejectModal"]/div/div[1]/span' # RECHAZAR ALBARÁN
        self.gestALPEDAlbRecTit1TXT = 'RECHAZAR ALBARÁN'
        self.gestALPEDAlbRecTit2XPath = '//*[@id="rejectModal"]/div/form/div[1]/p' # ' Va a rechazar un albarán validado. Esto causará ..
        self.gestALPEDAlbRecTit2TXT = 'Va a rechazar un albarán validado. Esto causará cambios en el stock disponible. ¿Está seguro de rechazar el albarán?'
        self.gestALPEDAlbRecKOXPath = '//*[@id="rejectModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestALPEDAlbRecOKXPath = '//*[@id="rejectModal"]/div/form/div[3]/button[2]' # Aceptar
        self.gestALPEDAlbDelXPath = '//*[@id="delivery-table"]/table/tbody/tr[1]/td[10]/i[3]' # Botón eliminar albarán de entrada
        self.gestALPEDAlbDel2XPath = '//*[@id="delivery-table"]/table/tbody/tr/td[11]/i[3]' # Botón eliminar albarán de salida
        self.gestALPEDAlbDelTit1XPath = '//*[@id="deleteDeliveryModal"]/div/div[1]/span' # ELIMINAR ALBARÁN
        self.gestALPEDAlbDelTit1TXT = 'ELIMINAR ALBARÁN'
        self.gestALPEDAlbDelTit2XPath = '//*[@id="deleteDeliveryModal"]/div/form/div[1]/p[2]' # ¿Está seguro de eliminar este albarán?
        self.gestALPEDAlbDelTit2TXT = '¿Está seguro de eliminar este albarán?'
        self.gestALPEDAlbDelKOXPath = '//*[@id="deleteDeliveryModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestALPEDAlbDelOKXPath = '//*[@id="deleteDeliveryModal"]/div/form/div[3]/button[2]' # Eliminar
        self.gestALPEDCLITitTXT = 'LISTA DE PEDIDOS DE CLIENTES'

    # PEDIDOS, COMPRAS EXTERNAS
        self.gestALPEDCETitTXT = 'COMPRAS EXTERNAS'
        self.gestAlPEDCEBusXPath = '//*[@id="externalpurchase-action"]/div[1]/span' # Buscar
        self.gestAlPEDCEMarXPath = '//*[@id="externalpurchase-action"]/div[1]/div[2]/span' # Marcas
        self.gestAlPEDCEAllXPath = '//*[@id="externalpurchase-action"]/div[1]/div[2]/div/div/select' # Todas
        self.gestAlPEDCEMosXPath = '//*[@id="externalpurchase-action"]/div[2]'  # Mostrando...
        self.gestALPEDNCEID = 'newExternalPurchase' # Nueva compra
        self.gestALPEDNCETXT = 'Nueva compra'
        self.gestALPEDCEC1XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[1]/div/span'  # Cód. interno
        self.gestALPEDCEC2XPath ='//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[2]/div/span' # Almacén
        self.gestALPEDCEC3XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[3]/div/span' # Fecha de creación
        self.gestALPEDCEC4XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[4]/div/span'  # Fecha de compra
        self.gestALPEDCEC5XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[5]/div/span' # Nombre
        self.gestALPEDCEC6XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[6]/div/span' # Cantidad
        self.gestALPEDCEC7XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[7]/div/span' # Unidad
        self.gestALPEDCEC8XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[8]/div/span' # Precio unitario (€)
        self.gestALPEDCEC9XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[9]/div/span' # Total
        self.gestALPEDCEC10XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[10]/div/span' # Total + IVA
        self.gestALPEDCEC11XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[11]/div/span'  # IVA
        self.gestALPEDCEC12XPath = '//*[@id="externalpurchase-table"]/table/thead/tr[1]/th[12]/div/span'  # Acciones
        # Nueva compra externa
        self.gestALPEDNCEOKID = 'submitPurchase' # Generar compra externa
        self.gestALPEDNCEOKTXT = 'Generar compra externa'
        self.gestALPEDNCEFVSXPath = '//*[@id="externalpurchase-search"]/label[1]' # Fecha de la variacion de stock
        self.gestALPEDNCEFVSTXT = 'Fecha de la variacion de stock'
        self.gestALPEDNCEAlmXPath = '//*[@id="externalpurchase-search"]/label[2]' # Almacén
        self.gestALPEDNCEIngXPath = '//*[@id="externalpurchase-accordion"]/div/div/div[1]/span' # Ingredientes
        self.gestALPEDNCEV1XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[1]' # Ingrediente:
        self.gestALPEDNCEV2XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[2]' # Unidad:
        self.gestALPEDNCEV3XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[3]' # Cantidad:
        self.gestALPEDNCEV4XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[4]' # Precio unitario (€):
        self.gestALPEDNCEV5XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[5]' # IVA
        self.gestALPEDNCEV6XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[6]' # Total:
        self.gestALPEDNCEV7XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[7]'  # Total + IVA
        self.gestALPEDNCEIngInput = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[1]/div/input[1]' # Valor ingrediente
        self.gestALPEDNCEC1XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[2]/table/thead/tr/td[1]' # Ingrediente
        self.gestALPEDNCEC2XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[2]/table/thead/tr/td[2]' # Unidad
        self.gestALPEDNCEC3XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[2]/table/thead/tr/td[3]' # Cantidad
        self.gestALPEDNCEC4XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[2]/table/thead/tr/td[4]' # Precio unitario (€)
        self.gestALPEDNCEC5XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[2]/table/thead/tr/td[5]' # IVA
        self.gestALPEDNCEC6XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[2]/table/thead/tr/td[6]' # Total
        self.gestALPEDNCEC7XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[2]/table/thead/tr/td[7]' # Total + IVA
        self.gestALPEDNCEC8XPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[2]/table/thead/tr/td[8]' # Eliminar
        self.gestALPEDNCEAlmInput = '//*[@id="warehouseSelect"]/select'
        self.gestALPEDNCEAlmValor = '//*[@id="warehouseSelect"]/select/option[10]' # LTL Fleming
        self.gestALPEDNCEIngValor = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[1]/div/ul/li[1]' # ALBAHACA
        self.gestALPEDNCEUnitInput ='//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[2]/div/select'
        self.gestALPEDNCEUnitValor = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[2]/div/select/option[1]' # UD (100 G)
        self.gestALPEDNCECanInput = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[3]/input[1]' # Cantidad
        self.gestALPEDNCEPreUnitInput = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[4]/input' # Precio unitario
        self.gestALPEDNCEPreIVAInput = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[5]/div/select/option[7]' # IVA 21%
        self.gestALPEDNCEAddXPath = '//*[@id="externalpurchase-accordion"]/div/div/div[2]/div/div[1]/form/div[8]/button' # Añadir
        self.gestALPEDNCETot1XPath = '//*[@id="externalpurchase-space"]/h4/span[1]'
        self.gestALPEDNCETot2XPath = '//*[@id="externalpurchase-space"]/h4/span[2]'
        self.gestALPEDNCETot1TXT = ':'
        self.gestALPEDNCETot2TXT = '2.42 €'
        self.gestALPEDNCEGCEtitXPath = '//*[@id="confirmationModal"]/div/div[1]/span' # GENERAR COMPRA EXTERNA
        self.gestALPEDNCEGCEtitTXT = 'GENERAR COMPRA EXTERNA'
        self.gestALPEDNCEGCEtit2XPath = '//*[@id="confirmationModal"]/div/form/div[1]/p[1]' # ¿Está seguro de generar la compra externa en esta fecha?
        self.gestALPEDNCEGCEtit2TXT = '¿Está seguro de generar la compra externa en esta fecha?'
        self.gestALPEDNCEGCEKOXPath = '//*[@id="confirmationModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestALPEDNCEGCEOKXPath = '//*[@id="confirmationModal"]/div/form/div[3]/button[2]' # Aceptar
        self.gestALPEDCE1XPath = '//*[@id="externalpurchase-table"]/table/tbody/tr/td[3]' # Fecha Compra externa 1
        self.gestALPEDNCEDELXPath = '//*[@id="externalpurchase-table"]/table/tbody/tr/td[12]/i' # Eliminar
        self.gestALPEDNCEDELTitXPath = '//*[@id="confirmationCancelModal"]/div/div[1]/span'
        self.gestALPEDNCEDELTitTXT = 'CANCELAR COMPRA EXTERNA'
        self.gestALPEDNCEDELTit2XPath = '//*[@id="confirmationCancelModal"]/div/form/div[1]/p'
        self.gestALPEDNCEDELTit2TXT = '¿Estás seguro que desea cancelar esta compra externa?'
        self.gestALPEDNCEDELKOXPath = '//*[@id="confirmationCancelModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestALPEDNCEDELOKXPath = '//*[@id="confirmationCancelModal"]/div/form/div[3]/button[2]' # Aceptar

    # RECETA, RECETAS A LA CARTA
        self.gestALPEDRCTitTXT = 'RELACIÓN DE PRODUCTOS DE CARTA Y ESCANDALLOS'
        self.gestALPEDRCBusXPath = '//*[@id="recipe-action"]/div[1]/span'
        self.gestALPEDRCBusInput = '//*[@id="recipe-action"]/div[1]/div/input' # Buscar: ALHAMBRA
        self.gestALPEDRCCol1XPath = '//*[@id="recipe-table"]/table/thead/tr[1]/th[1]/div/span' # Producto de carta
        self.gestALPEDRCCol2XPath = '//*[@id="recipe-table"]/table/thead/tr[1]/th[2]/div/span' # Escandallo
        self.gestALPEDRCCol3XPath = '//*[@id="recipe-table"]/table/thead/tr[1]/th[3]/div/span' # Combo
        self.gestALPEDRCCol4XPath = '//*[@id="recipe-table"]/table/thead/tr[1]/th[4]/div/span' # Precio de venta medio
        self.gestALPEDRCCol5XPath = '//*[@id="recipe-table"]/table/thead/tr[1]/th[5]/div/span' # Coste total de la receta
        self.gestALPEDRCCol6XPath = '//*[@id="recipe-table"]/table/thead/tr[1]/th[6]/div/span' # Beneficio(€)
        self.gestALPEDRCCol7XPath = '//*[@id="recipe-table"]/table/thead/tr[1]/th[7]/div/span' # Margen
        self.gestALPEDRCCol8XPath = '//*[@id="recipe-table"]/table/thead/tr[1]/th[8]/div/span' # Acciones
        self.gestALPEDRCPCarTXT = 'Producto de carta'
        self.gestALPEDRCEscTXT = 'Escandallo'
        self.gestALPEDRCComTXT = 'Combo'
        self.gestALPEDRCPVMTXT = 'Precio de venta medio'
        self.gestALPEDRCCTRTXT = 'Coste total de la receta'
        self.gestALPEDRCBenTXT = 'Beneficio (€)'
        self.gestALPEDRCMarTXT = 'Margen'

        # Avanzar/retroceder página recetas de carta
        self.gestAlmRC1erElXPath = '//*[@id="recipe-table"]/table/tbody/tr[1]/td[1]/span' # Primer elemento de la tabla
        self.gestAlmRCAvPXPath = '//*[@id="recipe-table"]/div/div/div/ul/li[13]/a'
        #self.gestAlmAvPTXT = '>>'
        self.gestAlmRCRePXPath = '//*[@id="recipe-table"]/div/div/div/ul/li[1]/a'
        #self.gestAlmRePTXT = '<<'
        self.gestAlmRCPg5XPath = '//*[@id="recipe-table"]/div/div/div/ul/li[4]/a/span'
        self.gestAlmRCPg5TXT = '5'
        self.gestAlmRCPg1XPath = '//*[@id="recipe-table"]/div/div/div/ul/li[2]/a/span'
        self.gestAlmRCPg1TXT = '1'
        self.gestAlmMosXRCXPath = '//*[@id="recipe-table"]/div/div/div/ul/li[6]/a'

        # Resultado busqueda y después de ordenar
        self.gestALPEDRCResCol1XPath = '//*[@id="recipe-table"]/table/tbody/tr[1]/td[1]'
        self.gestALPEDRCResCol2XPath = '//*[@id="recipe-table"]/table/tbody/tr[1]/td[2]'
        self.gestALPEDRCResCol3XPath ='//*[@id="recipe-table"]/table/tbody/tr[1]/td[4]'
        self.gestALPEDRCResCol3TXT = '3.63636 €'
        self.gestALPEDRCResCol4XPath = '//*[@id="recipe-table"]/table/tbody/tr[1]/td[5]'
        self.gestALPEDRCResCol4TXT = '1.12250 €'
        self.gestALPEDRCResCol5XPath = '//*[@id="recipe-table"]/table/tbody/tr[1]/td[6]'
        self.gestALPEDRCResCol5TXT = '2.51386 €'
        self.gestALPEDRCResCol6XPath = '//*[@id="recipe-table"]/table/tbody/tr[1]/td[7]'
        self.gestALPEDRCResCol6TXT = '69.13 %'
        self.gestALPEDRCResColX1XPath = '//*[@id="recipe-table"]/table/tbody/tr[6]/td[1]'
        self.gestALPEDRCResColX1TXT = 'P Alhambra Reservar' # IGUAL gestALPEDRCResColX2TXT
        self.gestALPEDRCResColX2XPath = '//*[@id="recipe-table"]/table/tbody/tr[6]/td[2]'
        self.gestALPEDRCResColX3XPath ='//*[@id="recipe-table"]/table/tbody/tr[6]/td[4]'
        self.gestALPEDRCResColX3TXT = '0.00000 €' # IGUAL gestALPEDRCResColX4TXT, gestALPEDRCResColX5TXT, gestALPEDRCResColO6TXT
        self.gestALPEDRCResColX4XPath = '//*[@id="recipe-table"]/table/tbody/tr[6]/td[5]'
        self.gestALPEDRCResColX5XPath = '//*[@id="recipe-table"]/table/tbody/tr[6]/td[6]'
        self.gestALPEDRCResColX6XPath = '//*[@id="recipe-table"]/table/tbody/tr[6]/td[7]'
        self.gestALPEDRCResColX6TXT = '0.00 %'  # IGUAL estALPEDRCResColO4TXT,gestALPEDRCResColO5TXT,
        self.gestALPEDRCOrdXPath = '//*[@id="recipe-table"]/table/thead/tr[1]/th[7]/div/span' # Ordenar por margen
        self.gestALPEDRCOrdColO1XPath = '//*[@id="recipe-table"]/table/tbody/tr[1]/td[7]'
        self.gestALPEDRCOrdColO1TXT = '83.51 %' # IGUAL gestALPEDRCResColO2TXT
        self.gestALPEDRCOrdColO2XPath = '//*[@id="recipe-table"]/table/tbody/tr[2]/td[7]'
        self.gestALPEDRCOrdColO3XPath ='//*[@id="recipe-table"]/table/tbody/tr[3]/td[7]'
        self.gestALPEDRCOrdColO3TXT = '69.13 %'
        self.gestALPEDRCOrdColO4XPath = '//*[@id="recipe-table"]/table/tbody/tr[4]/td[7]'
        self.gestALPEDRCOrdColO5XPath = '//*[@id="recipe-table"]/table/tbody/tr[5]/td[7]'
        self.gestALPEDRCOrdColO6XPath = '//*[@id="recipe-table"]/table/tbody/tr[6]/td[7]'
        # Editar
        self.gestALPEDRCEdP1XPath = '//*[@id="recipe-table"]/table/tbody/tr[1]/td[8]/i' # Editar primer producto
        self.gestALPEDRCEdP1TitXPath = '//*[@id="editRecipeModal"]/div/div[1]/span' # EDITAR RECETA
        self.gestALPEDRCEdP1TitTXT = 'EDITAR RECETA'
        self.gestALPEDRCEdP1NomXPath = '//*[@id="editRecipeModal"]/div/form/div[1]/div[1]/label/div' # Nombre*
        self.gestALPEDRCEdP1EscXPath = '//*[@id="editRecipeModal"]/div/form/div[1]/div[2]/label/label' # Escandallo
        self.gestALPEDRCEdP1NomInput = '//*[@id="recipe-table"]/table/tbody/tr[1]/td[1]/span' # Alhambra Especial 33cl DELIVERY
        self.gestALPEDRCEdP1NomValor = 'Alhambra Especial 33cl DELIVERY'
        self.gestALPEDRCEdP1EscInput = '//*[@id="recipeSelect"]/select'
        self.gestALPEDRCEdP1EscValor = '//*[@id="recipeSelect"]/select/option[42]' # 1/2 TOSTADA MIXTA
        self.gestALPEDRCEdP1KOXPath = '//*[@id="editRecipeModal"]/div/form/div[3]/button[1]' # Cancelar
        self.gestALPEDRCEdP1OKXPath = '//*[@id="editRecipeModal"]/div/form/div[3]/button[2]' # Aceptar

















