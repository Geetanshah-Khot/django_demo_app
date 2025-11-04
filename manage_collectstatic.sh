#!/usr/bin/env bash
echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Listing collected files:"
ls -R staticfiles/rest_framework || echo "No rest_framework files found"
