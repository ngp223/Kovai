Feature: [USUGALM] I revise the page

Background: I am logged as an user
    Given I visit the main page in web
    Then I login as an user

@USUGALM_SEE
  Scenario: [USUGALM_SEE] Ver página principal de almacén
    When I click to gestion almacen
    Then I see gestion de almacen

@USUGALM_LGA
  Scenario: [USUGALM_LGA] Menú lateral de gestión de usuarios
    When I click to gestion almacen
    Then I see menu lateral de almacen

@USUGALM_MNG
  Scenario: [USUGALM_MNG] Gestionar el almacén
    When I click to gestion almacen
    Then I manage almacen

@USUGALM_FNP @proveed
  Scenario: [USUGALM_FNP] Validar formulario nuevo proveedor
    When I click to gestion almacen
    Then I validate the form new provider

@USUGALM_NPMF @proveed
  Scenario: [USUGALM_NPMF] Crear nuevo proveedor con campos obligatorios
    When I click to gestion almacen
    Then I fill in the mandatory fields in the form new provider
    And I save the new provider
    And I search and delete the new provider

@USUGALM_NPAF @proveed
  Scenario: [USUGALM_NPAF] Crear nuevo proveedor con todos los campos
    When I click to gestion almacen
    Then I fill in the form new provider
    And I save the new provider
    And I search and delete the new provider

@USUGALM_SEAPRO @proveed
  Scenario: [USUGALM_SEAPRO] Buscar un proveedor
    When I click to gestion almacen
    Then I search a provider

@USUGALM_PROVEXP @export @proveed
  Scenario: [USUGALM_PROVEXP] Exportar un proveedor
    When I click to gestion almacen
    Then I export providers
    And I open providers file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_AVPAG
  Scenario: [USUGALM_AVPAG] Avanzar página de almacén
    When I click to gestion almacen
    Then I advance page almacen

@USUGALM_REPAG
  Scenario: [USUGALM_REPAG] Retroceder página de almacén
    When I click to gestion almacen
    Then I turn back page almacen

@INVsee
  Scenario: [USUGALM_INVO] Veo facturas
    When I click to gestion almacen
    And I click provider´s invoices
    Then I see provider´s invoices


@USUGALM_MPMASCOL @MPP
  Scenario: [USUGALM_MPMASCOL] Veo más columnas de productos
    When I click to gestion almacen
    And I click products
    Then I see mas columnas

@USUGALM_MPSEEPROD @MPP
  Scenario: [USUGALM_MPSEEPROD] Veo productos uso en receta o personal
    When I click to gestion almacen
    And I click products
    Then I see products of materias primas
    And I select uso en receta y/o personal

@USUGALM_MPPEXP @MPP @export
  Scenario: [USUGALM_MPPEXP] Exportar productos de materias primas
    When I click to gestion almacen
    And I click products
    Then I export products
    And I open MP_products file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_MPPADVSEA @MPP
  Scenario: [USUGALM_MPPADVSEA] Buscar un producto en materias primas
    When I click to gestion almacen
    And I click products
    Then I valid form advance search products
    And I do advance search products

@USUGALM_MPCLON @MPP
  Scenario: [USUGALM_MPCLON] Clono un producto en materias primas
    When I click to gestion almacen
    And I click products
    Then I clone product
    And I delete product cloned

@USUGALM_MPPNF @MPP @create
  Scenario: [USUGALM_MPPNF] Valido formulario creación de producto
    When I click to gestion almacen
    And I click products
    And I click to create an item
    Then I valid the form of a new product

@USUGALM_MPPNAF @MPP @create
  Scenario: [USUGALM_MPPNAF] Creo un producto con todos los campos
    When I click to gestion almacen
    And I click products
    And I click to create an item
    Then I create a product with all fields
    And I search and delete a product

@USUGALM_MPPNMF @MPP @create
  Scenario: [USUGALM_MPPNMF] Creo un producto con campos obligatorios
    When I click to gestion almacen
    And I click products
    And I click to create an item
    Then I create a product with mandatory fields
    And I search and delete a product

@USUGALM_MPPAHIS @MPPA
  Scenario: [USUGALM_MPPAHIS] Acción histórico de producto en materias primas
    When I click to gestion almacen
    And I click products
    Then I click to accion historico de precios

@USUGALM_MPPADIS @MPPA
  Scenario: [USUGALM_MPPADIS] Acción de distribuidor de producto en materias primas
    When I click to gestion almacen
    And I click products
    Then I click to accion distribuidor

@USUGALM_MPPAALE @MPPA @create
  Scenario: [USUGALM_MPPAALE] Acción de alérgenos de producto en materias primas
    When I click to gestion almacen
    And I click products
    And I click to create an item
    And I create a product with mandatory fields
    Then I valid form to accion alergenos
    And I fill form to accion alergenos
    And I search and delete a product

@USUGALM_MPPAEDI @MPPA @create
  Scenario: [USUGALM_MPPAEDI] Accion de editar producto en materias primas
    When I click to gestion almacen
    And I click products
    And I click to create an item
    And I create a product with mandatory fields
    Then I click to accion edit product
    And I valid the form of a new product
    And I click to accion edit product
    And I modify the product
    And I search and delete a product

@USUGALM_MPPADES @MPPA @create
  Scenario: [USUGALM_MPPADES] Accion de deshabilitar producto en materias primas
    When I click to gestion almacen
    And I click products
    And I click to create an item
    And I create a product with mandatory fields
    Then I click to accion deshabilitar

  @USUGALM_MPCAT @create
  Scenario: [USUGALM_MPCAT] Manejar catálogos
    When I click to gestion almacen
    And I click catalogs
    And I click to create a catalog
    Then I create a catalog
    And I search a catalog
    And I delete a catalog

@USUGALM_MPCEXP @export
  Scenario: [USUGALM_MPCEXP] Exportar catálogos
    When I click to gestion almacen
    And I click catalogs
    Then I export catalogs
    And I open catalog file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_MPIVALF @MPI @create
  Scenario: [USUGALM_MPIVALF] Valido formulario de ingredientes
    When I click to gestion almacen
    And I click ingredients
    Then I see ingredients
    And I click to create an item
    And I valid ingredients

@USUGALM_MPCIAF @MPI @create
  Scenario: [USUGALM_MPCIAF] Creo ingrediente con todos los campos
    When I click to gestion almacen
    And I click ingredients
    And I click to create an item
    Then I create an ingredient with all fields
    And I search and delete an ingredient

@USUGALM_MPCIMF @MPI @create
  Scenario: [USUGALM_MPCIMF] Creo ingredientes con campos obligatorios
    When I click to gestion almacen
    And I click ingredients
    And I click to create an item
    Then I create an ingredient with mandatory fields
    And I search and delete an ingredient

@USUGALM_MPEIAF @MPI @create
  Scenario: [USUGALM_MPEIAF] Edito ingrediente
    When I click to gestion almacen
    And I click ingredients
    And I click to create an item
    Then I create an ingredient with all fields
    And I modify an ingredient
    And I search and delete an ingredient

@USUGALM_MPIEXP @export @MPI
  Scenario: [USUGALM_MPIEXP] Exportar ingredientes de materias primas
    When I click to gestion almacen
    And I click ingredients
    Then I export ingredients
    And I open ingredients file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_MPIADVSEA @MPI
  Scenario: [USUGALM_MPIADVSEA] Buscar un ingrediente en materias primas
    When I click to gestion almacen
    And I click ingredients
    Then I valid form advance search ingredient
    And I do advance search ingredient

@USUGALM_MPSEECATEG @MPCATEG
  Scenario: [USUGALM_MPSEECATEG] Veo categorías de materias primas
    When I click to gestion almacen
    And I click materias primas categories
    Then I see categories of materias primas

@USUGALM_MPCATEGEXP @export @MPCATEG
  Scenario: [USUGALM_MPCATEGEXP] Exporta categorías
    When I click to gestion almacen
    And I click materias primas categories
    Then I export categories
    And I open categories file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_MPCATEGADVSEA @MPCATEG
  Scenario: [USUGALM_MPCATEGADVSEA] Buscar una categoría en materias primas
    When I click to gestion almacen
    And I click materias primas categories
    Then I valid form advance search categories
    And I do advance search categories

@USUGALM_MPCATEGVALF @MPCATEG @create
  Scenario: [USUGALM_MPCATEGVALF] Valido formulario de nueva categoría
    When I click to gestion almacen
    And I click materias primas categories
    And I click to create a category
    Then I valid form new category

@USUGALM_MPCATEGNAF @MPCATEG @create
  Scenario: [USUGALM_MPCATEGNAF] Creo una categoría con todos los campos
    When I click to gestion almacen
    And I click materias primas categories
    And I click to create a category
    Then I create a category with all fields
    And I search and delete a category

@USUGALM_MPCATEGNAF @MPCATEG @create
  Scenario: [USUGALM_MPCATEGNAF] Creo una categoría con todos los campos
    When I click to gestion almacen
    And I click materias primas categories
    And I click to create a category
    Then I create a category with mandatory fields
    And I search and delete a category

@USUGALM_MPCATEGEDI @MPCATEG @create
  Scenario: [USUGALM_MPCATEGEDI] Acción de editar categoría
  When I click to gestion almacen
    And I click materias primas categories
    And I click to create a category
    And I create a category with all fields
    And I search a category
    Then I click to action edit category
    And I valid form edit category
    And I modify the category
    And I click materias primas categories
    And I search and delete a category

@USUGALM_MPSEEUNIT @MPU
  Scenario: [USUGALM_MPSEEUNIT] Veo unidades de materias primas
    When I click to gestion almacen
    And I click materias primas units
    Then I see units of materias primas

@USUGALM_AVPAG @MPU
  Scenario: [USUGALM_AVPAG] Avanzar página de unidades
    When I click to gestion almacen
    And I click materias primas units
    Then I advance page units

@USUGALM_REPAG @MPU
  Scenario: [USUGALM_REPAG] Retroceder página de unidades
    When I click to gestion almacen
    And I click materias primas units
    Then I turn back page units

@USUGALM_MPUEXT @export @MPU
  Scenario: [USUGALM_MPUEXT] Exportar unidades
    When I click to gestion almacen
    And I click materias primas units
    Then I export units
    And I open units file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_MPUNITVALF @MPU @create
  Scenario: [USUGALM_MPUNITVALF] Valido formulario de nueva unidad
    When I click to gestion almacen
    And I click materias primas units
    And I click to create an unit
    Then I valid form new unit

@USUGALM_MPUNITNAF @MPU @create
  Scenario: [USUGALM_MPUNITNAF] Creo una unidad con todos los campos
    When I click to gestion almacen
    And I click materias primas units
    And I click to create an unit
    Then I create an unit with all fields
    And I search and delete an unit in buy
    And I search and delete an unit in storage
    And I search and delete an unit in recipe

@USUGALM_MPUNITNMF @MPU @create
  Scenario: [USUGALM_MPUNITNMF] Creo una unidad con los campos obligatorios
    When I click to gestion almacen
    And I click materias primas units
    And I click to create an unit
    Then I create an unit with mandatory fields
  ## HAY UN BUG, NO CREA UNIDAD SOLO CON EL CAMPO OBLIGATORIO NOMBRE

@USUGALM_MPUNITEDIT @MPU @create
  Scenario: [USUGALM_MPUNITEDIT] Edito una unidad
    When I click to gestion almacen
    And I click materias primas units
    And I click to create an unit
    And I create an unit with all fields
    Then I modify an unit
    And I click materias primas units
    And I search and delete an unit in buy
    And I search and delete an unit in storage
    And I search and delete an unit in recipe

@USUGALM_MERSEESTO @MERA
 Scenario: [USUGALM_MERSEESTO] Veo almacenes de mercancía
    When I click to gestion almacen
    Then I click the store
    And I see store
    And I see the email
    And I see locations
    And I see location's preferences

@USUGALM_MERSELSTO @MERA
 Scenario: [USUGALM_MERSELSTO] Veo almacén de mercancía seleccionado
    When I click to gestion almacen
    And I click the store
    Then I see selected store

@USUGALM_MERINVNMF @MERInv @MERA @create
  Scenario: [USUGALM_MERINVNMF] Creo un inventario
    When I click to gestion almacen
    And I click the inventory
    And I click a new inventory
    Then I create an inventory
    And I see the inventary created
    And I edit an inventary
    And I search and delete an inventory

@USUGALM_MERSEEINV @MERInv @MERA
 Scenario: [USUGALM_MERSEEINV] Veo inventario
    When I click to gestion almacen
    Then I click the inventory
    And I see the inventory

@USUGALM_MERINVEXP @export @MERPInv
  Scenario: [USUGALM_MERINVEXP] Exportar inventarios
    When I click to gestion almacen
    And I click the inventory
    Then I export inventories
    And I open the inventory file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_MERINVADVSEA @MERInv
  Scenario: [USUGALM_MERINVADVSEA] Búsqueda avanzada de un inventario
    When I click to gestion almacen
    And I click the inventory
    Then I valid inventory form advance search
    # And I do advance search inventory(Han desaparecido los elementos, 03/04/2025)

@USUGALM_MERINVDESPL @MERInv
  Scenario: [USUGALM_MERINVDESPL] Descargar plantilla inventario
    When I click to gestion almacen
    And I click the inventory
    Then I download the template inventory

@USUGALM_MERTSSEE @MERTS
  Scenario: [USUGALM_MERTSSEE] Veo transpasos y salidas
    When I click to gestion almacen
    And I click transfers and departures
    And I see transfers and departures

@USUGALM_MERTSMGN @MERTS @create
  Scenario: [USUGALM_MERTSMGN] Manejar transpasos y salidas
    When I click to gestion almacen
    And I click transfers and departures
    Then I click a new movement
    And I create a new movement: merma
    And I see and cancel a movement
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_MERTSEXP @MERTS @export
  Scenario: [USUGALM_MERTSEXP] Exportar transpasos y salidas
    When I click to gestion almacen
    And I click transfers and departures
    Then I export transfers and departures
    And I open transfers and departures file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_MERTSSEAAVD @MERTS
  Scenario: [USUGALM_MERTSSEAAVD] Búsqueda avanzada de transpasos y salidas
    When I click to gestion almacen
    And I click transfers and departures
    Then I do advance search transfers and departures

@USUGALM_MERDESSEE
 Scenario: [USUGALM_MERDESSEE] Veo descuadres
    When I click to gestion almacen
    And I click imbalances
    Then I see imbalances

@USUGALM_MEREXP @export
  Scenario: [USUGALM_MEREXP] Exportar descuadres
    When I click to gestion almacen
    And I click imbalances
    Then I export imbalances
    And I open imbalances file
# A veces falla el borrado por no cuadrar el minuto

@USUGALM_MERDESSEAAVD
  Scenario: [USUGALM_MERDESSEAAVD] Búsqueda avanzada de descuadres
    When I click to gestion almacen
    And I click imbalances
    Then I do advance search imbalances

@USUGALM_ORDSEE @ORD
  Scenario: [USUGALM_ORDSEE] Veo pedidos
    When I click to gestion almacen
    And I click orders
    Then I see orders
  # Los pedidos desaparecen cada X tiempo. No tiene sentido comprobar algunos valores

@USUGALM_NOMF @ORD @create # mirar si se puede confirmar pedido y luego borrarlo
  Scenario: [USUGALM_NOMF] Crear nuevo pedido
    When I click to gestion almacen
    And I click orders
    Then I fill fields in the form new order
    #And I search and delete the new order, no está hecho xq los pedidos no se pueden borrar

@USUGALM_ORDEXP @export @ORD
  Scenario: [USUGALM_ORDEXP] Acciones: Exportar pedidos
    When I click to gestion almacen
    And I click orders
    Then I export orders
    And I open orders file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_MPOADVSEA @ORD
  Scenario: [USUGALM_MPOADVSEA] Buscar avanzada pedidos
    When I click to gestion almacen
    And I click orders
    Then I valid form advance search orders
    And I do advance search orders

@USUGALM_MPOFIL @ORD
  Scenario: [USUGALM_MPOFIL] Filtrar pedidos
    #When I click to gestion almacen
    #And I click orders
    #Then I do filters orders
  # Los pedidos desaparecen cada X tiempo. No tiene sentido comprobar algunos valores

@USUGALM_MPOSEE @ORD
  Scenario: [USUGALM_MPOSEE] Acciones: pedido
    When I click to gestion almacen
    And I click orders
    Then I see an order

@USUGALM_ORDSEABRA @ORD
  Scenario: [USUGALM_ORDSEABRA] Busco pedido por su marca
    #When I click to gestion almacen
    #And I click orders
    #Then I see orders by brand
    # Los pedidos desaparecen cada X tiempo. No tiene sentido comprobar algunos valores

@USUGALM_DNISEE @DNI
  Scenario: [USUGALM_DNISEE] Veo albaranes de entrada
    When I click to gestion almacen
    And I click delivery notes(in)
    Then I see delivery notes(in)

@USUGALM_DNINAF @DNI @create
  Scenario: [USUGALM_DNINAF] Crear nuevo albarán
    When I click to gestion almacen
    And I click delivery notes(in)
    Then I fill fields in the form new delivery notes
    And I search and delete the new delivery notes

@USUGALM_DNIEXP @export @DNI
  Scenario: [USUGALM_DNIEXP] Acciones: Exportar pedidos
    When I click to gestion almacen
    And I click delivery notes(in)
    Then I export delivery notes(in)
    And I open delivery notes(in) file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_DNIADVSEA @DNI
  Scenario: [USUGALM_DNIADVSEA] Buscar avanzada albaranes de entrada
    When I click to gestion almacen
    And I click delivery notes(in)
    Then I valid form advance search delivery notes(in)
    And I do advance search delivery notes(in)

@USUGALM_ORDCSEE @ORDC
  Scenario: [USUGALM_ORDCSEE] Veo pedido clientes
    When I click to gestion almacen
    And I click client order
    Then I see client order

@USUGALM_ORDCEXP @export @ORDC
  Scenario: [USUGALM_ORDCEXP] Acciones: Exportar pedido clientes
    #When I click to gestion almacen
    #And I click client order
    #Then I export client order
    #And I open client order file NO HAY PEDIDOS DE CLIENTES

@USUGALM_MPOADVSEA @ORDC
  Scenario: [USUGALM_MPOADVSEA] Buscar avanzada pedido clientes
    #When I click to gestion almacen
    #And I click client order
    # Then I valid form advance search client order
    # And I do advance search client order  NO HAY PEDIDOS DE CLIENTES

@USUGALM_MPOFIL @ORDC
  Scenario: [USUGALM_MPOFIL] Filtrar pedido clientes
    #When I click to gestion almacen
    #And I click client order
    # Then I do filters client order NO HAY PEDIDOS DE CLIENTES

@USUGALM_DNOSEE @DNO
  Scenario: [USUGALM_DNOSEE] Veo albaranes de salida
    When I click to gestion almacen
    And I click delivery notes(out)
    Then I see delivery notes(out)

@USUGALM_DNONAF @DNO @create
  Scenario: [USUGALM_DNONAF] Crear nuevo albarán de salida
    When I click to gestion almacen
    And I click delivery notes(out)
    Then I fill fields in the form new delivery notes
    And I search and delete the new delivery notes

@USUGALM_DNOEXP @export @DNO
    Scenario: [USUGALM_DNOEXP] Exporto albarán de salida
    When I click to gestion almacen
    And I click delivery notes(out)
    Then I fill fields in the form new delivery notes
    And I export delivery notes(out)
    And I open delivery notes(out) file
    And I search and delete the new delivery notes
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_CESEE @CE
  Scenario: [USUGALM_CESEE] Veo compras externas
    When I click to gestion almacen
    And I click external purchases
    Then I see external purchases

@USUGALM_NCE @CE @create
  Scenario: [USUGALM_NCE] Crear nueva compra externa
    When I click to gestion almacen
    And I click external purchases
    Then I fill fields in the form new external purchases
    Then I search and delete the new external purchases

@USUGALM_CEEXP @export @CE
    Scenario: [USUGALM_CEEXP] Exporto compra externa
    When I click to gestion almacen
    And I click external purchases
    Then I fill fields in the form new external purchases
    And I export external purchases
    And I open external purchases file
    And I search and delete the new external purchases
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_RCSEE @RC
  Scenario: [USUGALM_RCSEE] Veo recetas de carta
    When I click to gestion almacen
    And I click menu recipes
    Then I see menu recipes

@RCadvancePage
  Scenario: [USUGALM_RCAVPAG] Avanzar página de recetas de carta
    When I click to gestion almacen
    And I click menu recipes
    Then I advance page menu recipes

@USUGALM_RCREPAG
  Scenario: [USUGALM_RCREPAG] Retroceder página de recetas de carta
    When I click to gestion almacen
    And I click menu recipes
    Then I turn back page menu recipes

@USUGALM_RCEXP @export @RC
  Scenario: [USUGALM_RCEXP] Exportar recetas de carta
    When I click to gestion almacen
    And I click menu recipes
    Then I export menu recipes
    And I open menu recipes file
  # A veces falla el borrado por no cuadrar el minuto

@USUGALM_RCSEAPRO @RC
  Scenario: [USUGALM_RCSEAPRO] Buscar un producto de recetas de carta
    When I click to gestion almacen
    And I click menu recipes
    Then I search a product
    And I edit a product's recipe







