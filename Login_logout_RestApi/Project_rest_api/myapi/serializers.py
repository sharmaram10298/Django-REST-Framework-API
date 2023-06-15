from rest_framework import serializers
from .models import Employee

# Model Serializers start

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# Model Serializers end
    
    
    
    
    
    
    
    
# class EmployeeSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=100)
    # email = serializers.EmailField()
    # age = serializers.CharField(max_length=100)
    # gender = serializers.CharField(max_length=100)
    # phone_number = serializers.CharField(max_length=100)
    # education = serializers.CharField(max_length=500)
    # address = serializers.CharField(max_length=500, default='Borivali')
    # city = serializers.CharField(max_length=100)
    # state = serializers.CharField(max_length=500)
    # pincode = serializers.CharField(max_length=100, default='400103')
    # country = serializers.CharField(max_length=500, default='India')
    # salary_annul_ctc = serializers.CharField(max_length=500, default='3Lpa')
    
    # # data creat method
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)
    
    
    # # data update method
    
    # def update(self, instance, validated_data):
    
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.education = validated_data.get('education', instance.education)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.state = validated_data.get('state', instance.state)
    #     instance.pincode = validated_data.get('pincode', instance.pincode)
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.salary_annul_ctc = validated_data.get('salary_annul_ctc', instance.salary_annul_ctc)
    #     instance.save()
    #     return instance
    
    
    # def validate_phone_number(self, value):
    #     if not value.isdigit() or len(value) != 10:
    #         raise serializers.ValidationError("Phone number should be a 10-digit number.")
    #     return value
