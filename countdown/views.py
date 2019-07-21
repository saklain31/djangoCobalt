from django.shortcuts import render

# Create your views here.


##### Parameter will be event, fetch data from db and show
def countDownTime(request):
    date = "Jan 5, 2021 15:37:25"
    return render(request,'count_down.html',{'date':date})
