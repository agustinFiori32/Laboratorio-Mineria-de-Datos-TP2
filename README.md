# Proyecto: Clasificación de Clientes con Random Forest

## Configuración del Proyecto

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el Repositorio
```bash
git clone https://github.com/agustinFiori32/Laboratorio-Mineria-de-Datos-TP2.git
cd tu-repositorio
```

---

## URL de la API:
https://nombre-de-tu-api.herokuapp.com

## Ejemplo de POST al Endpoint `/predict`:
- URL: https://nombre-de-tu-api.herokuapp.com/predict
- Método: POST
- Headers: 
  - Content-Type: application/json
- Body (JSON):
  {
    "features": [30, "Male", 40000, 10, 500, 5, 50.0, 1, 200, 10]
  }
