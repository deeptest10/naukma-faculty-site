from django.db import migrations, models


def convert_places(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")

    for program in ExchangeProgram.objects.all():
        text = program.places.strip()
        program.places_is_limit = text.startswith("до ")

        for word in text.split():
            if word.isdigit():
                program.places = str(int(word))
                break
        else:
            raise ValueError(f"Невідомий формат кількості місць: {text}")

        program.save()


def restore_places(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")

    for program in ExchangeProgram.objects.all():
        if program.places_is_limit:
            program.places = f"до {program.places}"
        else:
            program.places = str(program.places)

        program.save()


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0003_split_university_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="places_is_limit",
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(convert_places, restore_places),
        migrations.AlterField(
            model_name="exchangeprogram",
            name="places",
            field=models.PositiveIntegerField(),
        ),
    ]