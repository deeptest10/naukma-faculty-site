from django.db import migrations, models


def split_country(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")

    for program in ExchangeProgram.objects.all():
        text = program.university

        if text.endswith(")") and "(" in text:
            university, country = text[:-1].rsplit("(", 1)
        elif " - " in text:
            university, country = text.rsplit(" - ", 1)
        else:
            university, country = text.rsplit(",", 1)

        program.university = university.strip()
        program.country = country.strip()
        program.save()


def join_country(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")

    for program in ExchangeProgram.objects.all():
        if not program.country:
            continue

        if program.country == "Бельгія":
            program.university = (
                f"{program.university} ({program.country})"
            )
        elif program.country == "Естонія":
            program.university = (
                f"{program.university} - {program.country}"
            )
        else:
            program.university = (
                f"{program.university}, {program.country}"
            )

        program.country = ""
        program.save()


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0002_add_exchange_programs"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="country",
            field=models.CharField(
                max_length=100,
                blank=True,
                default="",
            ),
        ),
        migrations.RunPython(split_country, join_country),
    ]