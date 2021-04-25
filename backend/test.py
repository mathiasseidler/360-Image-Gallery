from sqlalchemy.sql.sqltypes import NULLTYPE
from sql_app import models

a = models.Project(title='asdf')
print(a.title)
