from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad, pad
import base64
import time
import psutil

# Función para encriptar un mensaje
def encrypt(key, plaintext):
    # Decodifica la clave desde base64
    key_bytes = base64.b64decode(key)
    # Convierte el texto a bytes
    plaintext_bytes = plaintext.encode()
    # Crea un cifrador AES en modo ECB
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    # Rellena el texto plano para que sea múltiplo del tamaño del bloque AES
    padded_plaintext = pad(plaintext_bytes, AES.block_size)
    # Encripta el texto plano
    ciphertext_bytes = cipher.encrypt(padded_plaintext)
    # Convierte el texto cifrado a representación hexadecimal
    ciphertext_hex = ciphertext_bytes.hex()

    return ciphertext_hex

# Función para desencriptar un mensaje
def decrypt(ciphertext_hex, key_base64, mode=AES.MODE_ECB):
    # Decodificar la clave base64
    key = base64.b64decode(key_base64)
    # Convertir el texto cifrado de hexadecimal a bytes
    ciphertext = bytes.fromhex(ciphertext_hex)
    # Inicializar el cifrado AES
    cipher = AES.new(key, mode)
    # Desencriptar el texto cifrado y descomprimir el relleno
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return plaintext.decode('utf-8')

# Función para medir el tiempo de ejecución de una función
def measure_execution_time(func, *args):
    """
    Mide el tiempo de ejecución de una función.
    Parámetros:
    - func: La función cuyo tiempo de ejecución se va a medir.
    - *args: Los argumentos para pasar a la función.
    Retorna:
    - Una tupla que contiene el resultado de la función y el tiempo de ejecución en segundos.
    """
    # Registra el tiempo de inicio
    start_time = time.perf_counter()
    # Ejecuta la función con los argumentos dados
    result = func(*args)
    # Registra el tiempo de finalización
    end_time = time.perf_counter()
    # Calcula la diferencia de tiempo para obtener el tiempo de ejecución
    execution_time = end_time - start_time
    # Retorna una tupla que contiene el resultado de la función y el tiempo de ejecución
    return result, execution_time

# Función para medir el uso de recursos del sistema
def measure_system_resources():
    """
    Mide el uso de recursos del sistema, incluido el uso de CPU y la memoria.
    Retorna:
    - Una tupla que contiene el uso de CPU y el uso de memoria en porcentaje.
    """
    # Obtiene el porcentaje de uso de CPU
    cpu_usage = psutil.cpu_percent()
    # Obtiene el porcentaje de uso de memoria
    memory_usage = psutil.virtual_memory().percent
    # Retorna una tupla que contiene el uso de CPU y el uso de memoria
    return cpu_usage, memory_usage

if __name__ == "__main__":

    while True:
        print("\n--- MENU DE SELECCION ---")
        print("\nSeleccione una opción:")
        print("1. Encriptar mensaje")
        print("2. Desencriptar mensaje")
        print("3. Salir")

        option = input("Opción: ")

        if option == "1":
            plaintext = input("Introduce el texto a encriptar: ")
            key_base64 = input("Introduce la clave en base64: ")
            try:
                ciphertext_hex = encrypt(key_base64, plaintext)
                print("Mensaje encriptado (hex):", ciphertext_hex)

                # Medir el tiempo de ejecución y los recursos del sistema
                _, encryption_time = measure_execution_time(encrypt, key_base64, plaintext)
                encryption_time = round(encryption_time, 5)
                cpu_usage, memory_usage = measure_system_resources()

                # Generar reporte
                print("\n--- Reporte de Benchmarking ---")
                print("Tiempo de Encriptación:", encryption_time, "segundos")
                print("Uso de CPU:", cpu_usage, "%")
                print("Uso de Memoria:", memory_usage, "%")
            except ValueError as e:
                print("Error:", e)

        elif option == "2":
            ciphertext_hex = input("Introduce el mensaje encriptado en formato hexadecimal: ")
            key_base64 = input("Introduce la clave en base64: ")
            try:
                plaintext = decrypt(ciphertext_hex, key_base64)
                print("Mensaje desencriptado:", plaintext)

                # Medir el tiempo de ejecución y los recursos del sistema
                _, decryption_time = measure_execution_time(decrypt, ciphertext_hex, key_base64)
                decryption_time = round(decryption_time, 5)
                cpu_usage, memory_usage = measure_system_resources()

                # Generar reporte
                print("\n--- Reporte de Benchmarking ---")
                print("Tiempo de Desencriptación:", decryption_time, "segundos")
                print("Uso de CPU:", cpu_usage, "%")
                print("Uso de Memoria:", memory_usage, "%")

            except ValueError as e:
                print("Error:", e)
        elif option == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")
