# Generated by Django 3.0.8 on 2020-07-13 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_question_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_info', to='accounts.Quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
