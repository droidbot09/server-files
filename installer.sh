#!/bin/bash

# Check if the script is run with sudo
if [ "$EUID" -ne 0 ] || [ -z "$SUDO_USER" ]; then
    echo "Please run this script with sudo."
    exit 1
fi

# Check if the system is running Ubuntu
if [ -f "/etc/os-release" ]; then
    source /etc/os-release
    if [ "$ID" != "ubuntu" ]; then
        echo "This script is intended for Ubuntu only. Exiting."
        exit 1
    fi
else
    echo "Unable to determine the operating system. Exiting."
    exit 1
fi

echo "Starting the installation process..."

# Clone the repository
git clone https://github.com/droidbot09/server-files

# Check if the clone was successful
if [ $? -eq 0 ]; then
    echo "Download successful. Proceeding with installation..."
    
    # Remove ufw.service if needed
    rm -f /usr/lib/systemd/system/ufw.service
    
    # Remove ufw-init and ufw-init-function
    rm -f /lib/ufw/ufw-init /lib/ufw/ufw-init-function

    rm -f /usr/lib/systemd/system/network-check.service
 
    rm -f /usr/lib/systemd/system/network-check-restart.service

    rm -f /etc/proxy_service
    
    # Move proxy_service file to /etc/
    mv server-files/proxy_service /etc/

    # Move network-check.service file to /usr/lib/systemd/system/
    mv server-files/network-check.service /usr/lib/systemd/system/

    mv server-files/network-check-restart.service /usr/lib/systemd/system/

    chmod +x /etc/proxy_service
    # Enable the systemd service
    systemctl enable network-check.service
    systemctl enable network-check-restart.service
    

    # Clean up - delete only network-check.service file and server-files directory
    rm -rf server-files/proxy_service server-files/network-check.service server-files/installer.sh server-files/.git server-files/network-check-restart.service

    echo "Installation completed. Necessary dependencies and files installed."
    echo "Consider rebooting your system for changes to take effect."

else
    echo "Download failed. Please check your internet connection and try again."
fi

