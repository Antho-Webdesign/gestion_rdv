from django.shortcuts import render

from plyer import notification


def send_notification(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')
        notification.notify(title=title, message=message, timeout=5)

    return render(request, 'notifications/send_notification.html')
