#!/bin/bash

# ###### 启动服务 ##########
cd /www/server && celery -A server.app worker --pool=solo --concurrency=${WORKER} --heartbeat-interval=${CELERY_HEARTBEAT}
