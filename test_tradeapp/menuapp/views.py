from django.shortcuts import render


def test_menu_view(request):
    return render(request, 'menuapp/test_template.html')
