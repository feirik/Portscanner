### Brief
Simple Python3 TCP port scanner. Usage: python3 portscanner.py [-p, -T] `<ip or domain target>`

### Command line options
#### -p --port `<port>` OR `<port1>,<port2>`... OR `<startPort-endPort>` (required)
Selects port(s) to scan. Possible to set single port, multiples and a range of ports.

#### -T --timeout `<decimalInSeconds>` (optional)
Sets timeout before attempting to connect next port. Default value is set to 0.5s. 

