from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from django.contrib.auth import authenticate

from rest_framework.exceptions import PermissionDenied


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"requests": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)


class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data)
    
class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data)   
    
 
 # Generic Views
class PollListGeneric(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    
class PollDetailGeneric(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer 
    
class ChoiceList(generics.ListCreateAPIView):
    # queryset = Choice.objects.all()
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    
    def post(self,request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs['pk'])
        if not request.user == poll.created_by: 
            raise PermissionDenied("Your can not choice for this poll")
        return super().post(request, *args, **kwargs)
    
    serializer_class = ChoiceSerializer
    
    
class CreateVote(APIView):
    # serializer_class = VoteSerializer  
    
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {"choice": choice_pk, "poll": pk, "voted_by": voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)   
        

class UserCreate(generics.CreateAPIView):
    authenticate_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
    
class LoginView(APIView):
    permission_classes = ()
    
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=400)       