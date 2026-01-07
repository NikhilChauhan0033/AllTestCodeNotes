from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from functools import wraps
import logging
from .models import Note
from django.http import JsonResponse

logger = logging.getLogger('my_app')


# Custom login-required decorator with message + log
def login_required_with_message(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            logger.warning("Unauthenticated user tried to access dashboard")
            messages.warning(request, "Please login to access the dashboard.")
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


def register_view(request):
    if request.user.is_authenticated:
        logger.info(f"Authenticated user {request.user.username} tried to access register page")
        return redirect('dashboard')

    try:
        if request.method == "POST":
            username = request.POST.get('username', '').strip()
            email = request.POST.get('email', '').strip()
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if not username or not password:
                logger.warning("Registration attempt with missing fields")
                messages.error(request, "All fields are required")
                return redirect('register')

            if password != confirm_password:
                logger.warning(f"Password mismatch during registration for {username}")
                messages.error(request, "Passwords do not match")
                return redirect('register')

            if User.objects.filter(username=username).exists():
                logger.warning(f"Registration attempt with existing username: {username}")
                messages.error(request, "Username already exists")
                return redirect('register')

            try:
                User.objects.create_user(username=username, email=email, password=password)
                logger.info(f"New user registered successfully: {username}")
                messages.success(request, "Registration successful. Please login.")
                return redirect('login')
            except Exception:
                logger.error("Error while creating new user", exc_info=True)
                messages.error(request, "Failed to create user. Please try again.")
                return redirect('register')

    except Exception:
        logger.error("Unexpected error during registration", exc_info=True)
        messages.error(request, "Something went wrong. Please try again.")

    return render(request, 'register.html')


def login_view(request):
    if request.user.is_authenticated:
        logger.info(f"Authenticated user {request.user.username} tried to access login page")
        return redirect('dashboard')

    try:
        if request.method == "POST":
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password')

            if not username or not password:
                logger.warning("Login attempt with missing fields")
                messages.error(request, "All fields are required")
                return redirect('login')

            try:
                user = authenticate(request, username=username, password=password)
                if user is None:
                    logger.warning(f"Failed login attempt for username: {username}")
                    messages.error(request, "Invalid username or password")
                    return redirect('login')

                login(request, user)
                logger.info(f"User logged in successfully: {username}")
                return redirect('dashboard')
            except Exception:
                logger.error("Error during user authentication", exc_info=True)
                messages.error(request, "Authentication failed. Please try again.")
                return redirect('login')

    except Exception:
        logger.error("Unexpected error during login", exc_info=True)
        messages.error(request, "Login failed. Please try again.")

    return render(request, 'login.html')


def logout_view(request):
    try:
        if request.user.is_authenticated:
            logger.info(f"User logged out: {request.user.username}")
        logout(request)
        messages.success(request, "You have been logged out successfully.")
    except Exception:
        logger.error("Error during logout", exc_info=True)
        messages.error(request, "Logout failed. Please try again.")
    return redirect('login')


@login_required_with_message
def dashboard_view(request):
    try:
        if request.method == "POST":
            title = request.POST.get('title', '').strip()
            description = request.POST.get('description', '').strip()

            if not title or not description:
                logger.warning("Missing fields while adding note")
                return JsonResponse({'success': False, 'message': 'All fields are required'})

            try:
                note = Note.objects.create(user=request.user, title=title, description=description)
                logger.info(f"Note created by {request.user.username}")
                return JsonResponse({
                    'success': True,
                    'note': {
                        'id': note.id,
                        'title': note.title,
                        'description': note.description,
                        'created_at': note.created_at.strftime('%Y-%m-%d %H:%M')
                    }
                })
            except Exception:
                logger.error("Error while creating note", exc_info=True)
                return JsonResponse({'success': False, 'message': 'Failed to create note'})

        try:
            notes = Note.objects.filter(user=request.user).order_by('-created_at')
        except Exception:
            logger.error("Error fetching notes", exc_info=True)
            notes = []
        return render(request, 'dashboard.html', {'notes': notes})

    except Exception:
        logger.error("Unexpected error in dashboard_view", exc_info=True)
        messages.error(request, "Something went wrong. Please try again.")
        return redirect('dashboard')


@login_required_with_message
def delete_note_view(request, note_id):
    try:
        if request.method == "POST":
            try:
                note = get_object_or_404(Note, id=note_id, user=request.user)
                note.delete()
                logger.info(f"Note deleted by {request.user.username}")
                return JsonResponse({'success': True})
            except Exception:
                logger.error("Error deleting note", exc_info=True)
                return JsonResponse({'success': False, 'message': 'Failed to delete note'})
    except Exception:
        logger.error("Unexpected error in delete_note_view", exc_info=True)
        return JsonResponse({'success': False, 'message': 'Something went wrong'})


@login_required_with_message
def edit_note_view(request, note_id):
    try:
        note = get_object_or_404(Note, id=note_id, user=request.user)

        if request.method == "POST":
            title = request.POST.get('title', '').strip()
            description = request.POST.get('description', '').strip()

            if not title or not description:
                logger.warning(f"User {request.user.username} tried to update note with empty fields")
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'message': 'All fields are required'})
                messages.error(request, "All fields are required")
                return redirect('edit_note', note_id=note.id)

            note.title = title
            note.description = description
            note.save()

            logger.info(f"User {request.user.username} updated note: {note.title}")

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'note': {
                        'id': note.id,
                        'title': note.title,
                        'description': note.description
                    }
                })

            messages.success(request, "Note updated successfully")
            return redirect('dashboard')

        return render(request, 'edit_note.html', {'note': note})

    except Exception:
        logger.error("Unexpected error in edit_note_view", exc_info=True)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'Something went wrong'})
        messages.error(request, "Something went wrong. Please try again.")
        return redirect('dashboard')