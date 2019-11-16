from rest_framework import serializers
from .models import SpProduct,SpDivision,SpCategory,SpSubCategory


class SpProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpProduct
        fields = "__all__"

class SpDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpDivision
        fields = "__all__"

class SpCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpCategory
        fields = "__all__"

class SpSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpSubCategory
        fields = "__all__"