#!/bin/bash
gunicorn -b 0.0.0.0:10000 fb_auto_create_backend:app
