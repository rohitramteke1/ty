import dns.resolver
   
# Finding A record 
result = dns.resolver.resolve('geeksforgeeks.org', 'A') 
   
# Printing record 
for val in result: 
    print('A Record : ', val.to_text()) 
