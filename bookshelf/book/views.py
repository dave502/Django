from django.shortcuts import render

# Create your views here.
def cover_view(request):
    # <app>/templates/<app>/cover.html
    return render(request, 'book/cover.html')

def variable_view(request):
    dict1 = {'first_name': 'Rosalin', 'last_name':'Franklin', 'some_list':[1,2,3], 'some_dict':{'inside_key':'inside_value'}, 'user_logged_in': True}
    return render(request, 'book/variable.html', context=dict1)