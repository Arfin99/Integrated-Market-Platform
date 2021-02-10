from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name='home'),
    path('Webadmin/',views.admin, name='web-admin'),
    path('commerce/',views.commerce, name='commerce'),
    path('Agriculture/',views.agriculture, name='agriculture'),
    path('Custom/',views.custom, name='custom'),
    path('Bank/',views.bank, name='bank'),

    #Bank
    path('importerinfo/',views.importerinfo, name='importer-info'),
    path('addimporter/',views.add_importer, name='addimporter'),
    path('deleteimporter/<str:pk>/',views.delete_importer, name='delete_importer'),
    path('view-single-importer/<str:pk>/',views.view_single_importer, name='single_importer'),
    path('edit-importer/<str:pk>/',views.edit_importer, name='edit_importer'),

    #web-Admin
    path('Register_User_Informations/',views.register_user, name='register_user'),
    path('Applicant_User_Informations/',views.applicant_user, name='applicant_user'),
    path('Register_User_Details_Informations/<str:pk>/',views.details_register_user, name='register_details'),
    path('Delete_Register_User_Informations/<str:pk>/',views.delete_register_user, name='delete_register_user'),
    path('Applicant_Details/<str:pk>/',views.details_applicant, name='applicant_details'),
    path('Delete_Applicant_User_Informations/<str:pk>/',views.delete_applicant, name='delete_applicant_user'),

    #Port/Custom
    path('importedproduct/',views.importedproduct, name='imported-product'),
    path('totalimport/',views.totalimport, name='total-import'),
    path('dailyimport/',views.dailyimport, name='daily-import'),
    path('totalviewimport/<str:pk_test>/', views.totalviewimport, name = 'total-view-import'),
    path('totaleditimport/<str:pk_test>/', views.totaleditimport, name = 'total-edit-import'),
    path('totaladdimport/', views.totaladdimport, name = 'total-add-import'),

    # Ministry of Agriculture

    path('productedproducts/',views.productedproducts, name='producted-products'),
    path('totalproduction/',views.totalproduction, name='total-production'),
    path('dailyproduction/',views.dailyproduction, name='daily-production'),
    path('totalproductionview/<str:pk_test>/', views.totalproductionview, name = 'total-production-view'),
    path('totalproductionedit/<str:pk_test>/', views.totalproductionedit, name = 'total-production-edit'),
    path('totalproductionadd/', views.totalproductionadd, name = 'total-production-add'),


]