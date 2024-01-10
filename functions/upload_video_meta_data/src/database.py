import os
import logging
import pymysql
from constants import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

class DatabaseManager:
    def __init__(self):
        self.conn = self._connect()

    def _connect(self):
        """Create connection to RDS database

        Returns:
            pymysql.connection: Connection to RDS database
        """
        try:
            conn = pymysql.connect(
                host=DB_HOST,
                user=DB_USER,
                passwd=DB_PASSWORD,
                db=DB_NAME,
                connect_timeout=5
            )
            return conn
        except pymysql.MySQLError as e:
            logging.error(e)
            raise e

    def execute_query(self, query, params=None):
        """Execute a given SQL query

        Args:
            query (str): SQL query to execute
            params (tuple, optional): Parameters for the SQL query. Defaults to None.

        Returns:
            list: Results of the SQL query
        """
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def close_connection(self):
        """Close the database connection"""
        self.conn.close()
