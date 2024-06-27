from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Password, Service
from .serializers import PasswordSerializer


class PasswordViewSet(viewsets.ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
    lookup_field = "service_name"
    lookup_url_kwarg = "service_name"

    def get_queryset(self):
        part_of_service_name = self.request.query_params.get("service_name")
        if part_of_service_name:
            services = Service.objects.filter(
                name__icontains=part_of_service_name
            )
            return Password.objects.filter(service_name__in=services)
        return super().get_queryset()

    def get_object(self):
        service_name = self.kwargs.get(self.lookup_url_kwarg)
        try:
            service = Service.objects.get(name=service_name)
            password = Password.objects.get(service_name=service)
            return password
        except Service.DoesNotExist:
            raise NotFound("Service not found")
        except Password.DoesNotExist:
            raise NotFound("Password not found")

    def create(self, request, service_name=None):
        if service_name:
            request.data["service_name"] = service_name
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
