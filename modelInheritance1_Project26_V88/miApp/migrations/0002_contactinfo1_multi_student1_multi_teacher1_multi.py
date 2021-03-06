# Generated by Django 3.1.5 on 2021-02-11 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo1_Multi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Student1_Multi',
            fields=[
                ('contactinfo1_multi_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='miApp.contactinfo1_multi')),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
            bases=('miApp.contactinfo1_multi',),
        ),
        migrations.CreateModel(
            name='Teacher1_Multi',
            fields=[
                ('contactinfo1_multi_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='miApp.contactinfo1_multi')),
                ('subject', models.CharField(max_length=128)),
                ('salary', models.IntegerField()),
            ],
            bases=('miApp.contactinfo1_multi',),
        ),
    ]