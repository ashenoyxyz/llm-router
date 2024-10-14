## README

- Simulating path based routing using nginx ingress controller.
- Each service (openai, llama, anthropic) is setup as a `Deployment` with 3 replicas each.
- Requests will be routed based on the paths (/openai, /llama, /anthropic) and subsequently load balanced among the 3 replicas.

## Prerequisites

Enable the microk8s ingress addon,
```bash
# microk8s enable ingress

# kubectl get pods -n ingress
NAME                                      READY   STATUS    RESTARTS   AGE
nginx-ingress-microk8s-controller-k2q9r   1/1     Running   0          25m
```

**Note:** Nginx ingress controller creates an ingress class called `public`, which we'll use for creating the Ingress object later.

Enable microk8s registry or setup a docker registry using this command,
```bash
docker run -d -p 32000:5000 --name registry registry:2.7
```

Build and push the llm-service image,
```bash
# cd llm-service
# ./build_image.sh
```

## Deployment

Deploy the llm services,
```bash
# cd scripts
# kubectl create -f openai.yaml
# kubectl create -f llama.yaml
# kubectl create -f anthropic.yaml
```

Deploy the ingress,
```bash
# cd scripts
# kubectl create -f llm-ingress.yaml
```

## Testing

```bash
# curl http://localhost/openai
{"host":"openai-5c6f988f8f-4llcl","type":"OPENAI","request_count":1}

# curl http://localhost/llama
{"host":"llama-779f556f74-qswgn","type":"LLAMA","request_count":1}

# curl http://localhost/anthropic
{"host":"anthropic-655dbc78c9-bdcp7","type":"ANTHROPIC","request_count":1}
```
