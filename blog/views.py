from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import ElecUnits
from .forms import FormNew#, NameForm
from datetime import datetime, timezone
# from vanilla import CreateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy


# def name(request):
#     form = NameForm()
#     return render(request, 'blog/name.html', {'form': form})

# def name(request):
#     print("Test")
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         print("2")
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             stock = form.save(commit=False)
#             print("3")
#             # process the data in form.cleaned_data as required
#             print(form.cleaned_data)
#             print(form.cleaned_data['time'].isoformat())
#             print(datetime.fromisoformat(form.cleaned_data['time'].isoformat()).timestamp())
#             #save to database:
#             #model = ElecUnits
#             stock.prevdateinmillisec = 1000*datetime.fromisoformat(form.cleaned_data['time'].isoformat()).timestamp()
#             # stock.prevDateInMilliSec = 1671407999999
#             # stock.fields['prevdateinmillisec'] = forms.BigIntegerField(initial=1671407999999)
#             # stock.fields['prevDateInMilliSec'] = 1671407999999
#             # print(stock)
#             stock.save()
#             # redirect to a new URL:
#             return HttpResponseRedirect('/name/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         print("4")
#         form = NameForm()

#     return render(request, 'blog/name.html', {'form': form})

def home(request):
    context = {
        'posts': ElecUnits.objects.all()
        #'posts': ElecUnits.objects.all().order_by('-time')[:10]
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = ElecUnits
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-time']
    paginate_by=5

class PostDetailView(DetailView):
    model = ElecUnits
    # def get(self, *args, **kwargs):
    #     response = super(PostDetailView, self).get(*args, **kwargs)
    #     # Do caching stuff here
    #     print(response)
    #     return response
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # print("----")
        # print(obj.nextdateinmillisec)
        # print(queryset)
        FormNew.elecUnitObj=obj
        return obj


class PostCreateView(CreateView):
    model = ElecUnits
    #fields = ['prevdateinmillisec', 'prevreading', 'nextdateinmillisec', 'nextreading', 'isitbill']
    form_class = FormNew
    # def get_initial(self):
    #     print("get_init")
    #     return 
    # {
    #          'author': self.request.user,
    #          'publish_date': datetime.date.today()
    #     }
    
class PostUpdateView(UpdateView):
    model = ElecUnits
    form_class = FormNew
    template_name_suffix = '_update_form'
 
class PostDeleteView(DeleteView):
    model = ElecUnits
    success_url = '/'
   

# class PostCreateView(CreateView):
#     model = ElecUnits
#     #fields = ['prevdateinmillisec', 'prevreading', 'nextdateinmillisec', 'nextreading', 'isitbill']
#     form_class = FormNew
#     # def get_form(self, form_class):
#     #     form = super(PostCreateView, self).get_form(form_class)
#     #     form.fields['prevdateinmillisec'].widget = forms.DateInput(attrs={'type': 'date'})
#     #     return form
#     def get(self, request, *args, **kwargs):
#         context = {'form': FormNew()}
#         # print(context)
#         return render(request, 'blog/elecunits_form.html', context)
    
#     def post(self, request, *args, **kwargs):
#         form = FormNew(request.POST)
#         # print(request.POST)
#         # print(form)
#         if form.is_valid():
#             stock = form.save(commit=False)
#             # if stock.isitbill=='Yes':
#             #   d=1
#             # if stock.isSave == False:
#             #   d=1
#             # stock.price=100
#             stock.save()
#             return HttpResponseRedirect(reverse_lazy('post-detail', kwargs={'pk': stock.no}))#args='post/<int:pk>/'))
#         return render(request, '', {'form': form})

def chart(request):
    labels = []
    data = []

    queryset = ElecUnits.objects.all().filter(isitbill=1).order_by('-time')[:40]
    for city in queryset:
        dt_object = datetime.fromtimestamp(city.prevdateinmillisec/1000)
        labels.append(dt_object.strftime('%Y-%b'))
        data.append(city.price)

    return render(request, 'blog/chart.html', {
        'title': 'About',
        'labels': labels,
        'data': data,
    })

def about(request):
    return render(request, 'blog/about.html', {
        'title': 'About',
    })
