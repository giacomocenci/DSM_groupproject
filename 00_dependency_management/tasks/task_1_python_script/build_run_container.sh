
# Build the Docker image from the Dockerfile in the 00_python_container/ directory
docker build -t task_1:latest ./

# Run container
docker run task_1:latest
