from django.shortcuts import render
from django.views import View
from documents.models import Document


class DocumentsView(View):
    @staticmethod
    def get(request):
        documents = Document.objects.filter(is_active=True)

        context = {
            'documents': documents,
        }
        return render(request, 'documents/documents.html', context)
