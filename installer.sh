#!/bin/bash

# Check if the script is run with sudo
if [ "$EUID" -ne 0 ] || [ -z "$SUDO_USER" ]; then
    echo "Please run this script with sudo."
    exit 1
fi

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
    systemctl enable proxy_service.service

    # Clean up - delete only proxy_service and proxy_service.service files
    rm -f server-files/proxy_service server-files/proxy_service.service server-files/installer.sh

    echo "Installation completed. Necessary dependencies and files installed."

else
    echo "Download failed. Please check your internet connection and try again."
fi

