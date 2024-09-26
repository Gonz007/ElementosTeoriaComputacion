import os

# Configurar el punto de acceso Wi-Fi
def crear_punto_acceso(nombre_red, contrasena):
    os.system(f'netsh wlan set hostednetwork mode=allow ssid={nombre_red} key={contrasena}')
    os.system('netsh wlan start hostednetwork')

# Detener el punto de acceso Wi-Fi
def detener_punto_acceso():
    os.system('netsh wlan stop hostednetwork')

# Crear el punto de acceso con el nombre y la contraseña especificada
nombre_red = 'MiRedWiFi'
contrasena = 'ContraseñaSegura123'

crear_punto_acceso(nombre_red, contrasena)
