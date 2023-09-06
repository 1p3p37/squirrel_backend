# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa

# from app.models.admin import Admin  # noqa
from app.models.user import User
from app.models.high_value import HighValue
from app.models.time_value import TimeValue

# from app.models.deposit import Deposit
