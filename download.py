#program for download manager
import requests,pyperclip,time
start = time.time()
print("Downloading...")
try:
    res = requests.get(pyperclip.paste())
except:
    print('Invalid address in the clipboard')
    quit()
# if res.status_code == 200 :
#     print("Downloading...")
# else:
#     print("Download Failed")
#     quit()
end = time.time()
name = input("Enter name for the file: ")
download = open(name,'wb')

for chunk in res.iter_content(100000):
	download.write(chunk)
print("Download Complete:")
print("--- %s seconds ---" % (end - start))
download.close()



