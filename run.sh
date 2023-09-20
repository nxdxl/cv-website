#!/bin/bash
docker run \
    --restart unless-stopped \
    -d \
    -p 8081:8000 \
    -v /home/walkinggiraffe/server/mail-server/mail_pipe:/app/mail_pipe \
    --name cv-website \
    cv-website
