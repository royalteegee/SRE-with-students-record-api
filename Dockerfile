# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the image
COPY . .

# Ensure the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Expose the port the app runs on
EXPOSE 5000

# Run the entrypoint script
CMD ["/app/entrypoint.sh"]