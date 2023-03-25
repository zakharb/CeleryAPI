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
        API to work with Celery library using FastAPI
        Parse url with celery tasks
        Also run Celery tasks in cron

"""

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from app.celeryapp import celery

from app.routes import router
from app.db import init_postgres, create_table


app = FastAPI()
logger = get_task_logger(__name__)

@app.on_event('startup')
async def startup_event():
    await init_postgres()
    await create_table()

app.include_router(router, prefix='/api/v1/articles', tags=['articles'])

# Define the Celery beat schedule
celery.conf.beat_schedule = {
    'scrape-every-hour': {
        'task': 'tasks.scrape_and_save',
        'schedule': crontab(minute=0, hour='*/1')
    },
}
