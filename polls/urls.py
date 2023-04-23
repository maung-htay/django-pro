from django.urls import path,include
from .views import polls_detail, polls_list, PollList,PollDetail, PollListGeneric, PollDetailGeneric, ChoiceList, CreateVote, UserCreate, LoginView
# from rest_framework.documentation import include_docs_urls

# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Polls API')
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="API documentation for My API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>", polls_detail, name="polls_detial"),
    
    # ApiView
    path("polls/api/", PollList.as_view(),name = "polls_list_api"),
    path("polls/api/<int:pk>", PollDetail.as_view(),name = "polls_detial_api"),
    
    # GenericView
    path("polls/generic/", PollListGeneric.as_view(),name = "polls_list_generic"),
    path("polls/generic/<int:pk>", PollDetailGeneric.as_view(),name = "polls_detial_generic"),
    
    # path("choices/", ChoiceList.as_view(),name = "choice_list"),
    # path("vote/", CreateVote.as_view(),name = "create_vote"),
    
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",CreateVote.as_view(), name="create_vote"),
    
    path("user/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    
    # path("swagger-docs/", schema_view),
    # path("swagger-docs/", include('rest_framework_swagger.urls'))
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    # path(r'docs/', include_docs_urls(title='Polls API')),
]
