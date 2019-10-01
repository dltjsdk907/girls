from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 저자
    title = models.CharField(max_length=200)                                       # 제목
    text = models.TextField()                                                      # 내용
    created_date = models.DateTimeField(                                           # 작성일
            default=timezone.now)
    published_date = models.DateTimeField(                                         # 게시일
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
