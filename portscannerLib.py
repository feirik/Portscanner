import socket
import portinfo
from IPy import IP

DEFAULT_TIMEOUT = 0.5
MAX_PORT_NUM = 65535


def scan(target, ports, timeout):
    ip = convert_domain_name_to_ip(target)

    # Use argument timeout if provided and valid
    if timeout is not None:
        if timeout > 0.0:
            pass
        else:
            print('Timeout ' + str(timeout) + 's is less than 0.0, using default ' + str(DEFAULT_TIMEOUT) + 's instead.')
            timeout = DEFAULT_TIMEOUT
    else:
        timeout = DEFAULT_TIMEOUT

    if ip != "":
        print('[!] Scanning target] ' + str(target))

        # startport-endport format
        if '-' in ports:
            try:
                start_port = int(ports.split('-')[0])
                end_port = int(ports.split('-')[1])

                if (start_port <= end_port) and (1 <= start_port) and (end_port <= MAX_PORT_NUM):
                    for port in range(start_port, end_port + 1):
                        scan_port(ip, port, timeout)
                else:
                    print('Port range: ' + str(ports) + ' invalid! Usage: -p <startPort-endPort>')
            except ValueError:
                print('Port range: ' + str(ports) + ' invalid! Usage: -p <startPort-endPort>')

        # port1,port2... format
        elif ',' in ports:
            for port in ports.split(','):
                try:
                    if 1 <= int(port) <= MAX_PORT_NUM:
                        scan_port(ip, int(port), timeout)
                except ValueError:
                    print('Port: ' + str(port) + ' invalid! Usage: -p <portNumber1>,<portNumber2>...')

        # Single port format
        else:
            try:
                if 1 <= int(ports) <= MAX_PORT_NUM:
                    scan_port(ip, int(ports), timeout)
            except ValueError:
                print('Port: ' + str(ports) + ' invalid! Usage: -p <portNumber>')


# Check if IP is of IP format, else get IP address from domain name lookup
def convert_domain_name_to_ip(target):
    try:
        IP(target)
        return(target)
    except ValueError:
        try:
            return socket.gethostbyname(target)
        except socket.gaierror:
            print('Target: ' + str(target) + ' is an invalid domain name or IP address!')
            return ""


def get_banner(s):
    return str(s.recv(1024).decode('utf-8').strip('\n'))


# Scan a port to check if it is possible to establish a TCP connection
def scan_port(ipaddress, port, timeout):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Port ' + str(port) + ' (' + portinfo.get_port_info(port) + ') open - banner:' + banner)
        except:
            print('[+] Port ' + str(port) + ' (' + portinfo.get_port_info(port) + ') open')
    except:
        pass
