from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class UserRank(models.TextChoices):
        S_RANK = 'S', 'S-rank'
        A_RANK = 'A', 'A-rank'
        B_RANK = 'B', 'B-rank'
        C_RANK = 'C', 'C-rank'
        D_RANK = 'D', 'D-rank'

    user_rank = models.CharField(max_length=1, choices=UserRank.choices, blank=True, null=False, default=UserRank.D_RANK)
    user_lvl = models.IntegerField(default=1, blank=True, null=False)
    avatar_img = models.CharField(max_length=255, blank=True, null=True)