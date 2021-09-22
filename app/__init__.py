from config.db import Base, engine

from .auth import routes as auth_routes
from .auth.models import *

from .default import routes as default_routes
from .default.models import *

from .upload import routes as upload_routes
from .upload.models import *


def create_data():
    Base.metadata.create_all(bind=engine)


def register_all_routes(app):
    default_routes.register_routes(app)
    auth_routes.register_routes(app)
    upload_routes.register_routes(app)
