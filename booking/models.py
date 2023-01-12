import uuid

from django.db import models


# Create your models here.
class Bus(models.Model):
    bus_name = [
        ("RAIPUR", 'RAIPUR'),
        ("AMBIKAPUR", 'AMBIKAPUR'),
    ]
    bus_name = models.CharField(max_length=25, choices=(("volvo", 'volvo'), ("mahindra", 'mahindra')))
    bus_number = models.CharField(max_length=30, default="")
    driver_name = models.CharField(max_length=50, default="")
    seats = models.IntegerField()
    available = models.BooleanField(default=True)
    onward_date = models.DateField()
    return_date = models.DateField()


class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    bus = models.ForeignKey(Bus, models.CASCADE)
    seat_number = models.IntegerField()


class Route(models.Model):
    BUSFROM = (
        ('Delhi', 'Delhi'),
        ('Jaipur', 'Jaipur'),
        ('Ajmer', 'Ajmer'),
    )
    BUSTO = (
        ('Ajmer', 'Ajmer'),
        ('Chandigarh', 'Chandigarh'),
        ('Delhi', 'Delhi'),
    )
    route_id = models.AutoField(primary_key=True, )
    location_from = models.CharField(max_length=255, choices=BUSFROM)
    location_to = models.CharField(max_length=255, choices=BUSTO)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.FloatField()
    total_time = models.FloatField()


class Booking(models.Model):
    class Meta:
        verbose_name_plural = "Booking"

    # user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=(('Mr', 'mr'), ('Mrs', 'mrs'), ('Ms', 'ms'),))
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    route = models.ForeignKey(Route, models.CASCADE)

    def __str__(self):
        return self.name


def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1]  # generate unique ticket id


class Ticket(models.Model):
    ticket_id = models.CharField(max_length=255, blank=True)
    booking = models.ForeignKey(Booking, models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.ticket_id)

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" ")) == 0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs)  # Call the real   save() method

    class Meta:
        ordering = ["-created"]
