from sqlconnection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()

    query = '''SELECT Products.Product_id, Products.name, Products.uom_id, Products.price_per_unit, uom.uom_name 
           FROM RodriguezGrocery.Products
           INNER JOIN uom 
           ON Products.uom_id = uom.uom_id;'''

    cursor.execute(query)

    response = []

    for (Product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'Product_id': Product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    return response


def insert_new_product(connection, Products):
    cursor = connection.cursor()
    query = ('INSERT INTO Products' 
             '(name, uom_id, price_per_unit)' 
             'VALUES (%s, %s, %s)')
    data = (Products['name'], Products['uom_id'], Products['price_per_unit'])
    cursor.execute = (query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ('DELETE FROM Products WHERE Product_id=' + str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    # delete_product(connection, 20)  # to delete a particular product
    #print(get_all_products(connection))  # this is to see all of your products
    print(insert_new_product(connection, {
        'name': 'cabbage',    # to insert a new product
        'uom_id': '2',
        'price_per_unit': '10'
    }))
    print(get_all_products(connection))  # this is to see all of your products