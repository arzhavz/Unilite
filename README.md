# Unilite
A powerful tool that can zip folders with a size that can be determined based on a percentage of their actual size by deleting random files XD

# Instalation
```sh
python setup.py install
```

# Usage
```sh
python -m unilite foldername
```

Add <code>-df</code> flags to delete folder after create zip file.
You can set name of output by add <code>-o output_name</code> and set the percentage by add <code>-r percentage</code>

Examples:
```sh
python -m unilite myfolder -r 20 -o myzip.zip -df
```
This will create a zip file from the myfolder folder and save it to a myzip file with a size of 20% of the original folder size. Then directly delete the initial folder.
