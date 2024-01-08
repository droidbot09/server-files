#!/bin/bash

echo "Starting the installation process..."

# Clone the repository
git clone https://github.com/droidbot09/server-files

# Check if the clone was successful
if [ $? -eq 0 ]; then
    echo "Download successful. Proceeding with installation..."

    # Move proxy_service file to /usr/local/bin/
    mv server-files/proxy_service /usr/local/bin/

    # Move proxy_service.service file to /usr/lib/systemd/system/
    mv server-files/proxy_service.service /usr/lib/systemd/system/

    # Enable the systemd service
    sudo systemctl enable proxy_service.service

    # Clean up - delete files
    rm -rf server-files

    echo "Installation completed. Necessary dependencies and files installed."

else
    echo "Download failed. Please check your internet connection and try again."
fi
