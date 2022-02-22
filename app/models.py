from sqlalchemy.ext.automap import automap_base

from app.db import engine


Base = automap_base()
Base.prepare(engine, reflect=True)


Status = Base.classes.status

Ticket = Base.classes.ticket

FileGroup = Base.classes.accounts_filegroup

FileGroupUser = Base.classes.accounts_filegroupuser

MyUser = Base.classes.accounts_myuser

Organizations = Base.classes.accounts_organization
