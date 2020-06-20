from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from phones.models import Phone, PhoneAddInfo


class Catalog(DetailView):
    model = Phone
    template = 'catalog.html'
    context_object_name = 'catalog'

    def get(self, request):
        phone = Phone.objects.all()
        add_info = PhoneAddInfo.objects.all().select_related('phone_model').values('phone_model', 'add_info')
        print(add_info)
        context = {
            'phone': phone,
            'add_info': add_info,
        }
        return render(request, self.template, context)