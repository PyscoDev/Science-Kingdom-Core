import os
from dotenv import load_dotenv

class Gatekeeper:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.dotenv_path = os.path.join(self.current_dir,'..','..','.env')

    def unlock(self,keytype):
        load_dotenv(self.dotenv_path)
        the_key = os.getenv(keytype)
        return the_key

if __name__=="__main__":

    Test_Gatekeeper=Gatekeeper()
    password = Test_Gatekeeper.unlock("Fake_Sudo")
    print(f"Password loaded successfully (hidden for security..... Naah you can have this one. The password is: {password}).")