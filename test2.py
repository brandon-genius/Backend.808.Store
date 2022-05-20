
##### List
from mock_data import mock_catalog



def test_1():
    print("basic python list")

    nums = [1,2,3,4,5,4563456,4356456]

    #read
    print(nums[3])
    print(nums[1])

    #add
    nums.append(55)

    #remove by element
    nums.remove(4563456)

    #remove by index
    del nums[0]

    print(nums)


    #loop
    for n in nums:
        print(n)

def test_2():
    print("sum numbers")

    prices = [12.23,345,123.2,542,65,123.2,0.223,-23, 123.2,6,171,5678]

    #for loop and print all numbers
    #print the sumof all numbers
    #find the cheapest
    total=0
    cheapest =  prices[0]
    expensive = prices[0]
    for num in prices:
        total += num

        #compare
        if num < cheapest:
            cheapest = num

        #compare
        if num > expensive:
            expensive = num

        
    print(total)
    print(f"The cheapest price is: {cheapest}")
    print(f"the most expensive price is:{expensive}")

   
def test_3():
    print("cheapest product")

    #for print every dict/prod from catalog
    #print title of every product
    solution =mock_catalog[0]
    for prod in mock_catalog:
        print(prod["title"])
        if prod["price"] < solution["price"]:
            solution = prod


    #cheapest product - title
    print(f"the cheapest product is: {solution['title']} - ${solution['price']}")


    




#call

#test_1()
#test_2()
test_3()