#Imports

try:
    from vista import registro
    from dotenv import load_dotenv
    import runpy
    import os
except Exception:
    print("Error: library not found")
    exit()

if(True):
    try:
        proof = os.path.join(os.path.dirname(__file__), "..\\controler\\registroController.py")
        print(proof)
        runpy.run_module(registro)
    except:
        print("path wrong")
        exit()