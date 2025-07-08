---
trigger: always_on
---

# Estilo de codigo en python

1. Sigue la guía de estilo PEP8 para nombres, indentación y espaciado.
2. Usa nombres descriptivos y en inglés para variables, funciones y clases.
3. Limita la longitud de línea a 120 caracteres.
4. Separa funciones y clases con dos líneas en blanco.
5. Usa docstrings en todas las funciones, métodos y clases, siguiendo el formato estándar.
6. Prefiere f-strings para la interpolación de cadenas.
7. Importa módulos estándar antes que módulos de terceros y luego los locales, separados por líneas en blanco.
8. Evita imports no utilizados y elimina código muerto.
9. No uses variables o argumentos no utilizados; si son necesarios, nómbralos como _.
10. Prefiere las comprensiones de listas y generadores para operaciones simples y legibles.
11. Maneja las excepciones de manera explícita y específica, nunca uses except sin tipo.
12. No uses prints para debug; utiliza el módulo logging.
13. Evita la mutabilidad innecesaria, especialmente en argumentos por defecto.
14. Añade anotaciones de tipo (type hints) en funciones y métodos.
15. Usa espacios alrededor de operadores y después de comas.
16. No uses variables globales salvo que sea estrictamente necesario.
17. Prefiere funciones pequeñas y con una sola responsabilidad.
18. Documenta cualquier comportamiento no trivial o decisión de diseño relevante.
19. Usa comentarios solo para explicar el “por qué”, no el “qué” si el código es claro.
20. Añade y ejecuta pruebas unitarias para toda nueva funcionalidad.