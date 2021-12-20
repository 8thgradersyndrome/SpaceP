# SELECT

# SELECT * FROM products;
# Product.objects.all()

# SELECT * FROM products WHERE ....;
# Product.objects.filter(...)

# SELECT * FROM products WHERE price = 10000;
# Product.objects.filter(price=10000)

# SELECT * FROM products WHERE price !=10000;
# Product.objects.filter(~Q(price=10000))
# Product.objects.exclude(price=10000)

# SELECT * FROM products WHERE price > 10000;
# Product.objects.filter(price__gt=10000)

# SELECT * FROM products WHERE price < 10000;
# Product.objects.filter(price__lt=10000)

# SELECT * FROM products WHERE price >= 10000;
# Product.objects.filter(price__gte=10000)

# SELECT * FROM products WHERE price <= 10000;
# Product.objects.filter(price__lte=10000)

# SELECT * FROM products WHERE price IN ('phones', 'tv')
# Product.objects.filter(price__in=['phones', 'tv'])

# SELECT * FROM products WHERE price BETWEEN 2000 and 5000;
# Product.objects.filter(price__range=[2000, 50000])

# LIKE

# SELECT * FROM products WHERE name LIKE '%test%';
# Product.objects.filter(name__exact='test')

# Product.objects.filter(name__startswith='test') - начинается
# Product.objects.filter(name__endswith='test') - заканчивается
# Product.objects.filter(name__contains='test') - содержится

# SELECT * FROM WHERE ILIKE '%test%';
# Product.objects.filter(name__iexact='test')


# получение одной записи
#SELECT * FROM products WHERE id=1;
#Product.objects.get(id=1)

# ограничение набора полей

# SELECT name, price FROM products;
# Product.objects.only('name', 'price')

# SELECT id, description, category_id FROM products;
# Products.objects.only('id', 'description', 'category_id')
# Products.objects.defer('name', 'price')

# SELECT * FROM products ORDER BY price;
# Product.objects.order_by(price)
#
# SELECT * FROM products ORDER BY  price desc;
# Product.objects.order_by(-price)


# INSERT
# INSERT INTO products(name, description, price, category) VALUES ('Mi 10', 'норм телеф', 40000, 'phones' )
#
# Product.objects.create('Mi 10', 'норм телеф', 40000, 'phones')
#
# Product.objects.bull create([....],[...])
#
# product = Product(...)
# product.save()


# UPDATE
# UPDATE products SET price=10000;
# Products.objects.update(price=10000)

# UPDATE  products SET price=10000 WHERE category = 'phone'
# Product.objects.filter(category='phones').update(price=1000)

# обновляем один объекта

# DELETE
# DELETE FROM  products WHERE category = 'tv';
# Product.objects.filter(category='tv').delete()
