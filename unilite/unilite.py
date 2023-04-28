import argparse
import os
import random
import shutil
import zipfile
from prompt_toolkit.shortcuts import ProgressBar


def create_zip(folder_name, size_percentage, zip_name, delete_after_zip):
	folder_size = sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(folder_name) for filename in filenames)
	zip_size = int(((size_percentage) / 100) * folder_size)

	with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
		with ProgressBar() as pb:
			for dirpath, dirnames, filenames in pb(os.walk(folder_name)):
				for filename in filenames:
					file_path = os.path.join(dirpath, filename)
					file_size = os.path.getsize(file_path)
					with open(file_path, 'rb') as file:
						file_data = file.read()
					if file_size <= zip_size:
						zip_file.write(file_path)
						zip_size -= file_size
						os.remove(file_path)
						if zip_size <= 0:
							break
				if zip_size <= 0:
					break

	if delete_after_zip:
		shutil.rmtree(folder_name)

def main():
	parser = argparse.ArgumentParser(description='Create zip file and delete some files from a folder before zipping it')
	parser.add_argument('source_folder', help='Folder yang ingin di-zip')
	parser.add_argument('-r', '--rate', type=int, default=10, help='Persentase ukuran folder yang ingin disimpan (default: 10)')
	parser.add_argument('-o', '--output', default='output.zip', help='Nama file zip yang akan dihasilkan (default: output.zip)')
	parser.add_argument('-df', '--delete_folder', action='store_true', help='Opsi untuk menghapus folder setelah selesai di-zip')
	args = parser.parse_args()

	create_zip(args.source_folder, args.rate, args.output, args.delete_folder)


if __name__ == '__main__':
	main()
