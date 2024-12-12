## Migration

- To set up migrations run ''' alembic init migrations '''.We run this command once
- Modify alembic.ini '''sqlalchemy.url''' to the required db i.e test.db
- Modify env.py inside migrations folder and import base models from model files
- To create migrations ' alembic revision --autogenerate -m "message"'
- To apply the generate migrations, run "alembic upgrade head"
