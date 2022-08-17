from rest_framework.response import Response
from rest_framework import views
from rest_framework import permissions
from .models import PublicationModel
from .serializers import PublSerializer


# get all publications
class AllPublicationsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        publications = PublicationModel.objects.all()
        serializer = PublSerializer(publications, many=True)
        return Response({"data": serializer.data})

# get all blog publications
class BlogPublicationsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        publications = PublicationModel.objects.all().filter(cat = 'Blog')
        serializer = PublSerializer(publications, many=True)
        return Response({"data": serializer.data})

# get all articles publications
class ArticlesPublicationsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        publications = PublicationModel.objects.all().filter(cat = 'Articles')
        serializer = PublSerializer(publications, many=True)
        return Response({"data": serializer.data})

# get publication by id
class GetPublAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request, id):
        publication = PublicationModel.objects.get(pk=id)
        serializer = PublSerializer(publication)
        return Response({"data": serializer.data})

class DeletePublAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        publication = PublicationModel.objects.get(pk=id)
        publication.delete()

        return Response({'data': 'deleted'})

class EditPublicationAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        item = PublicationModel.objects.get(pk=id)
        serializer = PublSerializer(instance=item, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response({'data': 'Updated'})


class CreatePublAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        print(request.data)

        serializer = PublSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'data': request.data})
