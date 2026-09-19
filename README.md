# Inteligencia-Artificial-2026-2
PRACTICA 1
## Árbol de decisión - Wine Dataset
Esta práctica aplica un modelo de árbol de decisión usando "scikit-learn" para clasificar 3 tipos
de vino cultivados en la región de Piamonte, Italia a partir de sus propiedades quimicas.
## RESULTADOS
Demostro un rendimiento muy bueno. Al permitir una profundidad de al menos tres niveles, se alcanzó
una precision del 94.44% en el conjunto de prueba. Esto demuestra que el arbol es capz de generalizar
correctamente sobre datos no vistos sin ajustarse de más.
# EVALUACIÓN DEL DATASET
**¿El dataset cumple con los requerimientos?**
Sí
### JUSTIFICACION
1. Atributos continuos y cuantitativos
  Las 13 variables representan variables quimicas, lo que facilita encontrar umbrales numéricos de corte en cada nodo
2. Clases diferenciadas
   Las clases representan perfiles quimicos por el proceso de cultivo y variedad de uva, lo que permite formar las reglas "si-entonces" y de baja profundidad.
## Características Fundamentales y Propuestas de Mejora
**Características clave identificadas por el árbol:**
  - `color_intensity` (Intensidad de color): Es el divisor principal del nodo raíz; separa eficazmente vinos con mayor o menor intensidad cromática.
  - `flavanoids` (Flavonoides): Ayuda a identificar vinos con baja concentración de compuestos fenólicos (típico de la clase 2).
