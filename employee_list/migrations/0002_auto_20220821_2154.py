# Generated by Django 3.2.8 on 2022-08-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='candidate_id',
        ),
        migrations.AddField(
            model_name='candidate',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='candidate',
            name='work_experience',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='aadhaar',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='father_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='highest_degree',
            field=models.CharField(choices=[('None', 'None'), ('Matriculate', 'Matriculate'), ('Intermediate', 'Intermediate'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Doctoral', 'Doctoral')], default='None', max_length=255),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(default='Applied', max_length=255),
        ),
    ]
