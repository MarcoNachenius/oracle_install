STEP 1: Before running VM
=========================
1.1 - Download Oracle Linux 8 OS image (https://yum.oracle.com/ISOS/OracleLinux/OL8/u10/x86_64/OracleLinux-R8-U10-x86_64-boot.iso)
1.2 - Download Oracle Database 19c rpm package (https://download.oracle.com/otn/linux/oracle19c/190000/oracle-database-ee-19c-1.0-1.x86_64.rpm)
1.3 - Place rpm package inside folder named 'shared_files'

STEP 2: Using VirtualBox manager
================================
2.1 - Run VM using Oracle Linux 8 OS image from Step 1.1
2.2 - Select 'Starnard' install 
       (Software selection -> Minimple install -> Standard)
2.3 - Mount Guest Additions CD 
       (VirtualBox VM -> Devices -> Insert Guest Additions CD image...)
2.4 - Share folder from Step 1.3 
       (VirtualBox VM -> Devices -> Shared Folders)
       (RPM package should appear indside vm path '/media/sf_shared_files/')
2.5 - Login as root
2.6 - Install git using 'dnf -y install git'
2.7 - Download git repo using 'git clone https://github.com/MarcoNachenius/oracle_install.git' 
2.8 - cd into downloaded git repo
2.9 - run 'bash main.sh'