#!/bin/bash
echo "bash -c '/home/walkinggiraffe/server/mail-server/sendmail.sh $1 $2 \"$3\"'" > /app/mail_pipe
