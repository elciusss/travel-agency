import os

def run_security_tests():
    os.system('bandit -r .')

    os.system('dependency-check --scan . --format ALL --out .')
    
if __name__ == "__main__":
    run_security_tests()