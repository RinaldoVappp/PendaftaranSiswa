from os import system
from datetime import datetime
from json import load, dump

def view_menu():
	system("cls")
	menu =  """
APLIKASI 
[1] - SHOW EVERY ITEM
[2] - FIND ITEM
[3] - EDIT ITEM
[4] - REMOVE ITEM
[5] - ADD ITEM
[I] - ABOUT
[Q] - QUIT
	"""
	print(menu)

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def print_header(msg):
	system("cls")
	print(msg)

def create_item_id():
	today = datetime.now()
	year = today.year
	month = today.month
	thisday = today.day
	counter = len(item_data)+1
	barcode_id = str("%4s%02s%02s-C%03s" % (year, month, thisday, counter))
	return(barcode_id)

def print_item_data(barcode_id = None, all_fields = False, stock = True):
	if barcode_id != None and all_fields == False:
		print(f"""
			-DATA FOUND-
	ID \t: {barcode_id}
	Name \t:{item_data[barcode_id]["Name"]}
	Price \t:{item_data[barcode_id]["Price"]}
	Stock \t:{item_data[barcode_id]["Stock"]}
			""")
	elif barcode_id != None and stock == False:
		print(f"""
			-DATA FOUND-
	ID \t: {barcode_id}
	Name \t:{item_data[barcode_id]["Name"]}
	Price \t:{item_data[barcode_id]["Price"]}
			""")
	elif all_fields == True:
		for barcode_id in item_data:
			name = item_data[barcode_id]["Name"]
			price = item_data[barcode_id]["Price"]
			stock = item_data[barcode_id]["Stock"]
			print(f"ID:{barcode_id}\tNAME{name}\tPRICE:{price}\tSTOCK:{stock}")

def add_to_item_list():
	print_header("-ENTERING THE NEW DATA-")
	name = input("NAME\t:")
	price = input("PRICE\t:")
	stock = input("STOCK\t:")

	user_ans = input("Press Y to save the data(Y/N) : ")

	if verify_ans(user_ans):
		barcode_id = create_item_id()
		print("Saving...")
	
		item_data[barcode_id] ={
			"Name" : Name,
			"Price" : Price,
			"Stock" : Stock
		}
		save_data_apps()
		print("Data Saved")
	else:
		print("Data Unsaved")
	input("Press ENTER To Go Back")

def print_item():
	print_header("-ALL ITEMS-")
	if len(item_data) == 0:
		print("!THERE IS NOTHING HERE!")
	else:
		print_item_data(all_fields=True)
	input("Press ENTER To Go Back")

def searching_by_name(item):
	for barcode_id in item_data:
		if item_data[barcode_id]["Name"] == item:
			print_item_data(barcode_id=barcode_id)
			return barcode_id
	else:
		print("-DATA NOT FOUND-")
		return False

def get_barcode_id_from_name(item):
	for barcode_id in item_data:
		if item_data[barcode_id]["Name"] == item:
			return barcode_id

def searching_by_id(barcode_id):
	if barcode_id in item_data:
		print_item_data(barcode_id=barcode_id)
		return True
	else:
		print("-DATA NOT FOUND-")
		return False

def find_item():
	print_header("-FIND ITEM-\n")
	name = input("Item Name : ")
	result = searching_by_name(name)
	input("Press ENTER To Go Back")

def update_name(item):
	print(f"Old Name\t:{item}")
	new_name = input("New Name\t:")
	response = input("Are you sure? (Y/N):")
	if verify_ans(response):
		barcode_id = get_barcode_id_from_name(item)
		item_data[barcode_id]["name"] = new_name
		#del item_data[item]
		save_data_apps()
		print("Data Overwriten")
	else:
		print("Data Not Overwriten")

def update_price(item):
	barcode_id = get_id_contact_from_name(item)
	print(f"Nama \t:{item_data[barcode_id]['name']}")
	print(f"Old Price\t:{item_data[barcode_id]['price']}")
	new_telp = input("New Price\t: ")
	response = input("Are you sure? (Y/N):")
	if verify_ans(response):
		item_data[item]['price'] = new_price
		save_data_apps()
		print("Data Overwriten")
	else:
		print("Data Not Overwriten")

def update_stock(item):
	barcode_id = get_id_contact_from_name(contact)
	print(f"Name \t:{item_data[barcode_id]['name']}")
	print(f"Old Stock\t:{item_data[barcode_id]['stock']}")
	new_stock = input("New Stock\t: ")
	response = input("Are you sure? (Y/N)")
	if verify_ans(response):
		item_data[item]['stock'] = new_stock
		save_data_apps()
		print("Data Overwriten")
	else:
		print("Data Not Overwriten")

def update_item_list():
	print_header("OVERWRITE ITEM DATA\t")
	name = input("Item Name : ")
	result = searching_by_name(name)
	if result:
		print("Item Name : ")
		print("[1]. Name , [2]. Price , [3]. Stock")
		response = input("Choice :")
		if response == "1":
			update_name(name)
		elif response == "2":
			update_price(name)
		elif response == "3":
			update_stock(name)
	input("Press ENTER To Go Back")

def delete_item():
	print_header("-DELETE ITEM-")
	name = input("Item Name : ")
	result = searching_by_name(name)
	if result:
		response =input(f"Remove {result} ? (Y/N): ")
		if verify_ans(response):
			del item_data[result]
			save_data_apps()
			print("DATA Deleted")

		else:
			print("DATA Not Deleted")
	input("Press ENTER To Go Back")

def check_input(char):
	char = char.upper()
	if char == "Q":
		print("We Hope You to Meet Us Again!")
		return True
	elif char == "1":
		print_item()
	elif char == "2":
		find_item()
	elif char == "3":
		update_item_list()
	elif char == "4":
		delete_item()
	elif char == "5":
		add_to_item_list()
	elif char == "I":
		print("Just my first project :D")
	
def load_data_apps():
	with open(file_path, 'r') as document:
		item_data = load(document)
	return item_data

def save_data_apps():
	with open(file_path, 'w') as document:
		dump(item_data, document)

file_path = 'storage/stationary_stuff.json'
item_data = None
stop = False

item_data = load_data_apps()

while not stop:
	view_menu()
	user_input = input("Choice : ")
	stop = check_input(user_input)