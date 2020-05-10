from pathlib import Path
import copy
all_files = Path().glob("*.md")


def rewrite_theta(file_path):
    with open(file_path,'r',encoding="utf8") as infile:
        all_lines = list(infile.readlines())
    with open(file_path,'w',encoding="utf8",
              errors="replace") as out:
        for a_line in all_lines:
            new_line = copy.copy(a_line)
            if new_line.find('θ') > -1:
                print(f'hit it with {a_line}')
                new_line=a_line.replace('θ','theta')
            if new_line.find(r"\'") > -1:
                print(f'hit single quote {a_line}')
                new_line=new_line.replace(r"\'","'")
            out.write(new_line)

def rewrite_encoding(file_path):
    with open(file_path,'rb') as infile:
        all_bytes = infile.read()
    new_string = all_bytes.decode("utf8", errors="replace")
    with open(file_path,'w',encoding="utf8") as out:
        out.write(new_string)


for a_file in all_files:
    print(a_file)
    rewrite_theta(a_file.resolve())
    rewrite_encoding(a_file.resolve())
