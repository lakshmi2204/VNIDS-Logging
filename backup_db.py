import shutil

# Source database
source_db = "logs.db"

# Backup file
backup_db = "logs_backup.db"

# Copy database
shutil.copy(source_db, backup_db)

print("Database backup created successfully!")