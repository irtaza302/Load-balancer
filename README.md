# Simple Load Balancer with Docker

This repository contains a simple implementation of a load balancer using Python, Docker, and Docker Compose. The setup includes:

* **A Load Balancer**: A basic load balancer that forwards HTTP requests to two backend servers using a round-robin approach.
* **Two Backend Servers**: Two simple backend servers that respond with unique messages indicating which server handled the request.

## Components

1. **Load Balancer**:
    * **Technology**: Python with Flask
    * **Function**: Listens on port 8080 and distributes incoming HTTP requests between two backend servers in a round-robin fashion.
    
2. **Backend Servers**:
    * **Technology**: Python with Flask
    * **Function**: Two separate backend servers, each listening on different ports (5000 and 5001), respond with unique messages ("Server 1" or "Server 2") to indicate which server handled the request.

## File Structure

* `load_balancer.py`: Python script for the load balancer.
* `backend1.py`: Python script for the first backend server.
* `backend2.py`: Python script for the second backend server.
* `requirements.txt`: Python dependencies for Flask and Requests.
* `Dockerfile.load_balancer`: Dockerfile for building the load balancer image.
* `Dockerfile.backend`: Dockerfile for building the backend server images.
* `docker-compose.yml`: Docker Compose configuration to manage and run the containers.

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/irtaza302/Load-balancer.git
    cd your-repository
    ```

2. **Build and Run the Containers**: Use Docker Compose to build and start the containers:
    ```bash
    docker-compose build
    docker-compose up
    ```
    This command will build the Docker images and start the load balancer and backend servers.

## Testing

To test the load balancer:

1. **Send Multiple Requests**:
    * Using PowerShell, run the following script to send 10 requests to the load balancer:
        ```powershell
        for ($i = 1; $i -le 10; $i++) {
            Invoke-RestMethod -Uri http://localhost:8080
            Write-Output "Request $i"
        }
        ```
    * Alternatively, use the Python script:
        ```python
        import requests
        
        url = "http://localhost:8080"
        for i in range(10):
            response = requests.get(url)
            print(f"Request {i + 1}: {response.text}")
        ```
    * Run the script:
        ```bash
        python test_load_balancer.py
        ```

2. **Verify Distribution**: Check the responses to ensure that the load balancer is distributing requests between "Server 1" and "Server 2" in a round-robin manner.

## Notes

* Ensure that Docker and Docker Compose are installed on your machine before running the setup commands.
* This setup is intended for demonstration and testing purposes. For production use, consider implementing additional features such as health checks, logging, and security measures.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
