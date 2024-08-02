import MySQLdb
from config import Config

def init_db():
    connection = MySQLdb.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        passwd=Config.MYSQL_PASSWORD,
        db=Config.MYSQL_DB
    )
    
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        is_read BOOLEAN NOT NULL DEFAULT FALSE
    )
    """)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    init_db()
