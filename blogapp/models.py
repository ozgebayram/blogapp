from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ("name",)



class Post(models.Model):
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  content = models.TextField(blank=True, max_length=100, null=True)
  status = models.BooleanField(default=False)
  created_data = models.DateTimeField(auto_now_add=True)
  updated_data = models.DateTimeField(auto_now=True)
  

def __str__(self):
  return f"{self.title} {self.content}"

class Meta:
  ordering=("title",) #burası itrable olmalıdır