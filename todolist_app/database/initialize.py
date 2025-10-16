# https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls
#  sqlite://<nohostname>/<path>
# where <path> is relative:
from .models import Base
from .connectivity import engine

# wont do anything if the db already exists
Base.metadata.create_all(bind=engine)