from django.contrib.admin import action
from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(detail=True, methods=['post'])
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data :
            if 1 <= int(request.data['stars']) <= 5:
                meal = self.get_object()
                stars = request.data['stars']
                user = request.user
                # update or create rating
                rating, created = Rating.objects.update_or_create(
                    user=user,
                    meal=meal,
                    defaults={'stars': stars}
                )
                return Response({'message': 'Rating has been added/updated.','data': {'stars': rating.stars}},status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Stars parameter must be an integer between 1 and 5.'}, status=status.HTTP_400_BAD_REQUEST)
        else:       
            return Response({'message': 'Stars parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)


    
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
