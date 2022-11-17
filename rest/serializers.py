from rest_framework import serializers
from django.contrib.auth.models import User

from education_app.models import Work, Assessment

# Create your serializers here.
class WorkSerializer(serializers.ModelSerializer):
    assessments = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='score'
    )

    class Meta:
        model = Work
        fields = ['id', 'name', 'description', 'assessments']


    # name = serializers.CharField(
    #     max_length=80,
    #     help_text='Название практической работы',
    # )
    # description = serializers.CharField(
    #     required=False,
    #     help_text='Описание практической работы',
    # )
    #
    # def create(self, validated_data):
    #     return Work.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance

    # Своя валидация
    def validate_name(self, value):
        if 'плохое название работы' in value.lower():
            raise serializers.ValidationError('Работа не может иметь плохое название!')
        return value

    def validate_description(self, value):
        if len(value) == 10:
            raise serializers.ValidationError('Не круто иметь 10 символов в описании!')
        return value


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name', 'email', 'is_active']
        # Либо fields, либо exclude
        # exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']
        # fields = '__all__' // показывает все поля


# class AssessmentSerializer(serializers.HyperlinkedModelSerializer):
class AssessmentSerializer(serializers.ModelSerializer):
    # Вот так работает по умолчанию:
    # work = serializers.PrimaryKeyRelatedField(read_only=True)
    # student = serializers.PrimaryKeyRelatedField(read_only=True)
    # teacher = serializers.PrimaryKeyRelatedField(read_only=True)

    # Можно оставить одни названия
    # work = serializers.StringRelatedField()
    # student = serializers.StringRelatedField()
    # teacher = serializers.StringRelatedField()

    # Вместо названий можно сделать ссылки
    # work = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='works-detail'
    # )
    # student = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='user-detail'
    # )
    # teacher = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='user-detail'
    # )

    # Можно обеспечить вложенность
    work = WorkSerializer()
    student = UserSerializer()
    teacher = UserSerializer()

    class Meta:
        model = Assessment
        fields = ['score', 'comment', 'work', 'student', 'teacher']