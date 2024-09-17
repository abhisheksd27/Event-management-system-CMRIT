from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Admin').exists():
            return Event.objects.all()
        elif user.groups.filter(name='HOD').exists():
            return Event.objects.filter(...)
        elif user.groups.filter(name='Principal').exists():
            return Event.objects.filter(...)
        elif user.groups.filter(name='Students').exists():
            return Event.objects.filter(...)
        else:
            return Event.objects.none()
