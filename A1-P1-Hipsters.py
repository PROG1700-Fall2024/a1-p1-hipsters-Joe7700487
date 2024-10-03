#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # init variables
    deliveryRate = 15
    taxRate = 0.14
    deliveryCost = float
    totalCost = float
    # get name, distance and cost from the user
    name = input("Enter name: ")
    distance = float(input("Enter distance in km: "))
    cost = float(input("Enter cost: "))

    # calculate the cost plus tax
    cost = cost + (cost * taxRate)
    # calculate the deliver cost
    deliveryCost = deliveryRate * distance
    # add the cost and deliver together
    totalCost = cost + deliveryCost

    # output all the different costs
    print("Purchase summary for", name)
    print("Delivery cost: ${0:.2f}".format(deliveryCost))
    print("Purchase cost: ${0:.2f}".format(cost))
    print("Total cost: ${0:.2f}".format(totalCost))
main()