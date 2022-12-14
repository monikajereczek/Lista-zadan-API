# Generated by Django 4.0.6 on 2022-07-28 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listnotedetails',
            name='list_note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='app_to_do_list.listnote'),
        ),
        migrations.AlterField(
            model_name='note',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
