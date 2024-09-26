#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    deliveryRate = 15
    taxRate = 0.14
    deliveryCost = float
    totalCost = float
    name = input("Enter name: ")
    distance = float(input("Enter distance in km: "))
    cost = float(input("Enter cost: "))

    cost = cost + (cost * taxRate)
    deliveryCost = deliveryRate * distance
    totalCost = cost + deliveryCost

    print("Purchase summary for", name)
    print("Delivery cost: ${0:.2f}".format(deliveryCost))
    print("Purchase cost: ${0:.2f}".format(cost))
    print("Total cost: ${0:.2f}".format(totalCost))
    # YOUR CODE ENDS HERE

main()