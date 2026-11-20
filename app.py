import csv
idx = 0
add = {
    "item":[],
    "qty":[],
    "total":[]
}
with open("sales.csv", "r",newline="") as file:
    reader = csv.DictReader(file)
    bad = False
    idx = 0
    with open("filtered_sales.csv","w",newline="") as good_file:
        header = ["Customer","Item","Qty","Price Total"]
        good = csv.writer(good_file)
        idx = 0
        good.writerow(header)
        for row in reader:
            try:
                (row["Item"])[3]
                (row["Customer"])[3]
                int(row["Qty"]) > 1
                float(row["Price Total"]) > 1
                good.writerow(row.values())
            except ValueError,IndexError:
                print(f"row {idx +2} is bad")
            idx +=1
with open("filtered_sales.csv","r",newline="") as file:
    read = csv.DictReader(file)
    with open("sales_summary.csv","w",newline="") as file:
        write = csv.writer(file)
        for row in read:
            if row["Item"] in add["item"]:
                idx = add["item"].index(row["Item"])
                add[ "qty" ][ idx ] = int(add[ "qty" ][ idx ]) + int( row[ "Qty" ] )
                add[ "total" ][ idx ] = round(float(add[ "total" ][ idx ]) + float(row[ "Price Total" ]), 2)
            else:
                add["item"].append((row["Item"]).title().strip())
                add["qty"].append(row["Qty"])
                add["total"].append(row["Price Total"])
                idx +=1
        for x in add:
            print(add[x])