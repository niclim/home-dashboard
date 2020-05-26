from flask import Blueprint

routes = Blueprint("routes", __name__)

from .example import *  # noqa
from .to_do_list import *  # noqa
