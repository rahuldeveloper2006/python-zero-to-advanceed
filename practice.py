import shutil
import os
#shutil.copy("practice.py","garbage.py")
# total,used,free=shutil.disk_usage("/")
# print("Total : ",total)
# print("used : ",used)
# print("Free : ",free)

# total_size=0
# path=input("enter your path")
# files=os.listdir(path)
# for file in files:
#     full_path=os.path.join(path,file)
#     if os.path.isfile(full_path):
#         size=os.path.getsize(full_path)
#         total_size=total_size+size
#         print(f"{file} : {size} bytes")
# print("\n total folder size is : ",total_size,"bytes")


# total_size=0
# path=input("enter your path")
# for root,dirs,files in os.walk(path):
#     for file in files:
#         full_path=os.path.join(root,file)
#         if os.path.exists(full_path):
#             size=os.path.getsize(full_path)
#             total_size=total_size+size
#             print(f"{file} : {size} bytes")
# print("\n total folder size is : ",total_size,"bytes")

import time

size=20
l1=list(range(size))
l2=list(range(size))
start=time.time()
add=[x+y for x,y in zip(l1,l2)]
end=time.time()
print(end-start)
print(add)