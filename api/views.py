from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Subject
from .serializers import SubjectSerializer

@api_view(['GET'])
def subjects(request):
	subjects = Subject.objects.all()
	serializer = SubjectSerializer(subjects, many=True)
	return Response(serializer.data)
	# return Response({'name': 'John', 'age': 23})


