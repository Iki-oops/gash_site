from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db.models.constraints import UniqueConstraint

User = get_user_model()


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        'Дата создания',
        null=True,
        blank=True,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        null=True,
        blank=True,
        auto_now=True,
    )


class Tag(models.Model):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    name = models.CharField(
        verbose_name='Название',
        max_length=30,
    )

    hex_color = models.CharField(
        verbose_name='Цвет тега',
        help_text='Цвет тега в формате HEX',
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^#[a-zA-Z0-9]{3,8}$',
                message='Неправильный формат цвета'
            ),
        ]
    )

    def __str__(self):
        return self.name


class Course(TimeBasedModel):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    name = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Описание',
    )
    tags = models.ManyToManyField(
        Tag,
        through='CourseTag',
    )

    def __str__(self):
        return self.name


class CourseTag(models.Model):
    class Meta:
        verbose_name = 'Курс - тэг'
        verbose_name_plural = 'Курсы - тэги'
        constraints = [
            UniqueConstraint(
                fields=('course', 'tag'),
                name='unique_course_tag',
            )
        ]

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
    )

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тэг',
    )

    def __str__(self):
        return f'{self.course} - {self.tag}'
