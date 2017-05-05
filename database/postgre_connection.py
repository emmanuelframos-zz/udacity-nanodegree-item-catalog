import sqlalchemy
from sqlalchemy.orm import sessionmaker

from database_setup import Base

class PostgreConnection:
    """
    Class used to connect on database and return the connection object
    """
    database_dict = dict(line.strip().split('=') for line in open('database.properties'))

    connection = None

    @staticmethod
    def get_connection():
        """
        Method that returns the open connection to the database
        :return: Connection
        """
        try:
            if not PostgreConnection.connection:
                url = "postgresql://{}:{}@{}:{}/{}"

                url = url.format(PostgreConnection.database_dict.get("username"),
                                 PostgreConnection.database_dict.get("password"),
                                 PostgreConnection.database_dict.get("hostname"),
                                 PostgreConnection.database_dict.get("port"),
                                 PostgreConnection.database_dict.get("database"))

                connection = sqlalchemy.create_engine(url, client_encoding=PostgreConnection.database_dict.get("encoding"))

                Base.metadata.bind = connection
        except:
            print "Cannot to connect to the database: " + \
                  PostgreConnection.database_dict.get("database")

        return connection

    @staticmethod
    def get_session():
        connection = PostgreConnection.get_connection()
        session = sessionmaker(bind=connection)
        return session()