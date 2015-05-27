from rest_framework import serializers

import pdb

from .models import *
from authentication.serializers import AccountSerializer

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=128, use_url=True,)
    class Meta:
        model = Image
        fields = ('title', 'image', 'brew', 'brewery')

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

class BrewDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrewDate
        fields = ('brew', 'date', 'activity')

    def create(self, validated_data):
        return BrewDate.objects.create(**validated_data)

class BrewerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Brewery
        fields = ('id', 'name', 'description')
        read_only_fields = ('id')

        def create(self, validated_data):
            return Brewery.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)

            instance.save()
            return instance

        def get_validation_exclusions(self, *args, **kwargs):
            exclusions = super(BrewerSerializer, self).get_validation_exclusions()

            return exclusions + ['brewery','user']

class BrewerSerializer(serializers.ModelSerializer):
    brewery = BrewerySerializer(read_only=True, required=False)
    user = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Brewer
        fields = ('id', 'brewery', 'user')
        read_only_fields = ('id')

        def create(self, validated_data):
            return Brewer.objects.create(**validated_data)

        def get_validation_exclusions(self, *args, **kwargs):
            exclusions = super(BrewerSerializer, self).get_validation_exclusions()

            return exclusions + ['brewery','user']

class BrewSerializer(serializers.ModelSerializer):
    brewer = BrewerSerializer(read_only=True, required=False)
    images = ImageSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Brew
        fields = ('id', 'name', 'description', 'style', 'type', 'abv', 'brewer', 'images')
        read_only_fields = ('id')

        def create(self, validated_data):
            return Brew.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)

            instance.save()
            return instance
        def get_validation_exclusions(self, *args, **kwargs):
            exclusions = super(BrewSerializer, self).get_validation_exclusions()
            return exclusions + ['brewer']

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id', 'tasting', 'category', 'key')
        read_only_fields = ('id')

        def create(self, validated_data):
            return Keyword.objects.create(**validated_data)

class TastingSerializer(serializers.ModelSerializer):
    brew = BrewSerializer(required=False, read_only=True)
    #brewId = serializers.
    user = AccountSerializer(required=False, read_only=True)
    keywords = KeywordSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Tasting
        fields = ('id', 'brew', 'user', 'appearance', 'smell', 'taste', 'mouthfeel', 'overall', 'keywords')
        read_only_fields = ('id')
        extra_kwargs = {'brew_id': {'write_only': True}}

        def create(self, validated_data):
            pdb.set_trace()
            brew_id = validated_data.pop('brew_id')
            brew = Brew.objects.get(id=brew_id)
            return Tasting.objects.create(brew=brew, **validated_data)

        def update(self, instance, validated_data):
            instance.appearance = validated_data.get('appearance', instance.appearance)
            instance.smell = validated_data.get('smell', instance.smell)
            instance.taste = validated_data.get('taste', instance.taste)
            instance.mouthfeel = validated_data.get('mouthfeel', instance.mouthfeel)
            instance.overall = validated_data.get('overall', instance.overall)
            instance.keywords = validated_data.get('keywords', instance.keywords)

            instance.save()
            return instance
