**Scanning de Red con Scapy**

**Descripción**
Este proyecto utiliza la biblioteca **Scapy** para escanear dispositivos en una red local. Al enviar paquetes ARP (Address Resolution Protocol) y recibir respuestas, el script identifica y muestra las direcciones IP y MAC de los dispositivos conectados a la red. Este script es útil para administradores de red y entusiastas de la ciberseguridad que deseen explorar y analizar sus redes locales.

**Requisitos**
Para ejecutar este script, necesitas tener instalado:
- Python 3.x
- Scapy

Puedes instalar Scapy ejecutando:
```bash
pip install scapy
```
**Uso**

1. Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/natuska26/Network-Scanner.git
```

2. Navega al directorio del proyecto:

```bash
cd Network-Scanner
```

3. Abre el archivo Python en un editor de texto o IDE.

4. Cambia el valor de target_ip a un rango de red que desees escanear (por ejemplo, 192.168.1.0/24).

5. Ejecuta el script:

```bash
python scapy_network_scanner.py
