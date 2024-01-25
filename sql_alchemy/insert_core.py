from sqlalchemy import insert

from db import engine
from create_table_core import user_table


stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
print(stmt)
with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
