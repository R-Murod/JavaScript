from data import datas

orders = datas["orders"]

drivers = {}

categories = {}

for order in orders:
    dr_id = order["driver_profile"].get("id", "")
    dr_short_id = order.get("short_id", "0")
    dr_name = order["driver_profile"]["name"]
    mileage = order.get("mileage", "0")
    category = order.get("category", "")
    if dr_id not in drivers:
        drivers[dr_id] = {
                "order_count": 0,
                "fio": dr_name,
                "id": dr_id,
                "short_id": dr_short_id,
                "all_traffic": 0,
                "all_order_count": 0,
                "category": {}
            }
    if category not in drivers[dr_id]["category"]:
        drivers[dr_id]["category"][category] = 0
    drivers[dr_id]["category"][category] += 1
    if category not in categories:
        categories[category] = {
            "order_category_count": 0,
            "category_name": category
        }

    mileage = int(float(mileage))
    drivers[dr_id]["all_order_count"] += 1
    drivers[dr_id]["all_traffic"] += mileage
    categories[category]["order_category_count"]+=1


    if mileage > 2000:
        drivers[dr_id]["order_count"] += 1

#'FIO\t > 0 km \t kms \t > 2km \n'
result = ""
for d in drivers:
    dr = drivers[d]
    result += f'{dr["short_id"]}\t{dr["fio"]}\t{dr["all_order_count"]}\t{dr["all_traffic"]}\t{dr["order_count"]}\t{dr["category"]}\n'
for c in categories:
    ca = categories[c]
    result += f'{ca["category_name"]}\t{ca["order_category_count"]}\n'
print(result)

