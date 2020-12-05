# Generated by Django 3.1.4 on 2020-12-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_title', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poem_timestamp', models.DateTimeField(auto_now_add=True)),
                ('poem_title', models.CharField(help_text='enter poem title', max_length=48)),
                ('poem_text', models.CharField(help_text='enter poem text', max_length=280)),
                ('links', models.ManyToManyField(related_name='_poem_links_+', to='library.Poem')),
                ('poetry_genres', models.ManyToManyField(blank=True, to='library.Genre')),
            ],
        ),
    ]
