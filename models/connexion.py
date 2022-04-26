from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base



Base=declarative_base()
engine=create_engine('postgresql://groupe3:passer123@localhost/projet_flask')
