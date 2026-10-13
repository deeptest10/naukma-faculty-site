from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                INSERT INTO exchange_exchangeprogram
                (id, university, languages, places, deadline, description)
                VALUES
                (
                    1,
                    'Uniwersytet Warszawski, Польща',
                    'польська, англійська',
                    '5',
                    '2026-11-15',
                    'Навчальний обмін для студентів природничих спеціальностей.'
                ),
                (
                    2,
                    'KU Leuven (Бельгія)',
                    'English',
                    '2 місця',
                    '2026-12-01',
                    'Програма обміну з можливістю вивчення природничих дисциплін англійською мовою.'
                ),
                (
                    3,
                    'Vilnius University, Литва',
                    'англійська',
                    'до 4',
                    '2026-10-20',
                    'Програма академічної мобільності для навчання та знайомства з університетськими дослідженнями.'
                ),
                (
                    4,
                    'Uniwersytet Jagielloński, Польща',
                    'Польська, Англійська',
                    '3',
                    '2026-11-15',
                    'Студентський обмін із навчанням польською або англійською мовою.'
                ),
                (
                    5,
                    'University of Tartu - Естонія',
                    'англійська, естонська',
                    '2',
                    '2027-01-10',
                    'Навчання в університеті-партнері та участь у студентському академічному житті.'
                ),
                (
                    6,
                    'Masaryk University, Чехія',
                    'англійська',
                    '1 місце',
                    '2026-09-30',
                    'Програма обміну для поглиблення знань із природничих наук.'
                );
            """,
            reverse_sql="""
                DELETE FROM exchange_exchangeprogram
                WHERE id IN (1, 2, 3, 4, 5, 6);
            """,
        ),
    ]