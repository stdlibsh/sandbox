#!/usr/bin/env bash

set -e

if [ "$1" = "server" ]; then
	exec gunicorn sandbox.asgi:application \
	  --worker-class uvicorn.workers.UvicornWorker \
	  --bind 0.0.0.0:8000 \
	  --access-logfile "-" \
	  --error-logfile "-" \
	  --forwarded-allow-ips "*"
fi

exec "$@"
