#!/bin/bash
set -e

# Set the FLASK_APP environment variable to migration.py
export FLASK_APP=migration.py

# Initialize the migration repository if it doesn't exist
if [ ! -d "migrations" ]; then
  flask db init
fi

# Check if the database is in sync with the latest migration
flask db stamp head

# Create a migration script (if needed)
flask db migrate -m "create student table"

# Apply the migration
flask db upgrade

# Set the FLASK_APP environment variable to main.py for Gunicorn
export FLASK_APP=main:app

# Run the main Flask app with Gunicorn
exec gunicorn --bind 0.0.0.0:5000 main:app