import asyncio
import time

async def myWork():
    print("Starting Work")
    time.sleep(5)
    print("Ending Work")

def main():
   loop = asyncio.get_event_loop()
   loop.run_until_complete(myWork())
   loop.close()

if __name__ == '__main__':
   main()
