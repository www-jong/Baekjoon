
while True:
    arr=input()
    arrr=arr.lower()
    if arrr.find('nemo') != -1:
        print("Found")
    elif "eoi" in arrr and "EOI" in arr:
        break
    else:
        print("Missing")
