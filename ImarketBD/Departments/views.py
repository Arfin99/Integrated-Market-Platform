from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from Departments.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import userInformation
from Commodities.models import commodities_import
from Commodities.models import commodities_production
from Supplier.models import importer_information
from datetime import date
# Create your views here.

def home(request):
    if request.user.is_authenticated and request.user.is_commerce:
        return redirect("commerce")
    elif request.user.is_authenticated and request.user.is_agriculture:
        return redirect("agriculture")
    elif request.user.is_authenticated and request.user.is_webadmin:
        return redirect("web-admin")
    elif request.user.is_authenticated and request.user.is_bank:
        return redirect("bank")
    elif request.user.is_authenticated and request.user.is_custom:
        return redirect("custom")
    else:
        return render(request,"home.html")

def registration_view(request):
    context = {}
    if request.user.is_authenticated and request.user.is_commerce:
        return redirect("commerce")
    elif request.user.is_authenticated and request.user.is_agriculture:
        return redirect("agriculture")
    elif request.user.is_authenticated and request.user.is_webadmin:
        return redirect("web-admin")
    elif request.user.is_authenticated and request.user.is_bank:
        return redirect("bank")
    elif request.user.is_authenticated and request.user.is_custom:
        return redirect("custom")
    else:
        if request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                organization = form.cleaned_data.get('organizations')
                account = authenticate(email=email, password=raw_password)
                return redirect('home')
            else:
                context['registration_form'] = form
        else:
            form = RegistrationForm()
            context['registration_form'] = form
            return render(request, 'Application form.html', context)


def login_view(request):
    context = {}
    user =  request.user
    if user.is_authenticated and user.is_commerce:
        return redirect("commerce")
    elif user.is_authenticated and user.is_agriculture:
        return redirect("agriculture")
    elif user.is_authenticated and user.is_webadmin:
        return redirect("web-admin")
    elif user.is_authenticated and user.is_bank:
        return redirect("bank")
    elif user.is_authenticated and user.is_custom:
        return redirect("custom")
    else:
        if request.POST:
            form = AccountAuthenticationForm(request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(email=email, password=password)

                if user.is_webadmin:
                    login(request,user)
                    return redirect("web-admin")
                
                if user.is_allow and user.is_commerce:
                    login(request,user)
                    return redirect("commerce") 
                
                if user.is_allow and user.is_custom:
                    login(request,user)
                    return redirect("custom") 
                
                if user.is_allow and user.is_bank:
                    login(request,user)
                    return redirect("bank") 
                
                if user.is_allow and user.is_agriculture:
                    login(request,user)
                    return redirect("agriculture")      
                else:
                    return HttpResponse("You are Not Authorized User Right Now!!!")
        else:
            form = AccountAuthenticationForm()
            context['login_form'] =form
            return render(request, 'signin.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def commerce(request):
    return render(request,"moc/index.html")


@login_required(login_url='login')
def agriculture(request):
    productionproducts = commodities_production.objects.all()
    totalproductionproducts = productionproducts.count()

    today = date.today()
    todayproductionproducts = commodities_production.objects.filter(last_updated=today)
    totalproductiontodayinsert = todayproductionproducts.count()

    context = {'todayproductionproducts':todayproductionproducts, 'totalproductionproducts':totalproductionproducts, 'totalproductiontodayinsert':totalproductiontodayinsert}


    return render(request,"moa/index-agriculture.html", context)

@login_required(login_url='login')
def bank(request):
    return render(request,"bb/index-bank.html")

@login_required(login_url='login')
def custom(request):
    importedproducts = commodities_import.objects.all()
    totalimportedproducts = importedproducts.count()
    

    today = date.today()
    todayimportedproducts = commodities_import.objects.filter(last_updated=today)
    totaltodayinsert = todayimportedproducts.count()

    context = {'todayimportedproducts':todayimportedproducts, 'totalimportproducts':totalimportedproducts, 'totaltodayinsert':totaltodayinsert}

    return render(request,"port/index-port.html", context)



#Bank-Information Block START
# (Importer CRUD)
@login_required(login_url='login')
def importerinfo(request):

    importers = importer_information.objects.all()
    return render(request,"bb/importer-information.html", {'importers': importers})

@login_required(login_url='login')
def add_importer(request):

    if request.method == 'POST':
        importer_ID         = request.POST['importer_id']
        importer_name       = request.POST['importer_name']
        nid_number          = request.POST['nid_number']
        phone               = request.POST['phone_number']
        bank_name           = request.POST['bank_name']
        bank_account        = request.POST['bank_account']

        importer = importer_information(importer_ID= importer_ID, importer_name=importer_name, importer_Nid=nid_number, importer_phone_number=phone, bank_name=bank_name, bank_account_number=bank_account)
        importer.save()
        return redirect("importer-info")
    else:
        return render(request,"bb/importer-add.html")

@login_required(login_url='login')
def view_single_importer(request, pk):
    importer = importer_information.objects.get(id=pk)
    return render(request,"bb/importer-view.html", {'importer': importer})

@login_required(login_url='login')
def edit_importer(request, pk):

    if request.method == 'POST':
        importer_ID         = request.POST['importer_id']
        importer_name       = request.POST['importer_name']
        nid_number          = request.POST['nid']
        phone               = request.POST['phone']
        bank_name           = request.POST['bank_name']
        bank_account        = request.POST['account_number']
        
        update_importer = importer_information(id=pk, importer_ID= importer_ID, importer_name=importer_name, importer_Nid=nid_number, importer_phone_number=phone, bank_name=bank_name, bank_account_number=bank_account)
        update_importer.save()
        return redirect("importer-info")
    else:
        importer = importer_information.objects.get(id=pk)
        return render(request,"bb/importer-edit.html", {'importer': importer})


@login_required(login_url='login')
def delete_importer(request, pk):
    importer = importer_information.objects.get(id=pk)
    importer.delete()
    return redirect("importer-info")

#Bank-Information Block END


#Web Admin Block Start

@login_required(login_url='login')
def admin(request):
    registerUser=userInformation.objects.all()
    return render(request,"web admin/web-admin.html",{'registerUser': registerUser})

#Registered User Informations
@login_required(login_url='login')
def register_user(request):
    registerUser=userInformation.objects.all()
    return render(request,"web admin/register-user.html",{'registerUser': registerUser})

@login_required(login_url='login')
def details_register_user(request, pk):
    register = userInformation.objects.get(id=pk)
    return render(request,"web admin/register-details.html", {'register': register})

@login_required(login_url='login')
def delete_register_user(request, pk):
    registerUser = userInformation.objects.get(id=pk)
    registerUser.delete()
    return redirect("register_user")


#Applicant Users Informations
@login_required(login_url='login')
def applicant_user(request):
    registerUser=userInformation.objects.all()
    return render(request,"web admin/applicant-info.html",{'registerUser': registerUser})

@login_required(login_url='login')
def details_applicant(request, pk):
    register = userInformation.objects.get(id=pk)
    return render(request,"web admin/applicant-details.html", {'register': register})

@login_required(login_url='login')
def delete_applicant(request, pk):
    registerUser = userInformation.objects.get(id=pk)
    registerUser.delete()
    return redirect("applicant_user")
#Web Admin Block END

#Port / Custom Block 

@login_required(login_url='login')
def importedproduct(request):

    importedproducts = commodities_import.objects.all()
    return render(request,"port/imported-product.html", {'importedproducts': importedproducts})
@login_required(login_url='login')
def totalimport(request):
    importedproducts = commodities_import.objects.all()
    context = {'importedproducts':importedproducts}
    return render(request, "port/total-import.html", context)

@login_required(login_url='login')
def dailyimport(request):
    today = date.today()
    dailyimportedproducts = commodities_import.objects.filter(last_updated=today)
    context = {'dailyimportedproducts':dailyimportedproducts}
    return render(request, "port/daily-import.html", context)

@login_required(login_url='login')
def totalviewimport(request, pk_test):
    importedproduct = commodities_import.objects.get(id=pk_test)
    context = {'importedproduct': importedproduct}
    return render(request, "port/total-view-import.html", context)

@login_required(login_url='login')
def totaleditimport(request, pk_test):
    if request.method == 'POST':
        product_Name        = request.POST['importedproduct_name']
        import_quantity       = request.POST['imported_product_quantity']
        import_cost         = request.POST['imported_product_cost']
        import_place                = request.POST['imported_port']
        import_date            = request.POST['imported_date']
        importer_name        = request.POST['importer_name']
        importer_mobile_number        = request.POST['importer_mobile_number']
        
        
        update_imported_product = commodities_import(id=pk_test, product_Name= product_Name, import_quantity=import_quantity, import_cost=import_cost, import_place=import_place, import_date=import_date, importer_name=importer_name,importer_mobile_number=importer_mobile_number, email_id=request.user)
        update_imported_product.save()
        return redirect("total-import")
    else:
        importedproduct = commodities_import.objects.get(id=pk_test)
        context = {'importedproduct':importedproduct}
        return render(request, "port/total-edit-import.html", context)

@login_required(login_url='login')
def totaladdimport(request):
    if request.method == 'POST':
        product_Name        = request.POST['importedproduct_name']
        import_quantity       = request.POST['imported_product_quantity']
        import_cost         = request.POST['imported_product_cost']
        import_place                = request.POST['imported_port']
        import_date            = request.POST['imported_date']
        importer_name        = request.POST['importer_name']
        importer_mobile_number        = request.POST['importer_mobile_number']
        
        
        insert_imported_product = commodities_import(product_Name= product_Name, import_quantity=import_quantity, import_cost=import_cost, import_place=import_place, import_date=import_date, importer_name=importer_name,importer_mobile_number=importer_mobile_number, email_id = request.user.id)
        insert_imported_product.save()
        return redirect("total-import")
    else:
        return render(request,"port/total-add-import.html")



#### End Port / Custom ####

##### Start Ministry of Agriculture #############
@login_required(login_url='login')
def productedproducts(request):

    productedproducts = commodities_production.objects.all()
    return render(request,"moa/producted-products.html", {'productedproducts': productedproducts})
@login_required(login_url='login')
def totalproduction(request):

    productedproducts = commodities_production.objects.all()
    context = {'productedproducts':productedproducts}
    return render(request, "moa/total-production.html", context)

@login_required(login_url='login')
def dailyproduction(request):
    today = date.today()
    dailyproductedproducts = commodities_production.objects.filter(last_updated=today)
    context = {'todayproductionproducts':dailyproductedproducts}
    return render(request, "moa/daily-production.html", context)

@login_required(login_url='login')
def totalproductionview(request, pk_test):
    productedproduct = commodities_production.objects.get(id=pk_test)
    context = {'productedproduct': productedproduct}
    return render(request, "moa/total-production-view.html", context)

@login_required(login_url='login')
def totalproductionedit(request, pk_test):
    if request.method == 'POST':
        product_Name        = request.POST['product_name']
        production_quantity       = request.POST['product_quantity']
        production_cost         = request.POST['product_cost']
        production_place                = request.POST['production_place']
        production_date            = request.POST['production_date']
        
        
        
        update_producted_product = commodities_production(id=pk_test, product_Name= product_Name, production_quantity=production_quantity, production_cost=production_cost, production_place=production_place, production_date=production_date, email_id=request.user)
        update_producted_product.save()
        return redirect("total-production")
    else:
        productedproduct = commodities_production.objects.get(id=pk_test)
        context = {'productedproduct':productedproduct}
        return render(request, "moa/total-production-edit.html", context)

@login_required(login_url='login')
def totalproductionadd(request):
    if request.method == 'POST':
        product_Name        = request.POST['product_name']
        production_quantity       = request.POST['product_quantity']
        production_cost         = request.POST['product_cost']
        production_place                = request.POST['production_place']
        production_date            = request.POST['production_date']
        
        
        insert_producted_product =commodities_production(product_Name= product_Name, production_quantity=production_quantity, production_cost=production_cost, production_place=production_place, production_date=production_date, email_id=request.user.id)
        insert_producted_product.save()
        return redirect("total-production")
    else:
        return render(request,"moa/total-production-add.html")

######### End Ministry of Agriculture #########

