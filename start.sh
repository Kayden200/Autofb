#!/bin/bash
gunicorn -b 0.0.0.0:10000 fb_auto_create_backend:app

#!/bin/bash
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
gunicorn -b 0.0.0.0:10000 fb_auto_create_backend:app
