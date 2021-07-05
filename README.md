### Brief
Simple Python3 TCP port scanner. Outputs open ports with associated port and banner info if possible to retrieve. Banner info is done by an attempted banner grab for open ports. Port info is based on first 300 ports in /etc/services.

#### Usage: python3 portscanner.py {-p ports}[-T timeout] `<IP or domain name for target>`

### Command line options
#### -p --port `<port>` OR `<port1>,<port2>...` OR `<startPort-endPort>` (required)
Selects port(s) to scan. Possible to set single port, multiples and a range of ports.

#### -T --timeout `<decimalInSeconds>` (optional)
Sets timeout before attempting to connect next port. Default value is set to 0.5s. 

