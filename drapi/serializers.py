from rest_framework import serializers
from .models import Aiquest
# -------second approach-----
class AiquestsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aiquest
        fields='__all__'

# -------first approach-----
# class AiquestsSerializer(serializers.Serializer):
#     teacher_name=serializers.CharField(max_length=20)
#     course_name=serializers.CharField(max_length=20)
#     course_duration=serializers.IntegerField()
#     seat=serializers.IntegerField()
    
#     #deSerializer
#     def create(self,validated_data):
#         return Aiquest.objects.create(**validated_data ) #create function ke call korle Aiquest je model sekhane object/model instanse create hobe ebong validated_data mane user je datagula dibe oigula cleanned data check korar pasapsi models instanse e data gulo save hobe
#     def update(self,instance,validated_data):
#         instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)#instance ekhane models instance er datagula niya kaj korbe
#         instance.course_name = validated_data.get('course_name', instance.course_name)
#         instance.course_duration = validated_data.get('course_duration', instance.course_duration)
#         instance.seat = validated_data.get('seat', instance.seat)
#         #ekhane sob gulo instanse model er data gulo updated kore ditam jodi validated_data.get er maddhome jodi kono update pay tahole sei data update korbe otherwise korbe na, jemon temon ei thakbe
#         instance.save() #shese amar update data gulo save korlam
#         return instance