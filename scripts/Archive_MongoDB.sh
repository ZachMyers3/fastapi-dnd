#!/bin/bash
# MongoDB Archival Script
# Author - Tyler Sparr
# A script which is run weekly in order to backup a specific MongoDB host to a specified folder.
# It is designed to be run on an automated weekly basis. Not Ad-Hoc.
# Usage: ./Archive_MongoDB.sh <MongDB Server URL> <Database Name> <Database User> <Database User's Password> </path/to/destination/folder> <# of weeks of backup to maintain>

#Initial Vars Passed In
HOST="$1"
DATABASE="$2"
USER="$3"
PASS="$4"
ARCHIVE_FOLDER="$5"
WEEKS=$6

# Calculate what the oldest date we're keeping is
DELETION_DATE=$(date -v -"$WEEKS"w +%m-%d-%y)

# Dump the databases to specified area and name the folder appropriately based on date
/usr/local/bin/mongodump -h $HOST -d $DATABASE -u $USER -p $PASS -o "$ARCHIVE_FOLDER/Archive_$(date +%m-%d-%y)"

# If the oldest folder exists, delete it
if [[ -d "$ARCHIVE_FOLDER/Archive_$DELETION_DATE" ]]; then

  rm -R "$ARCHIVE_FOLDER/Archive_$DELETION_DATE"

fi

exit 0
