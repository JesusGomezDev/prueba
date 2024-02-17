# Reporte de Benchmarking de Encriptado y Desencriptado

A continuación se presentan los resultados del benchmarking realizados durante el proceso de encriptado y desencriptado de mensajes utilizando AES.

## Encriptado de Mensaje

- Mensaje Original: "hola mundo"
- Clave en Base64: a1a2a3a4a5a6a7a8a9a0a1==
- Mensaje Encriptado (hex): 4dffbacc357a94120419aa6fd32488d0

### Reporte de Benchmarking

- Tiempo de Encriptación: 0.00014 segundos
- Uso de CPU: 15.3 %
- Uso de Memoria: 80.8 %

## Desencriptado de Mensaje

- Mensaje Encriptado (hex): 4dffbacc357a94120419aa6fd32488d0
- Clave en Base64: a1a2a3a4a5a6a7a8a9a0a1==
- Mensaje Desencriptado: "hola mundo"

### Reporte de Benchmarking

- Tiempo de Desencriptación: 0.0001 segundos
- Uso de CPU: 13.5 %
- Uso de Memoria: 80.3 %
