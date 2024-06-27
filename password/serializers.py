from rest_framework import serializers
from .models import Password, Service


class PasswordSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source="service_name.name")
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Password
        fields = ["service_name", "password"]

    def create(self, validated_data):
        service_name_data = validated_data.pop("service_name")
        service_name = service_name_data["name"]
        raw_password = validated_data.pop("password")
        service, created = Service.objects.get_or_create(name=service_name)
        password_instance, created = Password.objects.get_or_create(
            service_name=service
        )
        password_instance.encrypted_password = raw_password
        password_instance.save()
        return password_instance

    def update(self, instance, validated_data):
        raw_password = validated_data.get(
            "password", instance.encrypted_password
        )
        instance.encrypted_password = raw_password
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["password"] = instance.get_decrypted_password()
        return representation
