from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        # Здесь будет логика обработки формы
        return redirect('confirmation')
    return render(request, 'page2.html')

def confirmation(request):
    return render(request, 'registr.html')
