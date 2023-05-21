from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def showOrder(request) :
    tables = Table.objects.all()
    menus = Menu.objects.all()
    return render(request, 'main/order.html', {'tables': tables, 'menus':menus})

def create(request):
    new_table = Table()
    new_table.save()
    return redirect('showOrder')

def update(request, id):
    update_table = Table.objects.get(id=id)
    if True:
        total = 0
        menus = Menu.objects.all()

        update_table.menu1 = int(request.POST['menu1'])
        total = total + update_table.menu1 * menus[0].price
        update_table.menu2 = int(request.POST['menu2'])
        total = total + update_table.menu2 * menus[1].price
        update_table.menu3 = int(request.POST['menu3'])
        total = total + update_table.menu3 * menus[2].price
        update_table.menu4 = int(request.POST['menu4'])
        total = total + update_table.menu4 * menus[3].price
        update_table.menu5 = int(request.POST['menu5'])
        total = total + update_table.menu5* menus[4].price
        update_table.menu6 = int(request.POST['menu6'])
        total = total + update_table.menu6 * menus[5].price
        update_table.menu7 = int(request.POST['menu7'])
        total = total + update_table.menu7 * menus[6].price
        update_table.special_note = request.POST['special_note']
    

        update_table.total = total
        update_table.save()
        return redirect('showOrder')
    
def endtable(request, id):
    table = Table.objects.get(id=id)
    totalResult = Total.objects.all()
    if totalResult.count() == 0:
        new_total = Total()
        new_total.menu1 = table.menu1
        new_total.menu2 = table.menu2
        new_total.menu3 = table.menu3
        new_total.menu4 = table.menu4
        new_total.menu5 = table.menu5
        new_total.menu6 = table.menu6
        new_total.menu7 = table.menu7
        new_total.menu8 = table.menu8
        new_total.total = table.total
        new_total.save()

    else:
        update_total = totalResult[0]
        update_total.menu1 = update_total.menu1 + table.menu1
        update_total.menu2 = update_total.menu2 + table.menu2
        update_total.menu3 = update_total.menu3 + table.menu3
        update_total.menu4 = update_total.menu4 + table.menu4
        update_total.menu5 = update_total.menu5 + table.menu5
        update_total.menu6 = update_total.menu6 + table.menu6
        update_total.menu7 = update_total.menu7 + table.menu7
        update_total.menu8 = update_total.menu8 + table.menu8
        update_total.total = update_total.total + table.total
        update_total.save()
    
    new_Result = Result()
    new_Result.menu1 = table.menu1
    new_Result.menu2 = table.menu2
    new_Result.menu3 = table.menu3
    new_Result.menu4 = table.menu4
    new_Result.menu5 = table.menu5
    new_Result.menu6 = table.menu6
    new_Result.menu7 = table.menu7
    new_Result.menu8 = table.menu8
    new_Result.total = table.total
    new_Result.save()
        
    table.menu1 = 0
    table.menu2 = 0
    table.menu3 = 0
    table.menu4 = 0
    table.menu5 = 0
    table.menu6 = 0
    table.menu7 = 0
    table.menu8 = 0
    table.total = 0
    table.save()
    table.delete()
    return redirect('showOrder')


def showresults(request):
    results = Result.objects.all()
    totals = Total.objects.all()
    menus = Menu.objects.all()
    return render(request, 'main/results.html', {'results': results, 'menus':menus, 'totals':totals})

def updateresult(request,id):
    update_result = Result.objects.get(id=id)
    totalResults = Total.objects.all()
    totalResult = totalResults[0]
    total = 0
    menus = Menu.objects.all()

    totalResult.menu1 = totalResult.menu1 - update_result.menu1
    update_result.menu1 = int(request.POST['menu1'])
    total = total + update_result.menu1 * menus[0].price
    totalResult.menu1 = totalResult.menu1 + update_result.menu1

    totalResult.menu2 = totalResult.menu2 - update_result.menu2
    update_result.menu2 = int(request.POST['menu2'])
    total = total + update_result.menu2 * menus[1].price
    totalResult.menu2 = totalResult.menu2 + update_result.menu2

    totalResult.menu3 = totalResult.menu3 - update_result.menu3
    update_result.menu3 = int(request.POST['menu3'])
    total = total + update_result.menu3 * menus[2].price
    totalResult.menu3 = totalResult.menu3 + update_result.menu3

    totalResult.menu4 = totalResult.menu4 - update_result.menu4
    update_result.menu4 = int(request.POST['menu4'])
    total = total + update_result.menu4 * menus[3].price
    totalResult.menu4 = totalResult.menu4 + update_result.menu4

    totalResult.menu5 = totalResult.menu5 - update_result.menu5
    update_result.menu5 = int(request.POST['menu5'])
    total = total + update_result.menu5 * menus[4].price
    totalResult.menu5 = totalResult.menu5 + update_result.menu5

    totalResult.menu6 = totalResult.menu6 - update_result.menu6
    update_result.menu6 = int(request.POST['menu6'])
    total = total + update_result.menu6 * menus[5].price
    totalResult.menu6 = totalResult.menu6 + update_result.menu6

    totalResult.menu7 = totalResult.menu7 - update_result.menu7
    update_result.menu7 = int(request.POST['menu7'])
    total = total + update_result.menu7 * menus[6].price
    totalResult.menu7 = totalResult.menu7 + update_result.menu7

    totalResult.menu8 = totalResult.menu8 - update_result.menu8
    update_result.menu8 = int(request.POST['menu8'])
    total = total + update_result.menu8 * menus[7].price
    totalResult.menu8 = totalResult.menu8 + update_result.menu8

    totalResult.total = totalResult.total - update_result.total
    update_result.total = total
    totalResult.total = totalResult.total + update_result.total
    update_result.save()
    totalResult.save()
    return redirect('showresults')

def deleteresult(request,id):
    delete_result = Result.objects.get(id=id)
    totalResults = Total.objects.all()
    totalResult = totalResults[0]

    totalResult.menu1 = totalResult.menu1 - delete_result.menu1
    totalResult.menu2 = totalResult.menu2 - delete_result.menu2
    totalResult.menu3 = totalResult.menu3 - delete_result.menu3
    totalResult.menu4 = totalResult.menu4 - delete_result.menu4
    totalResult.menu5 = totalResult.menu5 - delete_result.menu5
    totalResult.menu6 = totalResult.menu6 - delete_result.menu6
    totalResult.menu7 = totalResult.menu7 - delete_result.menu7
    totalResult.menu8 = totalResult.menu8 - delete_result.menu8
    totalResult.total = totalResult.total - delete_result.total
    delete_result.delete()
    totalResult.save()
    return redirect('showresults')
    