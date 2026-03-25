import pandas as pd

# Datos de la plantilla
data = {
    "ID": ["HP1","HP2","ALT1","ALT2","NEG1","NEG2","EXT1","EXT2"],
    "Tipo de Flujo": ["Happy Path","Happy Path","Alternativo","Alternativo","Negativo","Negativo","Funcionalidad extra","Funcionalidad extra"],
    "Caso de Prueba": ["Crear pedido básico","Procesar pago","Dividir cuenta","Cambiar mesa","Añadir producto no disponible","Pagar con método no permitido","Ver reporte de ventas","Configuración de menú"],
    "Descripción": [
        "Registrar un pedido completo correctamente",
        "Realizar pago completo",
        "Cliente paga por partes",
        "Mover un pedido a otra mesa",
        "Probar error al agregar producto fuera de stock",
        "Intentar pagar con método inválido",
        "Comprobar reporte de ventas por día",
        "Modificar precio de un producto"
    ],
    "Pasos": [
        "1. Abrir app 2. Seleccionar mesa 1 3. Añadir productos A, B 4. Confirmar pedido",
        "1. Seleccionar pedido 2. Elegir método de pago 3. Confirmar",
        "1. Seleccionar pedido 2. Elegir “dividir cuenta” 3. Confirmar pagos parciales",
        "1. Seleccionar pedido 2. Elegir “cambiar mesa” 3. Seleccionar nueva mesa",
        "1. Abrir pedido 2. Intentar añadir producto X (agotado)",
        "1. Seleccionar pedido 2. Elegir método de pago no permitido 3. Confirmar",
        "1. Abrir módulo de reportes 2. Seleccionar fecha 3. Generar reporte",
        "1. Abrir configuración 2. Seleccionar producto 3. Cambiar precio 4. Guardar"
    ],
    "Datos de Prueba": [
        "Mesa 1, Producto A, B",
        "Tarjeta, total $45",
        "Dos tarjetas $20 + $25",
        "Mesa 1 → Mesa 2",
        "Producto X",
        "Método no aceptado",
        "Fecha actual",
        "Producto B → $12"
    ],
    "Resultado Esperado": [
        "Pedido registrado correctamente",
        "Pago registrado y ticket generado",
        "Cada pago registrado correctamente",
        "Pedido movido y estado actualizado",
        "Mensaje de error mostrado y producto no agregado",
        "Mensaje de error mostrado",
        "Reporte generado correctamente con datos correctos",
        "Precio actualizado correctamente"
    ],
    "Resultado Obtenido": [""]*8,
    "Estado": ["Pendiente/OK/Fail"]*8,
    "Observaciones": [""]*8
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar como Excel
df.to_excel("Plantilla_Pruebas_Restaurante.xlsx", index=False)

print("Archivo 'Plantilla_Pruebas_Restaurante.xlsx' generado correctamente en la carpeta actual.")