
# Build the Docker image from the Dockerfile in the 00_python_container/ directory
docker build -t python_container_with_script:latest ./

# Run container
docker run python_container_with_script:latest

