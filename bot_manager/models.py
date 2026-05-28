from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название трека")
    artist = models.CharField(max_length=255, verbose_name="Исполнитель")
    url = models.URLField(verbose_name="Прямая ссылка (Google Drive/S3)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Музыкальный трек"
        verbose_name_plural = "Музыкальные треки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.artist} - {self.title}"