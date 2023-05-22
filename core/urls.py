from django.urls import path
from .views import *

#urlpatterns = [
#path('admin/', admin.site.urls),
#]
urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('detail/', detail, name="detail"),
    path('price/', price, name="price"),
    path('product/', product, name="product"),
    path('service/', service, name="service"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),
    path('rastreo/', rastreo, name="rastreo"), 
    path('pagocarro/', pagocarro, name="pagocarro"),
    #CRUD
    path('add/', add, name="add"),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
    
    #Carrito
    path('carrito/', carrito, name='carrito'),
    path('carrito/agregar/<int:producto_id>/',agregar_producto, name='agregar_producto'),
    path('carrito/eliminar/<int:item_id>/',eliminar_producto, name='eliminar_producto'),

]