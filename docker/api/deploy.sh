#!/bin/bash

while true; do
  pg_isready -q -d "$DB_NAME" -h "$DB_HOST" -U "$DB_USER";
  status=$?;
  if [ "$status" == 0 ]; then break;
  fi;
  sleep 2;
done;

    flask delete_tables
    flask create_tables
    flask import_data
    python3 run.py
