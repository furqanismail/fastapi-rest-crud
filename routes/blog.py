from fastapi import APIRouter

import response
from config.db import conn
from models.index import blogs
from schemas.index import Blog
from transformer import BlogTransformer
blog = APIRouter()

@blog.get("/")
async def read_data():
    try:
        blog_data = conn.execute(blogs.select()).fetchall()
        # return conn.execute(blogs.select()).fetchall()
        transformer = BlogTransformer.transform(blog_data)
        return response.ok(transformer, "")
    except Exception as e:
        return response.badRequest('', f'{e}')


@blog.get("/{id}")
async def read_data(id : int):
    return conn.execute(blogs.select().where(blogs.c.id == id)).fetchall()

@blog.post("/")
async def write_data(blog: Blog):
    conn.execute(blogs.insert().values(
        title = blog.title,
        slug = blog.slug,
        description = blog.description
    ))
    return conn.execute(blogs.select()).fetchall()

@blog.put("/{id}")
async def update_data(id:int, blog: Blog):
    conn.execute(blogs.update().values(
        title=blog.title,
        slug=blog.slug,
        description=blog.description
    ).where(blogs.c.id == id))
    return conn.execute(blogs.select()).fetchall()

@blog.delete("/{id}")
async def delete_data(id: int):
    conn.execute(blogs.delete().where(blogs.c.id == id))
    return conn.execute(blogs.select()).fetchall()