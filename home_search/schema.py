import graphene  
import listing.schema
import authentication.schema

class Query(listing.schema.Query, authentication.schema.Query, graphene.ObjectType):
    pass

class Mutation(authentication.schema.Mutation,listing.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)