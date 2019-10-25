from django.shortcuts import render
from django.http import  JsonResponse
from .models import CustomerModel, CompanyModel, PersonsModel, AccountsModel
from .serializers import PersonSerializer, AccountsSerializer, ProjectsSerializer
# Create your views here.


# this is a Class Based View, but you can use a function based one too



def person_id_view(request, name):
    data = CustomerModel.objects.filter(name=name)[0].persons.all()
    serializer = PersonSerializer(data,many=True)
    print(serializer.data)
    return JsonResponse({
        'status' : serializer.data
    })


def accounts_id_view(request, name):
    data = CompanyModel.objects.filter(name=name)[0].account.all()
    serializer = AccountsSerializer(data, many=True)
    print(serializer.data)
    return JsonResponse({
        'status': serializer.data
    })



def project_id_view(request,  personname, companyname ):
    person = personname.split()[0]
    company = companyname.split()[0]
    print(companyname)
    print(personname)
    customer = CustomerModel.objects.filter(name=companyname)[0]
    data = PersonsModel.objects.filter(first_name=person,customer=customer)[0].projects
    serializer = ProjectsSerializer(data, many=True)
    # print(data)
    return JsonResponse({
        'status': serializer.data
    })


def accountsum(request):
    data = list(AccountsModel.objects.all())
    value = list(map(lambda x: x.azn_value(),data))
    summ = sum(value)
    return JsonResponse({
        'status' : summ
    })