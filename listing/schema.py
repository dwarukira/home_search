import graphene
from graphene_django.types import DjangoObjectType, ObjectType  
from listing.models import Listing, Contact
from graphql_jwt.decorators import user_passes_test


class ListingType(DjangoObjectType):
    class Meta:
        model = Listing


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact




class Query(ObjectType):
    listings = graphene.List(ListingType)
    listing = graphene.Field(ListingType, id=graphene.Int())


    def resolve_listings(self, info, **kwargs):
        return Listing.objects.all()


    def resolve_listing(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Listing.objects.get(pk=id)
        
        return None
    


class ListingInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    desc = graphene.String()
    sqft = graphene.Float()
    bed_rooms = graphene.Int(required=True)
    address = graphene.String()
    price = graphene.Float(required=True)
    garage = graphene.Boolean()
    is_pub = graphene.Boolean()
    bathroom = graphene.Float()

class CreateListing(graphene.Mutation):
    class Arguments:
        input = ListingInput()
    
        
    
    listing = graphene.Field(ListingType)


    @staticmethod
    @user_passes_test(lambda user: user.is_realtor)
    def mutate(root, info, input=None):
        listing = Listing.objects.create(
            title = input.title,
            desc = input.desc,
            sqft = input.sqft,
            bed_rooms = input.bed_rooms,
            address = input.address,
            price = input.price,
            garage = input.garage,
            is_pub = input.is_pub,
            realtor = info.context.user,
            bathroom = input.bathroom
        )

        return CreateListing(listing=listing)

# TODO create a mutation class in it's own file
class Mutation(ObjectType):
    create_listing = CreateListing.Field()
