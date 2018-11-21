import nmap

nm = nmap.PortScanner()

ret = nm.scan('192.168.0.122','20-3307')

print(ret)