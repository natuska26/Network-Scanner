from scapy.all import ARP, Ether, srp

# Definimos el rango de direcciones IP a escanear en la red local.
target_ip = "192.168.1.0/24"

# Creamos un paquete ARP para enviar una solicitud de descubrimiento a la red.
arp = ARP(pdst=target_ip)

# Creamos un paquete Ethernet con la dirección MAC de difusión que permite enviar el paquete a todos los dispositivos en la red local.
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Apilamos el paquete Ethernet con el paquete ARP para formar un único paquete.
packet = ether/arp

#Enviamos el paquete y esperamos recibir respuestas de los dispositivos en la red; siendo timeout=3 espera hasta 3 segundos por respuestas, 
# y verbose=0 oculta la salida detallada
result = srp(packet, timeout=3, verbose=0)[0]

# Inicializamos una lista para almacenar los dispositivos encontrados en la red.
clients = []

#Recorremos las respuestas recibidas.
for sent, received in result:
    # Por cada respuesta, añadimos la dirección IP y la dirección MAC del dispositivo a la lista 'clientes'.
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# Mostramos los dispositivos disponibles en la red.
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
    #Mostramos la IP y MAC de cada cliente encontrado.
exit()
