# SAGRILAFT (Docassemble)

Este repositorio contiene entrevistas de Docassemble (archivos YAML) y un módulo Python auxiliar para envío de archivos a un webhook.

## Prerrequisitos

- Tener **Docassemble** instalado y funcionando (recomendado: instalación vía Docker siguiendo la documentación oficial de Docassemble).
- Acceso al panel web de Docassemble (para usar el Playground o administrar paquetes).

## Estructura del repositorio

- `form/sagrf2.yaml` y `form/testSagrilaft.yaml`: entrevistas de ejemplo, la entrevista test ya funciona para la recoleccion de archivos
- `form/modules/test.py`: funciones auxiliares (ej. `enviar_archivos(...)`) que hacen POST al webhook.

## Uso desde Docassemble (rápido: Playground)

Esta opción no requiere “empaquetar” el proyecto; es la forma más rápida para probar.

Para usarlas, debes **copiar el contenido** al Playground o **instalarlas como paquete** (siguiente sección).

1. En Docassemble, entra a `Playground`.
2. En `Playground`:
   - Abre `Interview files` y crea/pega el contenido de `sagrf2.yaml` y/o `testSagrilaft.yaml`.
   - Abre `Modules` y crea/pega el contenido de `test.py` (nombre recomendado: `test.py`).
3. Ejecuta la entrevista desde el botón `Run`/`Play` del editor de Docassemble.

Notas:

- En los YAML se usa `modules: - .test`. Esto asume que el módulo `test.py` está disponible en el mismo “contexto” (paquete/playground) que la entrevista.
- Si Docassemble no encuentra el módulo, cambia la línea a `modules: - test` (import absoluto) y vuelve a ejecutar.

## Uso desde Docassemble (recomendado: como paquete)

Para despliegues o colaboración, lo habitual es convertir esto en un **paquete de Docassemble** e instalarlo en Docassemble.

En alto nivel, la estructura esperada por Docassemble es:

- `docassemble/<nombre_paquete>/data/questions/<entrevista>.yml`
- `docassemble/<nombre_paquete>/<modulo>.py`

Flujo sugerido:

1. Crear un paquete Docassemble (p. ej. `docassemble-sagrilaft`).
2. Mover/copiar:
   - `form/*.yaml` a `docassemble/<paquete>/data/questions/`
   - `form/modules/test.py` a `docassemble/<paquete>/test.py`
3. Instalar el paquete en Docassemble (por UI en `Package Management` o por `pip` dentro del contenedor).
4. Ejecutar la entrevista por nombre de paquete (desde la UI o URL de entrevista).

## Configuración del webhook

- El webhook está hardcodeado en `form/modules/test.py`. Para entornos reales conviene:
  - moverlo a una variable/configuración (por ejemplo, variable de entorno),
  - y evitar commitear URLs con firmas/tokens.
