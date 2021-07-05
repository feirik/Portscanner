import argparse
import portscannerLib

parser = argparse.ArgumentParser(description='Simple portscanner.')
parser.add_argument("-p", "--port", type=str, help="Ports to scan")
parser.add_argument("-T", "--timeout", type=float, help="Timeout in seconds when attempting to connect to a port")
args, target = parser.parse_known_args()

portscannerLib.scan(target[0], args.port, args.timeout)
