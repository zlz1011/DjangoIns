from django.db import models
#第三方库
#django model type
from imagekit.models import ProcessedImageField
# Create your models here.
#models.Model的子类
class Post(models.Model):
    title = models.TextField(blank=True,null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format= 'JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )