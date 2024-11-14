

from django.shortcuts import render, redirect, get_object_or_404
from .models import AdminMessage, Comment, Reaction
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

@login_required
def insight_view(request):
    # Automatically delete expired messages
    AdminMessage.objects.filter(is_visible=True, created_at__lt=timezone.now() - timedelta(days=14)).delete()

    # Fetch messages ordered by the latest first
    messages = AdminMessage.objects.filter(is_visible=True).order_by('-created_at')

    # Track whether a user has reacted to a message
    reacted_messages = {}
    if request.user.is_authenticated:
        # Check each message to see if the user has reacted
        for message in messages:
            reacted_messages[message.id] = Reaction.objects.filter(user=request.user, message=message).first()

    if request.method == "POST":
        # Handling new admin message (only for admin users)
        if 'admin_message' in request.POST and request.user.is_staff:
            content = request.POST['admin_message']
            reaction_mode = request.POST.get('reaction_mode', 'like_dislike')  # Default mode
            AdminMessage.objects.create(content=content, reaction_mode=reaction_mode)
            return redirect('insight')

        # Handling comment posting (user commenting on admin message)
        elif 'comment' in request.POST:
            message_id = request.POST['message_id']
            message = get_object_or_404(AdminMessage, id=message_id)

            if message.reaction_mode != 'like_dislike':  # Allow comment if it's not "like/dislike" mode
                content = request.POST['comment']
                Comment.objects.create(message=message, user=request.user, content=content)
                return redirect('insight')

        # Handling like/dislike reactions
        elif 'reaction_type' in request.POST:
            message_id = request.POST['message_id']
            reaction_type = request.POST['reaction_type']
            message = get_object_or_404(AdminMessage, id=message_id)

            # Get the user's existing reaction
            existing_reaction = Reaction.objects.filter(user=request.user, message=message).first()

            if existing_reaction:
                # User has already reacted, so adjust the counts based on the new reaction
                if existing_reaction.reaction_type == reaction_type:
                    # The user clicked the same reaction (no change)
                    return redirect('insight')
                else:
                    # User clicked the opposite reaction (switch reactions)
                    if reaction_type == 'like':
                        message.likes += 1
                        message.dislikes -= 1
                    elif reaction_type == 'dislike':
                        message.dislikes += 1
                        message.likes -= 1

                    # Update the existing reaction record
                    existing_reaction.reaction_type = reaction_type
                    existing_reaction.save()

            else:
                # User has not reacted yet, so add a new reaction
                if reaction_type == 'like':
                    message.likes += 1
                elif reaction_type == 'dislike':
                    message.dislikes += 1

                # Create the user's reaction record
                Reaction.objects.create(user=request.user, message=message, reaction_type=reaction_type)

            message.save()
            return redirect('insight')  # After handling the reaction, refresh the page

    return render(request, 'insight.html', {'messages': messages, 'reacted_messages': reacted_messages})










