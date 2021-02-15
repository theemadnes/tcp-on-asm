# tcp-on-asm
sample code for a tcp service exposed via an Anthos Service Mesh's ingress gateway, and a locally run "client" app

this walkthrough exposes a TCP-based service on a non-standard port via ASM's ingress gateway.

### setup

for this to work through ASM's ingress gateway via a non-standard port, you must add additional an additional port to the ingress gateway service. once you've done this, `istioctl analyze` can confirm that the port you're attempting to use is accessible via the ingress gateway:

```bash
$ istioctl analyze -n tcp-server

✔ No validation issues found when analyzing namespace: tcp-server.
```

also, in `tcp-client/client.py`, update the IP address to reflect your ingress gateway's public IP.

### example usage

```bash
$ for i in {1..10}; do python3 tcp-client/client.py; done
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-7sldk'
closing socket
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-4s922'
closing socket
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-7sldk'
closing socket
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-7sldk'
closing socket
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-bgzwn'
closing socket
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-4s922'
closing socket
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-7sldk'
closing socket
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-bgzwn'
closing socket
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-bgzwn'
closing socket
connecting to 34.67.100.153 port 5000
sending b'ping to server alexmattson-macbookpro2.roam.corp.google.com:5000'
received b'pong from tcp-server-6db4755594-bgzwn'
closing socket
```