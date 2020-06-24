from django.shortcuts import render

# Create your views here.
def calculator(request, met, v1, v2):
    webcontexto = {}
    if met and v1 and v2:
        webcontexto['v1'] = v1
        webcontexto['v2'] = v2
        if met == "soma":
            webcontexto['resultado'] = v1 + v2
            op = "+"

        if met == "sub":
            webcontexto['resultado'] = v1 - v2
            op = "-"
       

        if met == "mult":
            webcontexto['resultado'] = v1 * v2
            op = "x"

       
        if met == "div":
            webcontexto['resultado'] = v1 / v2
            op = "÷"

        webcontexto['op'] = op
        
    else:
        webcontexto['resultado'] = 'Nenhum dado foi passado!'
    
    return render(request, 'resultado.html', context=webcontexto)

def index(request):
    return render(request, 'calculadora.html')