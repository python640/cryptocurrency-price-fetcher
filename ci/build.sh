docker buildx build -t docker.io/python640/cryptocurrency-price-fetcher:0.0.2 --platform linux/amd64,linux/arm64 -f 'docker/app.Dockerfile' . --push
