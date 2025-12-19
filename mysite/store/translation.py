from .models import UserProfile, Country, City, Amenity, Property, Review
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Amenity)
class AmenityTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)