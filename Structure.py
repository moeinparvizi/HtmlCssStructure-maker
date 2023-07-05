import os

class CheckingReturn:
	def __init__(self, files_count):
		self.files_count = files_count

	def files_count_f(self):
		count_dic = {}
		if files_count > 10:
			return True
		else:
			for i in range(files_count):
				count_input_name = input("whats your name of page? ")
				count_input_asw = input("whats is your title? ")
				count_dic[count_input_name] = count_input_asw
			return count_dic

	def creative_folder():
		name_root = input('enter your name of project')
		os.mkdir(name_root)
		name_f = name_root + '/assets'
		os.mkdir(name_f)
		name_f1 =  name_f + '/styles'
		os.mkdir(name_f1)
		name_f1 = name_f + '/media'
		os.mkdir(name_f1)
		name_f2 = name_f1 + '/images'
		os.mkdir(name_f2)
		name_f2 = name_f1 + '/videos'
		os.mkdir(name_f2)
		return name_root

	def creative_index(self, res_dict, name_project):
		for name,value in res_dict.items():
			name = name_project+"/"+name+".html"
			files = open(name, "w")
			files.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>%s</title>\n    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;700&display=swap" rel="stylesheet">\n    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">\n    <link rel="stylesheet" href="assets/styles/master.css"></head>\n<body>\n</body>\n</html>'%(value))
			files.close()

files_count = int(input("how many files you want? "))

result = CheckingReturn(files_count)

result_files_count = result.files_count_f()

if result_files_count == True:
	print("try again\nyour number is big")
else:
	name_of_project = CheckingReturn.creative_folder()
	result_end = result.creative_index(result_files_count,name_of_project)
	print("done")
