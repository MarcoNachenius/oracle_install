# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi


# ORACLE DB FILE STRUCTURE
# ========================
# /u01/
# └── app/
#     └── oracle/
#         ├── product/
#         │   └── 19c/
#         │       └── db_home_1/          # ORACLE_HOME
#         ├── admin/                    # Database administration files
#         ├── oradata/                  # Database data files
#         ├── fast_recovery_area/       # Backup and recovery files
#         └── diag/                     # Diagnostic logs


umask 022
export ORACLE_SID=ORCLCDB
export ORACLE_BASE=/opt/oracle
export ORACLE_HOME=/opt/oracle/product/19c/dbhome_1
export PATH=$PATH:$ORACLE_HOME/bin