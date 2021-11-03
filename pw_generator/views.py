from django.shortcuts import render
from django import forms
from . import chars

class AddForm(forms.Form):
    upper = forms.IntegerField(label="Uppercase letters: ")
    lower = forms.IntegerField(label="Lowercase letters: ")
    symbols = forms.IntegerField(label="Symbols")
    nums = forms.IntegerField(label="Numbers")

# Create your views here.
def render_generator(request):
    return render(request, 'django_redo/generator.html', {})

def create(request):

    if request.method == 'GET':
        return render(request,'django_redo/create.html',{'form': AddForm()})

    elif request.method == 'POST':
        form = AddForm(request.POST)

        if form.is_valid():
            upper = form.cleaned_data['upper']
            lower = form.cleaned_data['lower']
            symbols = form.cleaned_data['symbols']
            nums = form.cleaned_data['nums']
            result = chars.allChars(upper,lower,symbols,nums)
            
            # vars to strip password from end of allChars() return statement, which is an f string and combine the return statement with the password in bold to the user
            total_num = upper + lower + symbols + nums
            list = result.split()
            pw = list[-1]
            list.remove(pw)
            list = ' '.join(list)
            
            return render(request,'django_redo/generated_pw.html',{
                'form': form,
                'upper': upper,
                'lower': lower,
                'symbols': symbols,
                'nums': nums,
                'total_num': total_num,
                'result': result,
                'list': list,
                'pw': pw     
            })
        else:
            return render(request,'django_redo/create.html',{'form': form}) 
