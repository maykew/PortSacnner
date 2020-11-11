### Trabalho 5 ###
import socket
import sys
import threading

def scanClasse(ipAddress, portaInicial, portaFinal):
    octets = ipAddress.split(".")
    if int(ipAddress[0:3]) < 128:
        if len(octets) == 1:
            print('Endereco IP: %s.0.0.0 - Classe A' % ipAddress)
        elif len(octets) == 2:
            print('Endereco IP: %s.0.0 - Classe A' % ipAddress)
        elif len(octets) == 3:
            print('Endereco IP: %s.0 - Classe A' % ipAddress)
        elif len(octets) == 4:
            print('Endereco IP: %s - Classe A' % ipAddress)
        for octet2 in range(0, 255):
            for octet3 in range(0, 255):
                ip = str(octets[0]) + '.' + str(octet2) + '.' + str(octet3)
                initThread(ip, portaInicial, portaFinal)
    
    elif int(ipAddress[0:3]) > 127 and int(ipAddress[0:3]) < 192:
        if len(octets) == 2:
            print('Endereco IP: %s.0.0 - Classe B' % ipAddress)
        elif len(octets) == 3:
            print('Endereco IP: %s.0 - Classe B' % ipAddress)
        elif len(octets) == 4:
            print('Endereco IP: %s - Classe B' % ipAddress)
        for octet3 in range(0, 255):
            ip = str(octets[0]) + '.' + str(octets[1]) + '.' + str(octet3)
            initThread(ip, portaInicial, portaFinal)
            
    else:
        if len(octets) == 3:
            print('Endereco IP: %s.0 - Classe C' % ipAddress)
        elif len(octets) == 4:
            print('ipAddress IP: %s - Classe C' % ipAddress)
        initThread(ipAddress, portaInicial, portaFinal)

def  initThread(rede, portaInicial, portaFinal):
    (threading.Thread(target=scanRede,args=(rede, 1, 100, portaInicial, portaFinal,))).start()
    (threading.Thread(target=scanRede,args=(rede, 100, 200, portaInicial, portaFinal,))).start()
    (threading.Thread(target=scanRede,args=(rede, 200, 255, portaInicial, portaFinal,))).start()

def scanRede(rede, ini, fim, portaInicial, portaFinal):
    print('Buscando portas abertas nos hosts da rede %s.0' % rede)
    for host in range(ini, fim):
        ip = rede + '.' + str(host)
        scanHost(ip, portaInicial, portaFinal)

def scanHost(ip, portaInicial, portaFinal):
    print('Buscando portas abertas no host %s' % ip)
    scanPorta(ip, portaInicial, portaFinal)
    print('Fim da busca no host %s' % ip)

def scanPorta(ip, portaInicial, portaFinal):
    for port in range(portaInicial, portaFinal + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            if not tcp.connect_ex((ip, port)):
                print('Porta %s:%d/TCP aberta' % (ip, port))
                tcp.close()
                
        except Exception:
            pass


if __name__ == '__main__':
    # Timeout em segundos
    socket.setdefaulttimeout(0.001)

    if len(sys.argv) < 4:
        print('Uso: ./portscanner.py <end IP> <porta inicial> <porta final>')
        print('Exemplo: ./portscanner.py 192.168.1.10 1 65535\n')
        print('Uso: ./portscanner.py <end rede> <porta inicial> <porta final> -n')
        print('Exemplo: ./portscanner.py 192.168.1 1 65535 -n')

    elif len(sys.argv) >= 4:
        rede   = sys.argv[1]
        portaInicial = int(sys.argv[2])
        portaFinal   = int(sys.argv[3])

    if len(sys.argv) == 4:
        scanHost(rede, portaInicial, portaFinal)

    if len(sys.argv) == 5:
        scanClasse(rede, portaInicial, portaFinal)