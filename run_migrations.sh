#!/bin/bash

# Set the FLASK_APP environment variable to migration.py
export FLASK_APP=migration.py

# Initialize the migration repository
flask db init

# Create a migration script
flask db migrate -m "create student table"

# Apply the migration
flask db upgrade

echo "Migrations completed successfully!"
