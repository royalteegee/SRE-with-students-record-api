# # Use the official Python image from the Docker Hub
# FROM python:3.9-slim

# # Set the working directory
# WORKDIR /app

# # Copy the requirements file into the image
# COPY requirements.txt .

# # Install the dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code into the image
# COPY . .

# # Ensure the entrypoint script is executable
# RUN chmod +x /app/entrypoint.sh

# # Expose the port the app runs on
# EXPOSE 5000

# # Run the entrypoint script
# CMD ["/app/entrypoint.sh"]


# Stage 1: Build stage
FROM python:3.9-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the image
COPY . .

# Stage 2: Final stage
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app .

# Ensure the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Expose the port the app runs on
EXPOSE 5000

# Run the entrypoint script
CMD ["/app/entrypoint.sh"]
