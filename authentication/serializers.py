from rest_framework import serializers
from authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'photo', 'bio', 'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        isinstance = self.Meta.model(**validated_data)
        isinstance.is_active = True
        
        if password is not None:
            isinstance.set_password(password)
        isinstance.save()
            
        return isinstance