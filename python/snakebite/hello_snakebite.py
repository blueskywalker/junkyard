from snakebite.client import Client
client = Client("trevally.amer.nevint.com", 9000, use_trash=False)
for x in client.ls(['/']):
    print x
