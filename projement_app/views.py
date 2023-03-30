from django.db import transaction
from django.db.models import F

from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from projement.pagination import StandardResultsSetPagination
from .serializers import ProjectSerializer
from .models import Project


class GetAllProjectsView(ListAPIView):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by("-end_date") # order by end date in decending order
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
    http_method_names = ['get', ]
    

class UpdateProjectView(UpdateAPIView):
   
    permission_classes = [IsAuthenticated,]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['patch', 'put', ]
    lookup_field = "pk"

    @transaction.atomic
    def update(self, request, *args, **kwargs):

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            
            # Incrementally update actual hours using the lock select for update method
            proj = Project.objects.select_for_update().get(id=instance.id)
            proj.actual_hours += serializer.validated_data['actual_hours']
            proj.save()
            
            serializer = self.serializer_class(proj, many=False)
            
            return Response({"status": "success", "data": serializer.data},  status=status.HTTP_200_OK)
        