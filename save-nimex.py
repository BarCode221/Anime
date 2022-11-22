import os,sys,random,requests,threading

os.system("clear")
print('\33[35m')
logo = """
###########################|
#                           |                       +
#  TIER (0)    {python}      |                      |AUTO NGEHAREM
#     [Akbar]                 |DOWNLOAD ISTRI<=======
#           [Ramadhan]         |                    |ISTRI CLOUD
#                               |                   +
################################|
"""
print(logo)
print("\33[92m(!).input 1 generate 4 foto [downloads dari 4 website].(!)")
put = int(input("\33[97mJumlah Istri: "))
def wibu():
    for i in range(put):
        resp = requests.get("https://nekos.best/api/v2/neko")    
        resp2 = requests.get("https://api.waifu.im/random")
        resp3 = requests.get("https://api.waifu.pics/sfw/waifu")
        resp4 = requests.get("https://api.waifu.pics/sfw/neko")
        data = resp.json()
        data2 = resp2.json()
        data3 = resp3.json()
        data4 = resp4.json()
        op = data["results"][0]["url"]
        op2 = data2["images"][0]["url"]
        op3 = data3["url"]
        op4 = data4["url"]
        #save gambar
        tes = requests.get(op)
        name_file = random.randint(1, 1000)
        with open('%s.png' % name_file, 'wb') as f:
            f.write(tes.content)
            print("\33[33mSUCCESS SAVE TO GALERI =>",op)
        #save gambar2
        tes2 = requests.get(op2)
        name_file = random.randint(1, 1000)
        with open('%s.png' % name_file, 'wb') as f:
            f.write(tes2.content)
            print("\33[33mSUCCESS SAVE TO GALERI =>",op2)
        #save gambar3
        tes3 = requests.get(op3)
        name_file = random.randint(1, 1000)
        with open('%s.png' % name_file, 'wb') as f:
            f.write(tes3.content)
            print("\33[33mSUCCESS SAVE TO GALERI =>",op3)
        #save gambar4
        tes4 = requests.get(op4)
        name_file = random.randint(1, 1000)
        with open('%s.png' % name_file, 'wb') as f:
            f.write(tes4.content)
            print("\33[33mSUCCESS SAVE TO GALERI =>",op4)
if __name__=="__main__":
    wibu()
    requests.Session()
    
