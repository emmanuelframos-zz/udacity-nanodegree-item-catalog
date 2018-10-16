import sqlalchemy
from sqlalchemy.orm import sessionmaker

from database_setup import Base

class PostgreConnection:
    """
    Class used to connect on database and return the connection object
    """
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

                url = url.format("grader",
                                 "l1nux;",
                                 "ec2-18-216-2-201.us-east-2.compute.amazonaws.com",
                                 "5432",
                                 "item-catalog")

                connection = sqlalchemy.create_engine(url, client_encoding=PostgreConnection.database_dict.get("UTF8"))

                Base.metadata.bind = connection

            return connection
        except:
            print "Cannot to connect to the database: " + \
                  PostgreConnection.database_dict.get("database")

    @staticmethod
    def get_session():
        connection = PostgreConnection.get_connection()
        session = sessionmaker(bind=connection)
        return session()