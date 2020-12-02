import os
import shutil

exclude = [ "co000" ]

output_path = os.path.realpath(".") + "/_output/"
total_pages = { }
total_lines = { }

def get_year(mod):
    if mod == "co572":
        return '3'
    return mod[2]

def scan(p, pre):
    dirs = list(os.listdir(p))
    dirs.sort()

    for d in filter(lambda x : os.path.isdir(x), dirs):
        if not (d[0:2] == "co" and d[2].isdigit()) or d in exclude:
            continue
        print("Copying " + p + "/" + d)
        year = "y" + get_year(d)
        shutil.copy(os.path.realpath(p + "/" + d) + "/main.pdf", output_path + year + "/" + pre + d + ".pdf")
        cmd = "pdfinfo " + p + "/" + d + "/main.pdf | grep 'Pages' | awk '{print $2}'"
        pages = int(os.popen(cmd).read().strip())
        lines = sum(1 for line in open(os.path.realpath(p + "/" + d) + "/main.tex"))
        total_pages[pre + year] = total_pages.get(pre + year, 0) + pages
        total_lines[pre + year] = total_lines.get(pre + year, 0) + lines
        print(d + ": " + str(pages) + " pages")
        print(d + ": " + str(lines) + " lines")

scan(".", "")
scan("tutorials", "t_")

print("Complete!")
print("Total pages:")
for key, val in total_pages.items():
    print("  " + key + ": " + str(val))
print("Total lines:")
for key, val in total_lines.items():
    print("  " + key + ": " + str(val))
