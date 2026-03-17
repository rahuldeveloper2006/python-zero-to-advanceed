# import time
# def function1():
#     time.sleep(2)
#     print("function 1 ")
# def function2():
#     time.sleep(2)
#     print("function 2")
# def function3():
#     time.sleep(2)
#     print("function 3")
# def main():
#     function1()
#     function2()
#     function3()
# main()
#here function 1 ,2 ,3 exicute one by one take time 2 seconds for each function
#but now we use 
import time
import asyncio
async def function1():
    await asyncio.sleep(1)
    print("function1 done")
async def function2():
    await asyncio.sleep(1)
    print("function 2done")
async def function3():
    await asyncio.sleep(4)
    print("function 3 done")

async def main():
    task=asyncio.create_task(function1())
    await function2()
    await function3()
    asyncio.run(main())
# async def main():
#     l =await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#        )
#     print(l)

    
