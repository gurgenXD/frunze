from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from callback.models import CallBack
from callback.forms import CallBackForm
from core.models import MailToString


class CallBackView(View):
    @staticmethod
    def post(request):
        callback_form = CallBackForm(request.POST)
        
        if callback_form.is_valid():
            current_site = get_current_site(request)
            mail_subject = 'Новый звонок на сайте: ' + current_site.domain
            message = render_to_string('email_messages/callback_message.html', {
                'domain': current_site.domain,
                'phone': request.POST.get('phone'),
            })
            try:
                to_email = MailToString.objects.first().email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                callback_form.save()
                status = 1
            except:
                status = 0
        else:
            status = 0
        
        context = {
            'status': status,
        }
        return JsonResponse(context)