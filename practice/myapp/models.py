from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.age}"

    # Optional: You could add validation to ensure age is greater than 0
    def clean(self):
        if self.age <= 0:
            raise ValidationError("Age must be a positive number.")

class FoodMenu(models.Model):
    item_name = models.CharField(max_length=255)  
    description = models.TextField() 
    price = models.DecimalField(max_digits=7, decimal_places=2)  
    image_url = models.URLField(max_length=5000)  # For external image URLs
    # OR Use ImageField for local image uploads:
    # image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return f"{self.item_name} - {self.price}"

    # Optional: You could add a `verbose_name` for clarity
    class Meta:
        verbose_name = "Food Menu Item"
        verbose_name_plural = "Food Menu Items"
