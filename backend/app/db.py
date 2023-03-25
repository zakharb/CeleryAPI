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
        DB manager

"""

import aiopg

# Connect to the database

async def init_postgres():
    global postgres_pool
    postgres_pool = await aiopg.create_pool(
        host='db',
        port=5432,
        user='postgres',
        password='postgres',
        database='postgres'
    )

# Define the startup event handler function to create the table
async def create_table():
    async with postgres_pool.acquire() as conn:
        async with conn.cursor() as cur:
            # Execute a CREATE TABLE statement
            query = 'CREATE TABLE IF NOT EXISTS articles (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, description TEXT)'
            await cur.execute(query)
