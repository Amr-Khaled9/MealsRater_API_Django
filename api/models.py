from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def number_of_ratings(self):
        return self.ratings.count()

    def average_rating(self):
        ratings = self.number_of_ratings()
        if ratings > 0:
            return sum(rating.stars for rating in self.ratings.all()) / ratings
        return 0

    def __str__(self):
        return self.name

class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    comment = models.TextField(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rating {self.stars} for {self.meal.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['meal', 'user'],
                name='unique_meal_user'
            ),
        ]

        indexes = [
            models.Index(
                fields=['meal', 'user'],
                name='meal_user_index'
            ),
        ]