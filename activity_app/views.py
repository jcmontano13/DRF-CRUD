from rest_framework import generics
from .models import Activity
from .serializers import ActivitySerializer


# ---------------------------------------------------------
# ActivityListCreateView
# Uses DRF's ListCreateAPIView which provides:
#   - GET  → list()    → List all Activity records
#   - POST → create()  → Create a new Activity record
# ---------------------------------------------------------
class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


# ---------------------------------------------------------
# ActivityDetailView
# Uses DRF's RetrieveUpdateDestroyAPIView which provides:
#   - GET     → retrieve() → Get a single Activity by ID
#   - PUT/PATCH → update() → Update an Activity
#   - DELETE  → destroy()  → Delete an Activity
# ---------------------------------------------------------
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer