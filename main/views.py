from django.shortcuts import render
import pickle

# Create your views here.
def home(request):
    return render(request,'main/home.html')
def result(request):
    # cls=pickle.load(open('model.pkl','rb'))
    with open('models.pkl','rb') as f:
        cls=pickle.load(f)
    list=[]
    list.append(request.GET['Fever'])
    list.append(request.GET['Pain'])
    list.append(request.GET['Severe'])
    list.append(request.GET['Age'])
    print(list)
    
    result = cls.predict_proba([list])[0][1]
    return render(request,'main/result.html',{'result':result})


    
