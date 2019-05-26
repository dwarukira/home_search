import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from graphene_django.types import DjangoObjectType, ObjectType  
from django.contrib.auth import get_user_model

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())
    viewer = graphene.Field(UserType)

    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return get_user_model().objects.get(pk=id)
        
        return None


    
    @login_required
    def resolve_viewer(self, info, **kwargs):
       
        return info.context.user



class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)



class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()

