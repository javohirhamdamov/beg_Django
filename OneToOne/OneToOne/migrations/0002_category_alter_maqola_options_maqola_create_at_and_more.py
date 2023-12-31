# Generated by Django 4.2.5 on 2023-09-26 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneToOne', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='maqola',
            options={'verbose_name': 'Maqola', 'verbose_name_plural': 'Maqolalar'},
        ),
        migrations.AddField(
            model_name='maqola',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='maqola',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
