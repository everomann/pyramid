from sqlalchemy import engine_from_config
from crud_pyramid.models.user_model import Base

def initialize_database(settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    from pyramid.paster import get_appsettings
    settings = get_appsettings('development.ini')
    initialize_database(settings)
