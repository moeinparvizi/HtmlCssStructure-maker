import os

class checking_return:
	def __init__(self, files_count):
		self.files_count = files_count

	def files_count_f(self):
		count_dic = {}
		if files_count > 10:
			return "your number is bigs"
		else:
			for i in range(files_count):
				count_input_name = input("whats your name of page? ")
				count_input_asw = input("whats is your title? ")
				count_dic[count_input_name] = count_input_asw
			return count_dic

	def creative(self, res_dict):
		for name,value in res_dict.items():
			name = name+".html"
			files = open(name, "w")
			files.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>%s</title>\n    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;700&display=swap" rel="stylesheet">\n    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">\n    <link rel="stylesheet" href="assets/styles/master.css"></head>\n<body>\n</body>\n</html>'%(value))
			files.close()


files_count = int(input("how many files you want? "))

result = checking_return(files_count)

result_files_count = result.files_count_f()

print(result_files_count, True)


try:
	result_end = result.creative(result_files_count)
	print(result_end , "is your counter")
except AttributeError:
	print("try again")
except FileNotFoundError:
	print('we dont have this file')
# except:
# 	print('we have a new error report me please')