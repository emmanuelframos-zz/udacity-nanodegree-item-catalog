from database.postgre_connection import PostgreConnection


class DAO:
    """
    Class that represents the Data Access Object pattern in a simple way
    """

    @staticmethod
    def session():
        return PostgreConnection.get_session()

    @staticmethod
    def find(cls, **args):
        session = PostgreConnection.get_session()
        one_result = session.query(cls).filter_by(**args).one()
        session.expunge(one_result)
        return one_result

    @staticmethod
    def find_all(cls):
        session = PostgreConnection.get_session()
        return session.query(cls).all()

    @staticmethod
    def create(object):
        session = PostgreConnection.get_session()
        session.add(object)
        session.commit()

    @staticmethod
    def update(object):
        session = PostgreConnection.get_session()
        session.merge(object)
        session.commit()

    @staticmethod
    def delete(object):
        session = PostgreConnection.get_session()
        session.delete(object)
        session.commit()