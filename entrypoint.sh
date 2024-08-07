#!/bin/bash

# Set the FLASK_APP environment variable to migration.py
export FLASK_APP=migration.py

# Initialize the migration repository
flask db init

# Create a migration script
flask db migrate -m "create student table"

# Apply the migration
flask db upgrade

# Set the FLASK_APP environment variable to main.py for Gunicorn
export FLASK_APP=main:app

# Run the main Flask app with Gunicorn
gunicorn --bind 0.0.0.0:5000 main:app

----------------------------------------------------------------------
#!/bin/bash

# Ensure the script exits if a command fails
set -e

# Set the FLASK_APP environment variable to migration.py
export FLASK_APP=migration.py

# Initialize the migration repository if it doesn't exist
if [ ! -d "migrations" ]; then
  flask db init
fi

# Create a migration script
flask db migrate -m "create student table"

# Apply the migration
flask db upgrade

# Set the FLASK_APP environment variable to main.py for Gunicorn
export FLASK_APP=main:app

# Run the main Flask app with Gunicorn
exec gunicorn --bind 0.0.0.0:5000 main:app
