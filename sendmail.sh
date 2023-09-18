#!/bin/bash
sendmail -i -t << MESSAGE_END
From: website@tomkeilers.com
To: info@tomkeilers.com
Subject: incoming request from website

Name: $1
E-Mail: $2
Message: $3
MESSAGE_END
