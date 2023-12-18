#!/bin/sh
# until cd /app/
# do
#     echo "Waiting for server volume..."
# done

# run a worker 
celery --app=Ryvm_project worker --pool=solo -l INFO
celery -A Ryvm_project beat -l INFO