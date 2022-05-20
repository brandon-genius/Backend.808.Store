


def test_dict():
    print("dictionary")

    me = {
        "first_name": "Brandon",
        "last_name": "Britt",
        "age": 30,
        "address": {
            "num": 1200,
            "street": "Queen Emma",
            "city": "Honolulu"
        }
    }

    print(me["first_name"] + " " + me["last_name"])

    #modify
    me["age"] = me["age"] +1
    

    #add new key
    me["color"] = "green"

    #remove key
    #del me["age"]

    #print address
    print(me["address"])

    #print street, num, city
    address = me["address"]
    print(address["street"] + "# " + str(address["num"]) + ", " + address["city"])

    #last, first
    print(f"{me['last_name']}, {me['first_name']}")


    print(f"Hi my name is {me['first_name']} {me['last_name']}, and I'm {me['age']} years old.")


    # read a key that doesn't exist

    try:
        print(me['xyz'])
    except:
        print("unexpected error")


    #check for key
    if "xyz" in me:
        print(me["xyz"])

    

test_dict()