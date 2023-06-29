from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
class UserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        exclude = [
            'password',
            'last_login',
            'date_joined',
            'groups',
            'user_permissions',
        ]

    def validate(self, attrs):
        data = self.context['request'].data
        if 'password' in data:
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password

            password = data['password']
            print(data)
            validate_password(password)
            attrs.update(
                {
                    'password': make_password(password)
                }
            )
        return super().validate(attrs)