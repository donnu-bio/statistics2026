from notion_client import Client
from datetime import datetime
import os

import os
from dotenv import load_dotenv

load_dotenv()   # підхопить .env, якщо він є
NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID = os.environ.get("DATABASE_ID_STAT_GRADES")

if not NOTION_TOKEN or not DATABASE_ID:
    raise ValueError(
        "NOTION_TOKEN і DATABASE_ID не знайдені. "
        "Переконайтеся, що ви відкрили Codespace з репозиторію організації."
    )

notion = Client(auth=NOTION_TOKEN)

def submit_grade(name: str, lab_name: str, comment: str = "", results = None, show_grade: bool = True):

    if not name or not lab_name or results is None:
        raise ValueError("Ім'я, назва лабораторної роботи та оцінка обов'язкові.")

    grade = results.total/results.possible*100
    if show_grade:
        print("Ваш результат у %:", grade)
    
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Name": {
                "title": [{"text": {"content": name}}]
            },
            "Lab": {
                "rich_text": [{"text": {"content": lab_name}}]
            },            
            "Grade": {
                "number": grade
            },
            "Date": {
                "date": {"start": datetime.now().isoformat()}
            },
            "Comment": {
                "rich_text": [{"text": {"content": comment}}]
            },            
        }
    )
    print("Дані успішно відправлено викладачу!")