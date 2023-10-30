from django.db import models


class MenuItem(models.Model):
    title = models.CharField(
        max_length=100
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(
        default=0
    )
    url = models.URLField(
        max_length=200,
        blank=True
    )
    url_name = models.CharField(
        max_length=200,
        blank=True,
        help_text='Используйте именованный URL или явный URL.'
    )
    name = models.CharField(
        max_length=100,
        unique=True
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
