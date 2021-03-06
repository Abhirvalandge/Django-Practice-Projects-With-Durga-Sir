# Generated by Django 3.1.5 on 2021-02-11 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_contactinfo1_multi_student1_multi_teacher1_multi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent_Multilevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb1', models.CharField(max_length=64)),
                ('fb2', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Child_Multilevel',
            fields=[
                ('parent_multilevel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='miApp.parent_multilevel')),
                ('fb3', models.CharField(max_length=64)),
                ('fb4', models.CharField(max_length=64)),
            ],
            bases=('miApp.parent_multilevel',),
        ),
        migrations.CreateModel(
            name='Sub_Child_Multilevel',
            fields=[
                ('child_multilevel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='miApp.child_multilevel')),
                ('fb5', models.CharField(max_length=64)),
            ],
            bases=('miApp.child_multilevel',),
        ),
    ]