import sys
import io
import string
import random


class IO:
    
    def __init__(self,device):
        
        self.device = device
        
    
    def write(self,data):
        self.fd = io.open(self.device,"w")
        self.fd.write(data)
        self.fd.close()
        
    def read(self,size):
        self.fd = io.open(self.device,"r")
        read_data = self.fd.read(size)
        self.fd.close()
        return read_data
        
    
    def __del__(self):
        
        #print "In destructor"
        self.fd.close()
        


class IO_Random:
    
    def __init__(self,device):
        self.io = IO(device)
    
    def random_string_generator(self,size):
        
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        
        return unicode(''.join(random.choice(chars) for _ in range(size)))
    
    
    def fire(self):
        
        random_string = self.random_string_generator(512)
        
        # Write on device
        self.io.write(random_string)
        
        read_string = self.io.read(512)
        


if __name__ == "__main__":
    
    
    device = sys.argv[2]
    
    pattern = sys.argv[1]
    
    
    if pattern == "random":
        
        random_obj = IO_Random(device)
        random_obj.fire()