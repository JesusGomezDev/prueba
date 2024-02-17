# Algoritmo seleccionado

## AES (Advanced Encryption Standard)

AES (Advanced Encryption Standard) es un algoritmo de encriptación simétrica ampliamente utilizado para proteger datos sensibles. Fue adoptado como estándar por el Instituto Nacional de Estándares y Tecnología (NIST) de Estados Unidos en 2001, tras un proceso de selección competitivo.

### Funcionamiento

El algoritmo AES funciona mediante la aplicación de rondas de sustitución y permutación de datos sobre bloques de texto de 128 bits. Utiliza claves de diferentes longitudes (128, 192 o 256 bits) para encriptar y desencriptar los datos. El proceso básico de encriptación AES se puede describir en los siguientes pasos:

1. **Inicialización**: Expansión de la clave y adición de una clave inicial al bloque de texto.
2. **Rondas de transformación**: Aplicación de múltiples rondas de sustitución y permutación de datos utilizando subclaves generadas a partir de la clave inicial.
3. **Finalización**: Aplicación de las últimas transformaciones para obtener el texto cifrado.

### Razones para escoger AES

- **Seguridad comprobada**: AES ha sido sometido a análisis criptográfico exhaustivo y se ha demostrado su robustez frente a diversos ataques.
- **Eficiencia y rendimiento**: Diseñado para ser eficiente tanto en hardware como en software, lo que facilita su implementación en una amplia gama de plataformas.
- **Flexibilidad de clave y bloque**: Ofrece tres longitudes de clave y opera sobre bloques de texto de 128 bits, adaptándose a diferentes necesidades de seguridad.
- **Estándar reconocido y ampliamente adoptado**: Respaldado por organizaciones como el NIST, lo que garantiza su compatibilidad e interoperabilidad en sistemas y aplicaciones.
