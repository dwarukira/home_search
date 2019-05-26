import graphene
from graphene_django.types import DjangoObjectType, ObjectType  
import listing.models import Listing, Contact

class ListingType(DjangoObjectType):
    class Meta:
        model = Listing


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact




class Query(ObjectType):
    listings = graphene.List(ListingType)
    
