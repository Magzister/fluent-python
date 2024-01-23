from sqlalchemy import text

from db import engine
import insert_core


with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x} y: {row.y}")

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT x, y FROM some_table WHERE y > :y"),
        {"y": 2},
    )
    for row in result:
        print(f"x: {row.x} y: {row.y}")
