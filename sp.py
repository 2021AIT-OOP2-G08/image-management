import subprocess

print("MongoDBをインストールします")
subprocess.run("brew tap mongodb/brew", shell=True)
subprocess.run("brew install mongodb-community", shell=True)

print("pymongoをインストールします")
subprocess.run("pip install pymongo", shell=True)

print("nanoidをインストールします")
subprocess.run("pip install nanoid", shell=True)

print("MongoDbをリストアします")
subprocess.run("mongorestore --port 27017 --dir ./dump", shell=True)
