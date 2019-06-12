from ..database.db_manager import DatabaseManager


class ModelNews(object):

    def __init__(self, db_configuration):
        if isinstance(db_configuration, dict):
            self._db_conf = db_configuration
        else:
            raise TypeError('Provide a dict for db configuration')

    def get_all_news(self):
        query = 'SELECT * FROM news ORDER BY date DESC LIMIT 100;'
        with DatabaseManager(self._db_conf) as db:
            all_news = db.execute_query(query)

        return list(
            map(
                lambda record: dict(
                    id=record[0],
                    title=record[1],
                    description=record[2],
                    image=record[3],
                    url=record[4],
                    source=record[5],
                    date=record[6]
                ),
                all_news
            )
        )

    def get_news_by_id(self, id):
        query = 'SELECT * FROM news WHERE id = %s;'
        with DatabaseManager(self._db_conf) as db:
            input = (id,)
            news = db.execute_query(query, input)

        if len(news) == 0:
            return None
        else:
            news = news[0]
            return dict(
                id=news[0],
                title=news[1],
                description=news[2],
                image=news[3],
                url=news[4],
                source=news[5],
                date=news[6]
            )

    def create_news(self, news):
        pass

    def update_news_val(self, val):
        pass

    def delete_news_by_id(self, id):
        pass
