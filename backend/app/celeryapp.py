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
        Task creation with Celery 

"""
from celery import Celery
import os
import psycopg2
from celery import group

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

@celery.task()
def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    meta_tag = soup.find_all('meta', {'name': 'description'})
    if not title or not meta_tag:
        return None
    save_to_db(title, description)

def save_to_db(title, description):
    description =  meta_tag[0].get('content')
    conn = psycopg2.connect(
        host='db',
        port=5432,
        user='postgres',
        password='postgres',
        database='postgres'
    )
    cursor = conn.cursor()
    cursor.execute('INSERT INTO articles (title, description) VALUES (%s, %s)', (title, description))
    conn.commit()
    cursor.close()
    conn.close()

def scrape_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    data = []
    for link in links:
        if '#' in link:
            continue
        if 'https' not in link:
            link = url + link
        data.append(link)
    return data

def scrape_and_save(url="https://bbc.com"):
    links = scrape_links(url)[:10]
    tasks = group(scrape.s(link) for link in links)
    results = tasks()
    articles = results.get()
    return tasks

postgres_conn = psycopg2.connect(
    host='db',
    port=5432,
    user='postgres',
    password='postgres',
    database='postgres'
)