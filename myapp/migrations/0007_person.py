# Generated by Django 2.1.1 on 2018-09-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20180906_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(default='NULL', max_length=20)),
                ('Pid', models.IntegerField()),
            ],
        ),
    ]
