# Generated by Django 4.0.5 on 2022-06-12 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0009_profile_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_voted', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content_likes', to='awwards.project')),
                ('profile_vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awwards.profile')),
            ],
        ),
        migrations.CreateModel(
            name='DesignVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_voted', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='design_likes', to='awwards.project')),
                ('profile_vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awwards.profile')),
            ],
        ),
        migrations.CreateModel(
            name='UsabilityVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_voted', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usability_likes', to='awwards.project')),
                ('profile_vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awwards.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='PostVote',
        ),
    ]