from email import message
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Note
from .serializer import NoteSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404

# Create your views here.


@api_view(["GET"])
def getRoutes(req):

    routes = [
        {
            "Endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes",
        },
        {
            "Endpoint": "/notes/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single note object",
        },
        {
            "Endpoint": "/notes/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting note",
        },
    ]

    # return JsonResponse(routes, safe=False)
    return Response(routes)


@api_view(["GET"])
def getNotes(req):
    notes = Note.objects.all().order_by("-updated")
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


# @api_view(["POST"])
# def createNote(req):
#     data = req.data
#     # title = data['title']
#     body = data["body"]
#     newNote = Note.objects.create(body)
#     serializer = NoteSerializer(data=newNote, many=False)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)

{"title": "test Title", "body": "Test Body"}


@api_view(["POST"])
def createNote(req):
    data = req.data
    body = data["body"]

    if "title" in data:
        title = data["title"]
    else:
        title = None

    serializer = NoteSerializer(data=data, many=False)
    if serializer.is_valid():
        if title != None:
            Note.objects.create(title=title, body=body)
        Note.objects.create(body=body)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def getNote(req, id):
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def updateNote(req, id):
    data = req.data
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteNote(req, id):
    note = get_object_or_404(Note, id=id)
    serializer = NoteSerializer(instance=note, many=False)
    title = serializer.data.get("title")
    note.delete()

    return Response({"msg": "success", "title": title}, status=status.HTTP_200_OK)
