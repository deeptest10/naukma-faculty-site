# Сайт факультету природничих наук НаУКМА

Проєкт на Django: головна сторінка, кафедри,
спеціальності та викладачі. Дані редагуються через адмінку

## Вибір факультету

Факультет має розділ на сайті НаУКМА. Посилання на окремий сайт
усьогг факультету не знайдено. Інформація про кафедри та програми
розміщена на різних сторінках, частина відомостей застаріла.

У проєкті зроблено спільне меню та переходи між кафедрами
і спеціальностями. Додано шість кафедр, чотири спеціальності
та вибірку викладачів.

Джерела:
- https://www.ukma.edu.ua/index.php/osvita/fakulteti/fprn
- https://vstup.ukma.edu.ua/education-programs
- https://vstup.ukma.edu.ua/education-program-info?ep-id=118
- https://vstup.ukma.edu.ua/education-program-info?ep-id=105
- https://vstup.ukma.edu.ua/education-program-info?ep-id=107
- https://vstup.ukma.edu.ua/education-program-info?ep-id=169

## Запуск у WSL / Linux

З кореня проєкту:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata faculty_data
python manage.py createsuperuser
python manage.py runserver
```

Сайт: http://127.0.0.1:8000/
Адмінка: http://127.0.0.1:8000/admin/

## Дані

Для головної сторінки створюється один запис FacultyInfo.
Наповненнч збережено у faculty/fixtures/faculty_data.json.

Після змін в адмінці оновити файл:

```bash
python manage.py dumpdata faculty --indent 2 -o faculty/fixtures/faculty_data.json
```

Міграції і фікстура зберігаються в Git, а база db.sqlite3 і .venv - ні.

## Програми обміну

Розділ /exchange/ показує програми академічного обміну. 
Шість записів завантажуються автоматично через міграцію RunSQL.
Наступні міграції відокремлюють країну та перетворюють кількість
місць на число. Статус прийому обчислюєтьсч за дедлайном