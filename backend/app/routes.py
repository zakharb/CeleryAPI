"""
    CeleryAPI
    Copyright (C) 2023

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Author:
        Bengart Zakhar

    Description:
        Routes for FastAPI

"""

from fastapi import APIRouter
import aiopg

from app.celeryapp import scrape_and_save

router = APIRouter()

#routes
@router.post("/scrape_articles")
async def scrape_articles():
    tasks = scrape_and_save(url="https://bbc.com")
    return {"tasks": tasks}

# Define a new route to read the articles from the database
@router.get('/articles')
async def read_articles():
    postgres_pool = await aiopg.create_pool(
        host='db',
        port=5432,
        user='postgres',
        password='postgres',
        database='postgres'
    )
    async with postgres_pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute('SELECT title, description FROM articles')
            rows = await cur.fetchall()
    articles = []
    for row in rows:
        title, description = row
        articles.append({'title': title, 'description': description})
    return {'articles': articles}