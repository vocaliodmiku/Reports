import glob

files = glob.glob("/Users/penglinkai/Reports/docs/static/Trial_20250207_5spk/figs/*")
files = sorted(files)
for file in files:
    fname=file.split("/")[-1]
    title=file.split("/")[-1].split(".")[0]
    line =  '{filename: "figs2/' + fname + '}",title: "' +  title + '"}' 
    print(line)