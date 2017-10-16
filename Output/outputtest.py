
import Output as output

if __name__ == '__main__':
    
    try:
        output.init()
        
        
        for i in range(100):
            name = "name"+str(i)
            dat1 = int(i *2.5)
            dat2 = int(i *3.14)
            dat3 = int((dat1+dat2)/3)
            data =[name, 'xposition', dat1, 'yposition', dat2, 'distance', dat3]

            print("Sending...")
            print("data")
            output.out(data)
        
    finally:    
        output.close()
    
    pass