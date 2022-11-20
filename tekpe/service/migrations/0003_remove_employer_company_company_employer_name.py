# Generated by Django 4.1.3 on 2022-11-20 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_company_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='employer_name',
            field=models.ForeignKey(default=1, max_length=20, on_delete=django.db.models.deletion.CASCADE, to='service.employer', verbose_name='Ish beruvchi'),
            preserve_default=False,
        ),
    ]
