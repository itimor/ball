# -*- coding: utf-8 -*-
# author: itimor

from users.models import User, Group, Role
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name', allow_null=True)
    roles = serializers.SlugRelatedField(queryset=Role.objects.all(), slug_field='name', allow_null=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'name', 'group', 'is_active', 'roles', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.group = validated_data.get('group', instance.group)
        instance.roles = validated_data.get('roles', instance.roles)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        try:
            instance.set_password(validated_data['password'])
        except:
            pass
        instance.save()
        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url','id', 'name', 'desc')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('url', 'id', 'name', 'cnname', 'desc')