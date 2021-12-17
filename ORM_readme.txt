# Product.objects.all()
# select * from products;

# Product.objects.get(id=1)
# select * from products where id=1;

# Product.objects.filter(условие1,условие2)
# select * from  products where условие1 and условие2

# Product.objects.filter(Q(условие1)|Q(условие2))
# select * from  products where условие1 OR условие2

# Product.objects.filter(~Q(условие))
# Product.objects.exclude(условие)  #возвращает те моменты которые не совпали с условием
# select * from  products where NOT условие

# select * from products WHERE price>50000;
# Product.object.filter(price__gt=50000)

# select * from products WHERE price<50000;
# Product.object.filter(price__lt=50000)

# select * from products WHERE price>=50000;
# Product.object.filter(price__gte=50000)

# select * from products WHERE price<=50000;
# Product.object.filter(price__lte=50000)

# SELECT * FROM product WHERE category_id IN ('phones','notebooks');
# Product.objects.filter(category_id__in ['phones','notebooks']

# SELECT * FROM products WHERE price BETWEEN 20000 and 50000;
# Product.objects.filter(price__range=[20000,50000])

# Product.objects.filter(name__exact='Iphone')
# SELECT * from products WHERE name LIKE 'Iphone';
# Product.objects.filter(name__iexact='Iphone')
# SELECT * from products WHERE name ILIKE 'Iphone';

# Product.objects.filter(name__startwith='Iphone')
# SELECT * from products WHERE name LIKE 'Iphone%';
# Product.objects.filter(name__istartwith='Iphone')
# SELECT * from products WHERE name ILIKE 'Iphone%';

# Product.objects.filter(name__contains='Iphone')
# SELECT * from products WHERE name LIKE '%Iphone%';
# Product.objects.filter(name__icontains='Iphone')
# SELECT * from products WHERE name ILIKE '%Iphone%';

# Product.objects.filter(name__endswith='Iphone')
# SELECT * from products WHERE name LIKE '%Iphone';
# Product.objects.filter(name__iendswith='Iphone')
# SELECT * from products WHERE name ILIKE '%Iphone';

# SELECT * FROM products ORDER BY price ASC;
# Product.objects.order_by('price')

# SELECT * FROM products ORDER BY price DESC;
# Product.objects.order_by('-price')

# SELECT name,price FROM products;
# Product.objects.price only(name)

# SELECT id,description,category_id FROM products;
# Product.objects.defer('name','price')

# Product.objects.count()
# Select count(*) FROM product;

# Product.objects.filter(...).count()
# Select count(*) FROM product WHERE ...;

#########          INSERT                ##############

# INSERT INTO products (name,description,price,category_id) VALUES ('Apple Iphone12','dsfdsf', 78000 ,'phones');
# Product.objects.create(name='Apple Iphone12',
#                        description ='dsfdsf',
#                        price= 78000 ,
#                        category_id ='phones') # одиночное добавление

# Product.objects.bulk_create([
#     Product(...),
#     Product(...)
# ]) # множественное добавление

#########          UPDATE                ##############

# Product.objects.update(price=50000)
# UPDATE products SET price=50000;

# Product.objects.filter(...).update(price=50000)
# UPDATE products SET price=50000 where условие;

#Вариант через 3 запроса
# product = Product.objects.get(id=1)
# product.price = 50000
# product.save()

#########          DELETE                ##############

# Product.objects.delete()
# DELETE FROM products;

# Product.objects.filter(category_id='phones').delete()
# DELETE FROM product WHERE category_id = 'phones';

# DELETE FROM products WHERE id=1
# Product.objects.filter(id=1).delete()

# вариант через два запроса

# product =  Product.objects.get(id=1)
# product.delete()

################################################ urls#####################
# 1 Variant
    # path('api/v1/products/', ProductListCreateView.as_view()),
    # path('api/v1/products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view())
# 2 Variant
    # path('api/v1/products/', ProductViewSet.as_view(
    #     {'get':'list','post':'create'}
    # )),
    # path('api/v1/products/<int:pk>/', ProductViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
    # ))
# 3 variant