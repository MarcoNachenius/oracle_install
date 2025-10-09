#!/usr/bin/bash

dnf install -y kernel-uek-devel-$(uname -r)


# NOTE: The following commands are specific to enabling VirtualBox Guest Additions.
# They assume that the VirtualBox Guest Additions ISO is already mounted to the VM.
# If not, you may need to mount it manually via the VirtualBox interface.
sudo mkdir /mnt/cdrom
sudo mount /dev/cdrom /mnt/cdrom
cd /mnt/cdrom
sudo ./VBoxLinuxAdditions.run
