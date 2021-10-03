

def TruncatCorreos(email):
    x = email.find("@")
    print(email[slice( x + 1,len(email),1)])
      
    
TruncatCorreos("hola@gmail.com")    
