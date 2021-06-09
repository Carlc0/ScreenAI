#Imports

try:
    from vista import main
    from dotenv import load_dotenv
    import runpy
    import os
except Exception:
    print("Error: library not found")
    exit()

if(True):
    try:
        proof = os.path.join(os.path.dirname(__file__), "..\\controler\\mainController.py")
        print(proof)
        runpy.run_module(main)
    except:
        print("path wrong")
        exit()