# Cryptocurrency Price Fetcher

This Flask application fetches the last 24 hours average prices for Bitcoin and Ethereum in USD and EUR from the CoinGecko API.

## Installation

### Prerequisites

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) (for running with Docker)
- [Python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installation/) (for running without Docker)

### Using Docker Compose

1. Clone the repository: `git clone https://github.com/yourusername/cryptocurrency-price-fetcher.git`
2. Navigate to the project folder: `cd cryptocurrency-price-fetcher`
3. Make the scripts executable: `chmod +x run.sh stop.sh`
4. Run the `run.sh` script to build and start the Docker containers: `./local-dev/run.sh`

Once the Docker containers are running, navigate to `http://localhost:8080` in your web browser. You will see a JSON response with the latest prices for Bitcoin and Ethereum in USD and EUR.

To stop the application and remove the Docker containers, run the `stop.sh` script: `./local-dev/stop.sh`

### Using Docker

1. Clone the repository: `git clone https://github.com/yourusername/cryptocurrency-price-fetcher.git`
2. Navigate to the project folder: `cd cryptocurrency-price-fetcher`
3. Build the Docker image: `docker build -t cryptocurrency-price-fetcher -f docker/app.Dockerfile .`
4. Run the Docker container: `docker run -p 8080:8080 cryptocurrency-price-fetcher`

Once the Docker container is running, navigate to `http://localhost:8080` in your web browser. You will see a JSON response with the latest prices for Bitcoin and Ethereum in USD and EUR.

### Without Docker

1. Clone the repository: `git clone https://github.com/yourusername/cryptocurrency-price-fetcher.git`
2. Navigate to the project folder: `cd cryptocurrency-price-fetcher`
3. Install the dependencies: `pip3 install -r app/requirements.txt`
4. Run the application: `python3 app/app.py`

## Helm Installation

### Prerequisites

- [Helm](https://helm.sh/) should be installed on your machine.
- Access to a Kubernetes cluster.

### Installing the Helm Chart

1. Clone the repository: `git clone https://github.com/yourusername/cryptocurrency-price-fetcher.git`
2. Navigate to the project folder: `cd cryptocurrency-price-fetcher`
3. Install the Helm chart: `helm upgrade -i cryptocurrency-price-fetcher chart/. -n <namespace>`

Replace cryptocurrency-price-fetcher with a name of your choice and adjust other parameters as needed.

### Configuration

Modify the values.yaml file in the chart directory to customize the deployment according to your requirements.
