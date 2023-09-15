# tcp-on-asm

sample TCP services using https://docs.python.org/3/library/asyncio-stream.html#tcp-echo-client-using-streams on K8s

### build 

```
# server 
docker build -t us-central1-docker.pkg.dev/cicd-system-demo-01/cicd-demo-01/tcp-on-asm-server .
docker push us-central1-docker.pkg.dev/cicd-system-demo-01/cicd-demo-01/tcp-on-asm-server

# client 
docker build -t us-central1-docker.pkg.dev/cicd-system-demo-01/cicd-demo-01/tcp-on-asm-client .
docker push us-central1-docker.pkg.dev/cicd-system-demo-01/cicd-demo-01/tcp-on-asm-client
```