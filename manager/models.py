from django.db import models


# Create your models here.
class UserReservations(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=500)
    order_date = models.TextField(max_length=11)
    order_time = models.TextField(max_length=6)
    num_of_people = models.SmallIntegerField()

    is_processed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return f"{self.name}, mob #: {self.phone}. Persons: {self.num_of_people}. " \
               f"Date: {self.order_date}, time: {self.order_time}, message: {self.message[:20]}. " \
               f"Status: {self.is_processed}"

