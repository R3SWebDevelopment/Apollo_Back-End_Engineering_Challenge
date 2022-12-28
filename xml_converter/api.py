from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import ValidationError
from xml_converter.converted import convert_to_json


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        # Valid the file has been provided
        if 'file' not in request.FILES or request.FILES['file'] is None:
            raise ValidationError("No Input File provided")

        # Fetch content of uploaded file
        file = request.FILES['file']
        file.open()
        content = file.read()
        file.close()

        # Valid is not an empty file
        if len(content.strip()) == 0:
            raise ValidationError("Empty File provided")

        json_obj = convert_to_json(content)

        return Response(json_obj)
