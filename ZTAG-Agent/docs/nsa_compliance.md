# Mapeo de Cumplimiento NSA Zero Trust

Este proyecto utiliza a **Monday** (IA Granite) para validar los siguientes controles de la NSA:

## Referencias de Documentos (Directorio /data)
- **Conceptos Base:** `1769475823091.pdf` (Primer)
- **Controles Técnicos:** `1769896060719.pdf` (Phase One)

## Actividades Técnicas Cubiertas
- **Actividad 2.4.1 (Validación de Atributos):** Monday detecta el uso de confianza implícita en variables de entrada y exige validación dinámica.
- **Actividad 7.1.2 (Log Parsing):** Los eventos se estructuran para ser ingeridos por herramientas de analítica, eliminando logs planos sin contexto.
- **Micro-segmentación:** Los conectores seguros (`secure_db.py`) aíslan las credenciales de la lógica de ejecución.