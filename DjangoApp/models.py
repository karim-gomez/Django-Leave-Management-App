from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True )
    phone_no=models.IntegerField(null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class leaveReport(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    leave_date=models.CharField(max_length=255)
    leave_message=models.TextField()
    leave_reply=models.TextField(default='null')
    leave_status=models.CharField(max_length=50, default="pending")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.customer.user.username