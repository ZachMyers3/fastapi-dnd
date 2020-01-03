#!/bin/bash
# MongoDB Archival Script
# Author - Tyler Sparr
# A script which is run weekly in order to backup a specific MongoDB host to a specified folder.
# It is designed to be run on an automated weekly basis. Not Ad-Hoc.
# Usage: ./Archive_MongoDB.sh -MONGODB_HOST <URL to MongoDB host> -ARCHIVE_FOLDER <path\to\destination\folder> -WEEKS <# Of Weeks to Maintain>

#Initial Vars Passed In
HOST="$1"
DATABASE="$2"
USER="$3"
PASS="$4"
ARCHIVE_FOLDER="$5"
WEEKS=$6

DELETION_DATE=$(date -v -"$WEEKS"w +%m-%d-%y)

/usr/local/bin/mongodump -h $HOST -d $DATABASE -u $USER -p $PASS -o "$ARCHIVE_FOLDER/Archive_$(date +%m-%d-%y)"


if [[ -d "$ARCHIVE_FOLDER/Archive_$DELETION_DATE" ]]; then

  rm -R "$ARCHIVE_FOLDER/Archive_$DELETION_DATE"

fi

exit 0
