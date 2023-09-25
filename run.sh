#!/bin/bash
docker run \
    --restart unless-stopped \
    -d \
    -e FROM_ADDRESS=ADDRESS \
    -e TO_ADDRESS=ADDRESS \
    -e PASSWORD=PASSWORD \
    -p 8081:8000 \
    --name cv-website \
    cv-website
