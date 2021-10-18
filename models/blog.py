from sqlalchemy import Table, Column, Integer, String
from config.db import meta

blogs = Table(
    'blogs', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(255)),
    Column('slug', String(255)),
    Column('description', String(255)),
)