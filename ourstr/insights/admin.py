


from django.contrib import admin
from .models import AdminMessage, Comment

class AdminMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'likes', 'dislikes', 'reaction_mode_display')
    search_fields = ('content',)
    list_filter = ('reaction_mode',)  # Allows filtering by reaction_mode

    # Custom method to display the reaction type (text or like/dislike)
    def reaction_mode_display(self, obj):
        # Check the reaction mode and return a custom label
        if obj.reaction_mode == 'like_dislike':
            return "Like/Dislike"
        elif obj.reaction_mode == 'text':
            return "Text Suggestion"
        return "Unknown"

    # Optional: Add custom method for sorting or more customization if needed
    reaction_mode_display.short_description = 'Reaction Type'  # Custom label for this column

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'content', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(AdminMessage, AdminMessageAdmin)
admin.site.register(Comment, CommentAdmin)
