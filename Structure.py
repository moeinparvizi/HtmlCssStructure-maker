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
		name_root = input('enter your name of project: ')
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
			files.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>%s</title>\n    <link href="assets/styles/master.css" rel="stylesheet">\n</head>\n<body>\n</body>\n</html>'%(value))
			files.close()

	def css_creator(name_root):
		cssorsass = input('css or sass ?')
		if cssorsass == 'sass':
			fi = open(f'{name_root}/assets/styles/global.sass', 'w')
			fi.write(':root{font-size:10px;}\n*{margin : 0; padding : 0;box-sizing: border-box;}\nbody{font-size: 1.6rem;}\na,a:visited,\na::selection {color: black;text-decoration: none;}\nul{list-style-type: none;}')
			fi.close()
			fe = open(f'{name_root}/assets/styles/master.sass', 'w')
			fe.write('@import global;\n// you can write code here...')
			fe.close()
			masterq = input('do you want master.css? (yes or no)')
			if masterq == "yes":
				fi = open(f'{name_root}/assets/styles/master.css','w')
				fi.close()

		elif cssorsass == 'css':
			fi = open(f'{name_root}/assets/styles/master.css','w')
			fi.write(':root{font-size:10px;}\n*{margin : 0; padding : 0;box-sizing: border-box;}\nbody{font-size: 1.6rem;}\na,a:visited,\na::selection {color: black;text-decoration: none;}\nul{list-style-type: none;}')
			fi.close()
		else:
			print(f"{cssorsass} is not find")

try:
	files_count = int(input("how many html file you want? "))
	result = CheckingReturn(files_count)
	result_files_count = result.files_count_f()
except ValueError:
	print('you most be enter a number')


try:
	if result_files_count == True:
		print("try again\nyour number is big")
	else:
		try:
			name_of_project = CheckingReturn.creative_folder()
			result_end = result.creative_index(result_files_count,name_of_project)
			CheckingReturn.css_creator(name_of_project)
			print("done")
		except:
			print('you have a error Trye Again')
except NameError:
	print('an error ;(')
