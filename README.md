# ZTAG-Agent: Monday AI Audit (Local Granite Edition) 

**ZTAG (Zero Trust Audit & Guard)** es un sistema de orquestación de seguridad diseñado para auditar, detectar y remediar vulnerabilidades críticas en tiempo real, operando bajo los estándares más estrictos de la **NSA (National Security Agency)**.

##  El Cerebro: Monday
El agente **Monday** es una implementación avanzada basada en el modelo **IBM Granite-Code (8b)**. A diferencia de las soluciones en la nube, Monday vive en tu infraestructura local, garantizando la **Soberanía de Datos** y eliminando cualquier riesgo de filtración de código fuente.

##  Capacidades Probadas (Retos Superados)
ZTAG-Agent ha sido validado en escenarios de alta criticidad:
- **Dominio SQL:** Detección de Inyecciones SQL y remediación mediante parametrización dinámica (Actividad 2.4.1 NSA Phase One).
- **Dominio OS:** Identificación de Inyecciones de Comandos (RCE) en funciones de sistema operativo, sustituyendo ejecuciones inseguras por procesos controlados de `subprocess`.
- **Diferenciación de Contexto:** Monday distingue automáticamente entre reglas de bases de datos y de sistema, aplicando parches específicos según el entorno.



##  Estructura de Referencia Zero Trust
El sistema utiliza directamente los activos de conocimiento alojados en `/data`:
- **Guía Maestro:** `1769475823091.pdf` (Zero Trust Primer).
- **Guía Fase Uno:** `1769896060719.pdf` (Zero Trust Phase One Implementation).

##  Funcionamiento 100% Local
Este sistema utiliza **Ollama** para la inferencia, asegurando que el análisis de seguridad sea:
1. **Privado:** El código nunca sale de la red local.
2. **Auditable:** Genera logs estructurados (Activity 7.1.2) para análisis forense.
3. **Autónomo:** Capaz de proponer soluciones sin conexión a internet.

##  Ejecución Rápida
1. **Inicia el modelo:** ```bash
   ollama run granite-code:8b
