from core.models import BaseModel
from django.db import models


class UserModel(BaseModel):
    class Meta:
        db_table = 'users'

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
