#Imports

try:
    from vista import registro
    from dotenv import load_dotenv
    import runpy
except Exception:
    print("Error: library not found")
    exit()

if(True):
    try:
        runpy.run_module(registro)
    except:
        print("path wrong")