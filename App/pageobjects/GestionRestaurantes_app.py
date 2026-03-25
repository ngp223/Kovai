# app/pageobjects_app.py

# Info general de la app
APP_PACKAGE = "com.tu.paquete"           # Reemplaza con el package real
APP_ACTIVITY = "com.tu.paquete.MainActivity"  # Reemplaza con la activity principal

# Pantalla principal Gestión Restaurantes
# Botones / elementos principales
GESTION_RESTAURANTES_BTN = "gestionRestaurantesBtn"  # accessibility_id del botón "Gestión Restaurantes"
TITULO_GESTION_RESTAURANTES = "tituloGestionRestaurantes"  # accessibility_id de título principal

# Opciones del menú lateral (ejemplo)
MENU_TERMINALES = "menuTerminales"      # ID de "Terminales"
MENU_ZONAS = "menuZonasMesas"           # ID de "Zonas y Mesas"
MENU_CARTA = "menuCarta"                # ID de "Carta"
MENU_SUBCATEGORIAS = "menuSubcategorias"  # ID de "Subcategorías"
MENU_PRODUCTOS = "menuProductos"          # ID de "Productos"
MENU_MENUS = "menuMenusDia"               # ID de "Menús del día/grupos"

# Terminales
TERMINAL_1 = "terminal1"                 # ID del primer terminal
TERMINAL_2 = "terminal2"                 # ID del segundo terminal
TERMINAL_MOVIL_1 = "terminalMovil1"      # ID terminal móvil 1
TERMINAL_MOVIL_2 = "terminalMovil2"      # ID terminal móvil 2
TERMINAL_KITCHEN = "terminalKitchenDisplay"  # ID terminal KDS

# Ejemplo de texto o elementos visibles que se usan para validaciones
TEXTO_LISTADO_TERMINALES = "ListadoDeTerminales"   # accessibility_id de un título que confirme pantalla cargada
TEXTO_SELECCION_RESTAURANTE = "SeleccionRestaurante"  # ID de "Por favor seleccione un restaurante"

# Botón de guardar cambios
GUARDAR_CAMBIOS_BTN = "guardarCambiosBtn"
GUARDADO_OK_MSG = "guardadoOkMsg"