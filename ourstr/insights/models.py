

from django.db import models
from django.contrib.auth.models import User

class AdminMessage(models.Model):
    REACTION_MODES = [
        ('like_dislike', 'Like/Dislike'),
        ('text', 'Text Suggestions'),
    ]

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)
    reaction_mode = models.CharField(max_length=20, choices=REACTION_MODES, default='like_dislike')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.content

class Comment(models.Model):
    message = models.ForeignKey(AdminMessage, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.message.id}"

# New model to track user reactions (likes/dislikes)
class Reaction(models.Model):
    REACTION_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(AdminMessage, related_name='reactions', on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'message')  # Ensure a user can react only once to a message

    def __str__(self):
        return f"{self.user.username} reacted {self.reaction_type} to message {self.message.id}"






