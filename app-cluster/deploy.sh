#!/bin/bash

echo "🚀 Starting Deployment..."

# 1. Pull latest changes (if using git)
# git pull origin main

# 2. Rebuild and restart in background
docker compose up -d --build

# 3. Wait and check health
echo "⏳ Waiting for health check..."
sleep 10
docker ps | grep agoda-repeat-web-app-1

echo "✅ Done!"
