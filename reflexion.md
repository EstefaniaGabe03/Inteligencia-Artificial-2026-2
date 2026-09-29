# Respuestas a Preguntas de Reflexión

## 1. Limitaciones observadas en el enfoque
-  El motor exige combinaciones exactas de síntomas. Si falta uno o cambia de nombre, no se activa la regla.
- Evaluación binaria: Simplificación de valores Verdadero/Falso sin matices.

## 2. Manejo de la incertidumbre en los síntomas
- Uso de **Lógica Difusa (Fuzzy Logic)** para manejar grados de pertenencia (ej. fiebre leve, moderada, alta).
- Incorporación de **Factores de Certeza (CF)** para asignar probabilidades a las reglas y síntomas.

## 3. Implicaciones de la activación simultánea de varias reglas
- Representa escenarios reales de múltiples afecciones a la vez.
- Puede provocar recomendaciones contradictorias o tratamientos incompatibles si no hay un módulo de resolución de conflictos médicos.