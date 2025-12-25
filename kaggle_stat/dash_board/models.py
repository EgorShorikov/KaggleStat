from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL


class Contest(models.Model):
    '''Основная сущность соревнования Kaggle'''
    kaggle_id = models.CharField(
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


class KaggleUser(models.Model):
    '''Пользователь Kaggle'''
    user_name = models.CharField(
        verbose_name='Никнейм на платформе',
        max_length=50,
    )
    skill_level = models.CharField(
        verbose_name='Уровень мастерства',
        max_length=11,
        blank=True
    )
    registered = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True
    )
    contests = models.ManyToManyField(
        Contest,
        through='ParticipantContest'
    )


class ParticipantContest(models.Model):
    '''Участник соревнования'''
    contest_id = models.ForeignKey(
        Contest,
        on_delete=CASCADE
    )
    kaggle_user_id = models.ForeignKey(
        KaggleUser,
        on_delete=CASCADE
    )
    score = models.FloatField(
        verbose_name='Очки рейтинга',
        blank=True
    )
    position = models.IntegerField(
        verbose_name='Позиция в таблице лидеров',
    )
    submissions = models.IntegerField(
        verbose_name='Количество посылок',
    )
    last_submission = models.DateTimeField(
        verbose_name='Время последней отправки',
        auto_now=True
    )


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
