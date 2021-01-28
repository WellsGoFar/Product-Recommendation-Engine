import pandas as pd
from numpy import load
from random import randint

cosine_sim = load('resources/cosine_sim.npy')

print(cosine_sim.shape)

df = pd.read_csv('resources/flipkart_com-ecommerce_sample.csv')
df = df.reset_index()

def get_prod_name_from_index(index):
	return df[df.index == index]["product_name"].values[0]

def get_index_from_prod_name(prod_name):
	return df[df.product_name == prod_name]["index"].values[0]

orders = pd.read_csv('resources/orders.csv')

c_id = int(input("select a customer id between 100 and 149: "))

while True:
    if c_id!=0:
        customer_order_index = orders.loc[orders['user_id'] == c_id]['product_name'].index[0]
        order_item = orders.loc[orders['user_id'] == c_id]['product_name'][customer_order_index]

        # for i in customer_order:
        #     # order_item = i['product_name']
        #     print(i)


        offers = [5, 7, 10]
        print('The customer ordered: ' + order_item)

        print('Some similar items are: ')
        prod_index = get_index_from_prod_name(order_item)
        similar_products = list(enumerate(cosine_sim[prod_index]))
        sorted_similar_products = sorted(similar_products, key = lambda x:x[1], reverse=True)
        i=0
        recommended_products = set()
        for prod in sorted_similar_products:
            # print(get_prod_name_from_index(prod[0]))
            recommended_products.add(get_prod_name_from_index(prod[0]))
            i=i+1
            if i>10:
                break
        # print(len(recommended_products))
        print("this customer might also like: ")
        l = 0
        for i in recommended_products:
            print(i + " AT " + str(offers[randint(0,2)]) + '%' + ' OFF')
            l = l+1
            if l ==3:
                break

        print('========================================================================')
        c_id = int(input("select a customer id between 100 and 149 or 0 to exit: "))

    else:
        break
        
