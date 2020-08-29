"""CloudFlare Variables for use by other libraries or scripts: 

   cfurlmain="https://api.cloudflare.com/client/v4/" <-- The main CloudFlare URL. At the time of       
           building this script, this was the main url.                                                
                                                                                                       
   personalAPItoken="<redacted>" <-- Your CloudFlare API token                                         
                                                                                                       
   personalAPIkey="<redacted>" <-- Your CloudFlare API key                                             
                                                                                                       
   personalEmailid="<redacted>" <-- The Email address associated to your CloudFlare account   

   accountName="<redacted>" <-- The name in the user account to search for the site records

   gbaccountName="<redacted>" <-- The name in the account name field to search for the site records

"""                                                                                               

global cfurlmain
global personalAPItoken
global personalAPIkey
global personalEmailid
global gbaccountName

cfurlmain="https://api.cloudflare.com/client/v4/"
personalAPItoken="<redacted>"
personalAPIkey="<redacted>"
personalEmailid="<redacted>"
gbaccountName="<redacted>"

if __name__ == '__main__':
    print ('This statement will be executed only if this script is called directly')