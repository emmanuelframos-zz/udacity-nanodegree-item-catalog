from database.postgre_connection import PostgreConnection


class DAO:
    """
    Class that represents the Data Access Object (Generic) 
    pattern in a simple way
    """
    @staticmethod
    def session():
        """ Returns opened session 
        :return: Session
        """
        return PostgreConnection.get_session()

    @staticmethod
    def find(cls, **args):
        """ 
        Finds one unique object
        :return: Object
        """
        session = PostgreConnection.get_session()
        one_result = session.query(cls).filter_by(**args).first()
        if one_result is not None:
            session.expunge(one_result)
        return one_result

    @staticmethod
    def find_all(cls):
        """ 
        Finds a list of object
        :return: List of Object
        """
        session = PostgreConnection.get_session()
        return session.query(cls).all()

    @staticmethod
    def create(object):
        """ Creates a new object """
        session = PostgreConnection.get_session()
        session.add(object)
        session.commit()

    @staticmethod
    def update(object):
        """ Updates an object """
        session = PostgreConnection.get_session()
        session.merge(object)
        session.commit()

    @staticmethod
    def delete(object):
        """ Removes an object """
        session = PostgreConnection.get_session()
        session.delete(object)
        session.commit()
