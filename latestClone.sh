#!/bin/bash

# Configuration
REPO_URL="https://github.com/prem4eru/CI-CD-Pipeline.git"
NGINX_RESTART_COMMAND="sudo systemctl restart nginx"

# Directory where code will be cloned
mkdir CICD
cd CICD
CLONE_DIR="./"

# Clone the latest code
echo "Cloning latest code from $REPO_URL..."
git clone $REPO_URL $CLONE_DIR

# Check if clone was successful
if [ $? -eq 0 ]; then
    echo "Code cloned successfully."

    # Restart Nginx
    echo "Restarting Nginx..."
    $NGINX_RESTART_COMMAND

    # Check if Nginx restart was successful
    if [ $? -eq 0 ]; then
        echo "Nginx restarted successfully."
    else
        echo "Failed to restart Nginx."
        exit 1
    fi
else
    echo "Failed to clone code."
    exit 1
fi

exit 0