# Generated by Django 2.2.5 on 2019-09-25 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fooddb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='food',
            old_name='foodname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='food',
            name='foodcategory',
        ),
        migrations.CreateModel(
            name='Food_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddb.Category')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddb.Food')),
            ],
        ),
    ]