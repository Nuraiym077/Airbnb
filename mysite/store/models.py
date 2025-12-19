from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator




class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='avtar', null=True, blank=True)
    ROLE_CHOICES = (
        ('host', 'host'),
        ('guest', 'guest')
    )
    user_role = models.CharField(choices=ROLE_CHOICES, default='guest', max_length=10)
    phone_number = PhoneNumberField(null=True, blank=True)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return  f'{self.first_name}, {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=50, unique=True)
    country_image = models.ImageField(upload_to='country_image')

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icon', null=True, blank=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    amenity = models.ManyToManyField(Amenity)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    PROPERTY_TYPE_CHOICES = (
    ('apartment', 'apartment'),
    ('house', 'house'),
    ('studio', 'studio'),
    )
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    RULE_CHOICES = (
    ('no_smoking', 'no_smoking'),
    ('pets_allowed', 'pets_allowed'),
    )
    rule = models.CharField(max_length=50, choices=RULE_CHOICES)
    title = models.TextField()
    description = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                    MaxValueValidator(5)])
    host = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='host')

    def __str__(self):
        return f'{self.property_type}, {self.user}, {self.city}'

    def get_avg_rating(self):
        ratings = self.review.all()
        if ratings.exists():
            return round(sum([i.rating for i in ratings]) / ratings.count(), 1)
        return 0

    def get_count_people(self):
        return self.review.count()


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_image')
    image = models.ImageField(upload_to='property_image')

    def __str__(self):
        return f'{self.property}, {self.image}'


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField(null=True, blank=True)
    STATUS_CHOICES = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('rejected', 'rejected'),
    ('cancelled', 'cancelled'),
    )
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='review')
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)