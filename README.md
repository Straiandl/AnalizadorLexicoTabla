# Analizador Léxico para Compilador LR(1)

Se implementa un analizador Lexico agregando que se puedan reconcer los simbolos.

---


### 2. Ejecución en Consola

![docs/ejecucion_consola.png](https://github.com/Straiandl/AnalizadorLexicoTabla/blob/8dff9b7c048b9fd0c2423fb0ff05f538f5b2e76c/Lexico1.png)
*Figura 2: Ejemplo de tokenización de código fuente en la terminal con los IDs numéricos.*

---

## 📊 Tabla de Especificación de Tipos (LR1)

El analizador retorna una tupla `(lexema, tipo_id)` donde `tipo_id` corresponde al entero asignado a cada columna de la gramática $LR(1)$:

| Tipo (ID) | Token / Categoría | Lexemas / Descripción |
| :---: | :--- | :--- |
| **0** | `identificador` | Nombres de variables y funciones (`id`) |
| **1** | `entero` | Constantes numéricas enteras (`70`, `100`) |
| **2** | `real` | Números de punto flotante (`39.5`, `0.5`) |
| **3** | `cadena` | Cadenas entre comillas (`"Hola Mundo"`) |
| **4** | `tipo` | Palabras reservadas `int`, `float`, `void` |
| **5** | `opSuma` | Operadores aditivos `+`, `-` |
| **6** | `opMul` | Operadores multiplicativos `*`, `/` |
| **7** | `opRelac` | Relacionales `<`, `<=`, `>`, `>=` |
| **8** | `opOr` | Operador lógico OR `\|\|` |
| **9** | `opAnd` | Operador lógico AND `&&` |
| **10** | `opNot` | Operador lógico NOT `!` |
| **11** | `opIgualdad` | Igualdad y desigualdad `==`, `!=` |
| **12** | `;` | Punto y coma |
| **13** | `,` | Coma |
| **14** | `(` | Paréntesis izquierdo |
| **15** | `)` | Paréntesis derecho |
| **16** | `{` | Llave izquierda |
| **17** | `}` | Llave derecha |
| **18** | `=` | Operador de asignación |
| **19** | `if` | Palabra reservada `if` |
| **20** | `while` | Palabra reservada `while` |
| **21** | `return` | Palabra reservada `return` |
| **22** | `else` | Palabra reservada `else` |
| **23** | `$` | Símbolo de fin de archivo / cadena |

---

## 🛠️ Estructura de la Máquina de Estados (AFD)

* **Estado 0:** Estado inicial distribuidor. Evalúa el carácter inicial, reconoce símbolos simples inmediatamente o transiciona a estados acumuladores.
* **Estado 1:** Acumula caracteres alfanuméricos para `identificador`. Al finalizar, consulta una tabla de palabras reservadas para asignar el tipo correspondiente (`4`, `19`, `20`, `21`, `22` u `0`).
* **Estado 100 / 2 / 3:** Maneja números. Si encuentra un punto `.`, pasa al Estado 2 (esperando al menos un dígito) y luego al Estado 3 para confirmar un número `real` (tipo `2`).
* **Estado 200:** Acumula caracteres dentro de comillas dobles para formar una `cadena` (tipo `3`).
* **Inspección Adelantada (Lookahead):** Permite diferenciar operadores compuestos de dos caracteres (`==`, `!=`, `<=`, `>=`, `&&`, `||`) de operadores de un solo carácter.

---

## 🚀 Requisitos e Instalación

### Prerrequisitos

* **Python 3.x** instalado.

---

## 💻 Uso

Ejecuta el script directamente desde la terminal:

```bash
python AnalizadorLexico.py
```

### Ejemplo de Código a Tokenizar:

```c
int main() {
    float total = 39.5;
    if (total >= 10 && !false || true) {
        return "Hola";
    }
} $
```

### Ejemplo de Salida:

```text
Lexema: int             | Tipo (ID): 4
Lexema: main            | Tipo (ID): 0
Lexema: (               | Tipo (ID): 14
Lexema: )               | Tipo (ID): 15
Lexema: {               | Tipo (ID): 16
Lexema: float           | Tipo (ID): 4
Lexema: total           | Tipo (ID): 0
Lexema: =               | Tipo (ID): 18
Lexema: 39.5            | Tipo (ID): 2
Lexema: ;               | Tipo (ID): 12
Lexema: if              | Tipo (ID): 19
Lexema: (               | Tipo (ID): 14
Lexema: total           | Tipo (ID): 0
Lexema: >=              | Tipo (ID): 7
Lexema: 10              | Tipo (ID): 1
Lexema: &&              | Tipo (ID): 9
Lexema: !               | Tipo (ID): 10
Lexema: false           | Tipo (ID): 0
Lexema: ||              | Tipo (ID): 8
Lexema: true            | Tipo (ID): 0
Lexema: )               | Tipo (ID): 15
Lexema: {               | Tipo (ID): 16
Lexema: return          | Tipo (ID): 21
Lexema: "Hola"          | Tipo (ID): 3
Lexema: ;               | Tipo (ID): 12
Lexema: }               | Tipo (ID): 17
Lexema: }               | Tipo (ID): 17
Lexema: $               | Tipo (ID): 23
```

---

## 📁 Estructura del Repositorio

```text
.
├── AnalizadorLexico.py   # Código fuente del analizador léxico en Python
├── README.md             # Documentación general del proyecto
└── docs/                 # Recursos gráficos e imágenes
    ├── diagrama_afd.png      # Esquema visual del AFD
    └── ejecucion_consola.png # Captura de prueba de ejecución
```

---

## 🎓 Materia y Profesor
* **Asignatura:** Taller de Compiladores / Traductores de Lenguaje 2
* **Docente:** Ing. Michel Emanuel López Franco
