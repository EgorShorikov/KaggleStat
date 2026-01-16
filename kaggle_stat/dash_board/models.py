from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL


class Contest(models.Model):
    '''Основная сущность соревнования Kaggle'''
    competition_slug = models.CharField(
        verbose_name='Уникальный идентификатор контеста',
        max_length=50,
        unique=True
    )
    title = models.CharField(
        verbose_name='Название соревнования',
        max_length=300
    )
    deadline = models.DateTimeField(
        verbose_name='Срок окончания',
        blank=True,
        auto_now_add=True
    )
    participant_count = models.IntegerField(
        verbose_name='Количество участников',
        blank=True
    )
    prize = models.CharField(
        verbose_name='Вознаграждение',
        max_length=20,
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=200,
        default=''
    )
    image_url = models.CharField(
        verbose_name='Ссылка на картинку',
        max_length=500,
        default=''
    )
    organization_name = models.CharField(
        verbose_name='Название организации, проводящей контест',
        max_length=200,
        default=''
    )
    organization_ref = models.CharField(
        verbose_name='Слаг организации',
        max_length=500,
        default=''
    )
    url = models.CharField(
        verbose_name='Ссылка на контест на кагле',
        max_length=500,
        default=''
    )

    def __str__(self):
        return f"{self.competition_slug}: {self.title}"

    class Meta:
        db_table = 'contest'


class Team(models.Model):
    '''Команда участник Kaggle'''
    team_slug = models.CharField(
        verbose_name='Название команды',
        max_length=50,
    )
    team_id = models.IntegerField(verbose_name='Айди команды')
    contests = models.ManyToManyField(Contest)

    class Meta:
        db_table = 'kaggle_team'


class LeaderBoard(models.Model):
    '''Таблица лидеров'''
    contest_id = models.ForeignKey(
        Contest,
        on_delete=CASCADE
    )
    saved_at = models.DateTimeField(
        verbose_name='Время сохранения таблицы',
        auto_now=True
    )
    data = models.JSONField(
        verbose_name='Данные лидерборда'
    )
    version = models.IntegerField(
        verbose_name='Версия записи позиций в лидерборде',
    )

    class Meta:
        db_table = 'leaderboard'
