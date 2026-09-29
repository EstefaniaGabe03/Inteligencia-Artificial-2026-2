# Sistema Experto de Diagnóstico Médico

Este proyecto implementa un sistema experto basado en reglas utilizando encadenamiento hacia adelante (Forward Chaining) con la librería `experta` en Python.

# Objetivos
• Comprender el funcionamiento de un sistema experto basado en reglas.
• Implementar un motor de inferencia hacia adelante (forward chaining).
• Construir una base de conocimiento para diagnóstico médico simple.
• Analizar el comportamiento del sistema ante distintos conjuntos de síntomas de entrada.

# Introducción
Un sistema experto es un programa que imita el proceso de razonamiento de un experto humano dentro
de un dominio específico. Está compuesto por tres elementos:
1. Base de conocimiento: un conjunto de reglas de la forma SI (condiciones) ENTONCES
(conclusión).
2. Motor de inferencia: el mecanismo que compara los hechos conocidos contra las reglas y decide
cuáles se activan.
3. Memoria de trabajo: el conjunto de hechos conocidos en un momento dado