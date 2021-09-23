from config.db import Base, engine
from .default import routes as default_routes
from .default.models import *
from .file import routes as upload_routes
from .file.models import *
from .oauth import routes as auth_routes
from .oauth.models import *


def create_data():
    Base.metadata.create_all(bind=engine)


def register_all_routes(app):
    default_routes.register_routes(app)
    auth_routes.register_routes(app)
    upload_routes.register_routes(app)
