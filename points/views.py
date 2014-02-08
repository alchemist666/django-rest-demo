from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OriginationPoint
from .serializers import OriginationPointSerializer


@api_view(['GET', 'POST'])
def op_list(request):
    """
    List all op, or create a new op.
    """
    if request.method == 'GET':
        ops = OriginationPoint.objects.all()
        serializer = OriginationPointSerializer(ops, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OriginationPointSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def op_detail(request, pk):
    """
    Retrieve, update or delete a op instance.
    """
    try:
        op = OriginationPoint.objects.get(pk=pk)
    except OriginationPoint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OriginationPointSerializer(op)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OriginationPointSerializer(op, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        op.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)