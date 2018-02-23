from django.db import models
from django.contrib.auth.models import AbstractUser
import json
# Create your models here.

class User(AbstractUser):
    # nickname = models.CharField(max_length=50, blank=True)
    job_monitor = models.TextField(blank=True)

    # 下面理论上起作用，只是不知道怎么调用。所以先用其他方法解决。
    def set_job_monitor(self,x):
        self.job_monitor = json.dumps(x)
    def get_job_monitor(self):
        return json.loads(self.job_monitor)

    class Meta(AbstractUser.Meta):
        pass


