# Problema 1: Manipulación Básica de Arrays

### Descripción:
Crea un programa en Python que permita:

1. Leer un array de números enteros desde la entrada del usuario.
2. Encontrar y mostrar:
   - El número más grande y su posición en el array.
   - El número más pequeño y su posición en el array.
3. Invertir el array y mostrar el resultado.

### Restricciones:
- No se puede usar la función `max()` ni `min()`.
- La entrada del array debe ser validada (solo números enteros).

### Ejemplo de Entrada:
```
Ingrese los números del array separados por espacio: 10 20 -5 7 3
```

### Ejemplo de Salida:
```
Número más grande: 20 en la posición 1
Número más pequeño: -5 en la posición 2
Array invertido: [3, 7, -5, 20, 10]
```

### Pistas:
- Utiliza un bucle para recorrer el array y encontrar el mayor y menor valor.
- Recuerda que los índices en Python empiezan desde 0.
- Usa slicing o un bucle para invertir el array.

---

# Problema 2: Operaciones Avanzadas con Arrays

### Descripción:
Escribe un programa en Python que realice las siguientes operaciones con arrays:

1. Lea dos arrays de números enteros del usuario.
2. Determine si ambos arrays tienen los mismos elementos (sin importar el orden).
3. Calcule la intersección y la unión de ambos arrays y muéstralos como listas únicas.

### Restricciones:
- No puedes usar las funciones `set()` ni bibliotecas adicionales como NumPy.
- La entrada debe ser validada (solo números enteros).

### Ejemplo de Entrada:
```
Ingrese los números del primer array separados por espacio: 1 2 3 4
Ingrese los números del segundo array separados por espacio: 4 3 2 1 5
```

### Ejemplo de Salida:
```
¿Los arrays tienen los mismos elementos? No
Intersección: [1, 2, 3, 4]
Unión: [1, 2, 3, 4, 5]
```

### Pistas:
- Para verificar si dos arrays tienen los mismos elementos, ordena ambos y compáralos.
- Usa bucles para calcular la intersección y la unión.
