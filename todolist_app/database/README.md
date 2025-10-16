run with 
`python -m todolist_app.database.initialize`

but should get familiar with https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

# TODO
## models
- recreate the SQLAlchemy initialization into a plain SQL for practice sake
- user_id_fk should not be nullable=True in all the tables
- transform all of this into a SQLscript
- rework the name of tables - conceptually it is better to have plural for table names
- rework the name of columns, especially PKs and FKs
- make a data model