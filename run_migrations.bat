@echo off
REM Set the FLASK_APP environment variable to migration.py
set FLASK_APP=migration.py

REM Initialize the migration repository
flask db init

REM Create a migration script
flask db migrate -m "create student table"

REM Apply the migration
flask db upgrade

echo Migrations completed successfully!
