from django.db import models

# Create your models here.
class printTask(models.Model):
    Id=models.IntegerField()
    PayMoney=models.IntergerField()
    Payed=models.IntergerField()
    PrintStatus=models.IntergerField() #0 is waiting ,1 is printing,2 is over
    create_date = models.DateTimeField('任务提交时间', default=timezone.now)
    over_date = models.DateTimeField('任务结束时间', default=timezone.now)
    UserLeavedMessage=models.CharField()
    UserLeavedPhone=models.CharField()