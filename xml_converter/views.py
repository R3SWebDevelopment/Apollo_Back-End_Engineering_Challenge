from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import BadRequest
from xml_converter.converted import convert_to_json


def upload_page(request):
    if request.method == 'POST':
        # Valid the file has been provided
        if 'file' not in request.FILES or request.FILES['file'] is None:
            raise BadRequest("No Input File provided")

        # Fetch content of uploaded file
        file = request.FILES['file']
        file.open()
        content = file.read()
        file.close()

        # Valid is not an empty file
        if len(content.strip()) == 0:
            raise BadRequest("Empty File provided")

        json_obj = convert_to_json(content)

        return JsonResponse(json_obj)

    return render(request, "upload_page.html")
