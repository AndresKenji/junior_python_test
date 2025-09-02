# Prueba Técnica - Python Junior

## Descripción
Esta prueba técnica está diseñada para evaluar conocimientos básicos de Python, específicamente el manejo de:
- Listas y arrays
- Ciclos (for, while)
- Función `range()`
- Estructuras de control (if/else)
- Funciones y return
- Tipos de datos básicos

## Instrucciones

### Configuración del Entorno
1. Asegúrate de tener Python 3.8+ instalado
2. Activa el entorno virtual (si ya está configurado):
```bash
env\Scripts\activate
```
3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Tu Tarea
Debes implementar las 4 funciones en el archivo `basics.py` y crear los dos endpoint del archivo `api.py`. Cada función tiene:

### Cómo Probar el Código

1. **Ejecutar todos los tests**:
```bash
python -m pytest test_basics.py -v
# api
python -m pytest test_api.py -v
```

2. **Ejecutar tests de una función específica**:
```bash
python -m pytest test_basics.py::TestLimpiarLista -v
```

