# Generated by Django 4.2 on 2023-04-25 15:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Строка должна соответствовать значению цвета в RGB', regex='(\\d+),\\s*(\\d+),\\s*(\\d+)')])),
                ('icon', models.ImageField(upload_to='workout/icon/')),
                ('initial_break', models.CharField()),
                ('playlist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='used_workout', to='music.playlistmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('time', 'Time'), ('repetitions', 'Repetitions')], max_length=11)),
                ('icon', models.ImageField(upload_to='workout/icon/')),
                ('break_between_approaches', models.CharField()),
                ('break_after_exercise', models.CharField()),
                ('number', models.PositiveIntegerField()),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='workout.workoutmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ApproachModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('break_after_approach', models.TimeField()),
                ('working_weight', models.IntegerField()),
                ('repetitions', models.IntegerField(null=True)),
                ('duration', models.CharField(null=True)),
                ('number', models.PositiveIntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.exercisemodel')),
            ],
        ),
    ]