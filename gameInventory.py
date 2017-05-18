import csv

def display_inventory(inventory):
    print("Inventory:")
    amounts_inv_list = []
    for key in inventory:
        amounts_inv_list.append(inventory[key])
        print(str(inventory[key]) + " " + key)
    sum_of_inv = sum(amounts_inv_list)
    print("Total number of items: " + str(sum_of_inv))

def add_to_inventory(inventory, added_items):
    for thing in added_items:
        if thing in inventory:
            inventory[thing] = inventory[thing] + 1
        if thing not in inventory:
            inventory[thing] = 1
    return inv

def print_table(inventory, order=1): # order is: empty, "count,desc" or "count,asc"
    things_leng = len(max(inventory, key=len)) + 4
    amount_leng = 7
    sum_of_inv = []
    print("\nInventory:")
    print('count'.rjust(amount_leng) + 'item name'.rjust(things_leng))
    print("-" * (things_leng+amount_leng))
    if order == "count,asc":
        inv_sorted_keys = sorted(inventory, key=inventory.get, reverse=False)
    if order == "count,desc":
        inv_sorted_keys = sorted(inventory, key=inventory.get, reverse=True)
    if order == 1:
        inv_sorted_keys = inventory
    for thing in inv_sorted_keys:
        sum_of_inv.append(inventory[thing])
        print(str(inventory[thing]).rjust(amount_leng) + thing.rjust(things_leng))
    print("-" * (things_leng+amount_leng))
    print("Total number of items: " + str(sum(sum_of_inv)))

def import_inventory(inventory, filename=1):
    if filename == 1:
        final_import = open("import_inventory.csv", "r").read().split(',')
        final_import[-1] = final_import[-1].replace("\n", "")
        print(final_import)
        for thing in final_import:
            if thing in inventory:
                inventory[thing] = inventory[thing] + 1
            if thing not in inventory:
                inventory[thing] = 1
    else:
        final_import = open(filename, "r").read().split(',')
        final_import[-1] = final_import[-1].replace("\n", "")
        print(final_import)
        for thing in final_import:
            if thing in inventory:
                inventory[thing] = inventory[thing] + 1
            if thing not in inventory:
                inventory[thing] = 1
    return inventory

def export_inventory(inventory, filename=1):
    if filename == 1:
        writer = open("export_inventory.csv", "a")
        inv_export = []
        for key in inventory:
            writer.write("".join((key + ",") * inventory[key]))


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

inv = add_to_inventory(inv, dragon_loot)
inv = import_inventory(inv)
export_inventory(inv)
display_inventory(inv)

print_table(inv)
