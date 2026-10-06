from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name = "Адміністратор"
        verbose_name_plural = "Адміністратори"

    def __str__(self):
        return f"{self.username} - Адмін Charwood.Chalet"
