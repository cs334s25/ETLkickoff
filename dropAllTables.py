import boto3
import pymysql

# AWS RDS settings
rds_host = "your-rds-endpoint"
db_username = "your-username"
db_password = "your-password"
db_name = "your-database-name"

# Connect to the database
connection = pymysql.connect(
    host=rds_host,
    user=db_username,
    password=db_password,
    database=db_name
)

try:
    with connection.cursor() as cursor:
        # Fetch all table names
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # Drop each table
        for table in tables:
            table_name = table[0]
            drop_table_query = f"DROP TABLE IF EXISTS `{table_name}`"
            cursor.execute(drop_table_query)
            print(f"Dropped table {table_name}")

    # Commit changes
    connection.commit()
finally:
    connection.close()