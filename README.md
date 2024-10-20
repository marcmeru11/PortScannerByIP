# PortScannerByIP
Given an IP range it scans all the devices on your net in that range and returns the IP and the MAC directions. Besides it can scan a given port for a given IP and return a boolean type for the result (open port / closed).

## How to use

### Example 1:
```
import scanIP

scanIP("192.168.1.1/24")
```
This code will return a dictionary with all the IP directions and their MAC.

### Example 2:
```
import scanPort

scanPort("192.168.1.1", 80)
```
This code will return true if the given port is open for the given IP, otherwise it will return false.
