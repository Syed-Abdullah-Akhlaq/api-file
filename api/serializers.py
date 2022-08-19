from rest_framework import serializers
from .models import Students

class StudentSerializers(serializers.Serializer):
    Name = serializers.CharField(max_length=100)
    City = serializers.CharField(max_length=100)
    Age = serializers.IntegerField()
    Roll_Number =  serializers.IntegerField()
    School_Name = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.Name)
        instance.Name = validated_data.get('Name', instance.Name)
        print(instance.Name)
        instance.City = validated_data.get('City', instance.City)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.Roll_Number = validated_data.get('Roll_Number', instance.Roll_Number)
        instance.School_Name = validated_data.get('School_Name', instance.School_Name)
        instance.save()
        return instance
 