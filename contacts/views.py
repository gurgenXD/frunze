from django.shortcuts import render
from django.views import View
from contacts.models import *
from callback.forms import CallBackForm


class ContactsView(View):
    @staticmethod
    def get(request):
        addresses = Address.objects.all()
        phones = Phone.objects.all()
        faxes = Fax.objects.all()
        emails = Email.objects.all()
        map_code = MapCode.objects.first()
        requisite = Requisite.objects.first()

        callback_form = CallBackForm()

        context = {
            'addresses': addresses,
            'phones': phones,
            'faxes': faxes,
            'emails': emails,
            'map_code': map_code,
            'requisite': requisite,
            'callback_form': callback_form,
        }
        return render(request, 'contacts/contacts.html', context)