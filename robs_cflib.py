#########################################################################################################
# robs-cflib.py                                                                                         #
# v1.1.0                                                                                                #
# Created 22 Dec 2019                                                                                   #
# Last Modified 28 Aug 2020                                                                             #
#                                                                                                       #
# Robert Goldstein                                                                                      #
# rsg@pobox.com                                                                                         #
#                                                                                                       #
# This is a python library script of various overlay functions used to return CloudFlare outputs back   #
# to the calling program/script. This library needs cf-variables to have the main url, and other        #
# authC and authZ requirements for performing the CloudFlare API calls.                                 #
#                                                                                                       #
# Note: Each CloudFlare function will crash the program/script if there is not a succesful return from  #
#       the CF API. This will provide a means of direct troubleshooting vs trying to sort the issue     #
#       especially when performing large bulk operations.                                               #
#                                                                                                       #
# Bug fixes - 1.1.0 adjusted getcfAccountID to account for the fact that the account in question        #
#           may not always be the first one in the retrieval. Additionally, adjust requests calls to    #
#           not verify SSL/TLS certificates, which is default...because of SSL/TLS decrypt calls from   #
#           man-in-the-middle Zscaler inspections. If need to disable verification run python with      #
#           -W ignore flag to ignore the warning messages able doing this                               #
#                                                                                                       #
#########################################################################################################

""" This is a python library script of various overlay functions used to return CloudFlare outputs back
to the calling program/script. This library needs cf-variables to have the main url, and other        
authC and authZ requirements for performing the CloudFlare API calls.                                 
                                                                                                      
Note: Each CloudFlare function will crash the program/script if there is not a succesful return from  
      the CF API. This will provide a means of direct troubleshooting vs trying to sort the issue     
      especially when performing large bulk operations.                                               
  """
import sys
import requests
import json
from gdcfvars import cf_variables

# CFgetCall Function
# uses the request.get function to call CloudFlare API get functions
# returns status of the call
def CFgetCall(url='', getParams="", getHeaders={}):
    """CFgetCall(url, getParams="", getHeaders)

        Uses the requests.get function to call CloudFlare API get functions

        It references global variables:
        - cfurlmain : root CloudFlare URL

        It takes the following variables:
        - url (string): substring component / API tree portions
            to complete the API invocation
        - getParams (dictionary, default "" / empty) : The 
            ?<component1>=<value1>&<component2>=<value2>... items
        - getHeaders : Those items that authenticate and permit
            the API call to be used + specifying the Content-Type
            of input/outputs to the API call
            
        Returns json version of get request response
    """

    getURL = cf_variables.cfurlmain + url

    try:
        r = requests.get(url=getURL, params=getParams, headers=getHeaders, verify=False)
        #r = requests.get(url=getURL, params=getParams, headers=getHeaders)
    except requests.exceptions.SSLError as err:
        print("SSL Error...Certificate Pinning issue has occurred, handle request differently...")
        sys.exit(-1)
    except Exception as exception:
        print ("Exception occurred using get API Call: " + getURL + " with exception" + exception)
        sys.exit(-1)
    
    data = r.json()
    if(data['success'] == False):
        print("get API Call: " + getURL + " was unsuccessful for params: " + json.dumps(getParams) )
        print("returned data was: " + json.dumps(data))
        sys.exit(-1)

    return data


# CFputCall Function
# uses the request.post function to call CloudFlare API put functions
# returns status of the call
def CFputCall(url='', putData={}):
    """CFputCall(url, putData)

        Uses the requests.get function to call CloudFlare API get functions

        It references global variables:
        - cfurlmain : root CloudFlare URL

        It takes the following variables:
        - url (string): substring component / API tree portions
            to complete the API invocation
        - putData : Those need to be used to create or update the items
            related to the API call

        Returns json version of post request response
    """

    putURL = cf_variables.cfurlmain + url
    putHeaders = makeCFHeaders()

    try:
        r = requests.put(url=putURL, headers=putHeaders,data=json.dumps(putData),verify=False)
        #r = requests.put(url=putURL, headers=putHeaders,data=json.dumps(putData))
    except requests.exceptions.SSLError as err:
        print("SSL Error...Certificate Pinning issue has occurred, handle request differently...")
        sys.exit(-1)
    except Exception as exception:
        print ("Exception occurred using put API Call: " + putURL + " with exception" + exception)
        sys.exit(-1)

    data= r.json()
    if(data['success'] == False):
        print("put API Call: " + putURL + " was unsuccessful for data: " + json.dumps(putData) )
        print("returned data was: " + json.dumps(data))
        sys.exit(-1)

    return data

# CFpostCall Function
# uses the request.post function to call CloudFlare API post functions
# returns status of the call
def CFpostCall(url='', postData={}):
    """CFpostCall(url, postData)

        Uses the requests.get function to call CloudFlare API get functions

        It references global variables:
        - cfurlmain : root CloudFlare URL

        It takes the following variables:
        - url (string): substring component / API tree portions
            to complete the API invocation
        - postData : Those need to be used to create or update the items
            related to the API call

        Returns json version of post request response
    """

    postURL = cf_variables.cfurlmain + url
    postHeaders = makeCFHeaders()

    try:
        r = requests.post(url=postURL, headers=postHeaders,data=json.dumps(postData),verify=False)
        #r = requests.post(url=postURL, headers=postHeaders,data=json.dumps(postData))
    except requests.exceptions.SSLError as err:
        print("SSL Error...Certificate Pinning issue has occurred, handle request differently...")
        sys.exit(-1)
    except Exception as exception:
        print ("Exception occurred using post API Call: " + postURL + " with exception" + exception)
        sys.exit(-1)

    data= r.json()
    if(data['success'] == False):
        print("post API Call: " + postURL + " was unsuccessful for data: " + json.dumps(postData) )
        print("returned data was: " + json.dumps(data))
        sys.exit(-1)

    return data

# CFpatchCall Function
# uses the request.patch function to call CloudFlare API post functions
# returns status of the call
def CFpatchCall(url='', patchData={}):
    """CFpatchCall(url, patchData)

        Uses the requests.patch function to call CloudFlare API get functions

        It references global variables:
        - cfurlmain : root CloudFlare URL

        It takes the following variables:
        - url (string): substring component / API tree portions
            to complete the API invocation
        - patchData : Those need to be used to create or update the item
            related to the API call
            Note: Per review, one can only do a patch on a single item
                at a time.

        Returns json version of patch request response
    """

    patchURL = cf_variables.cfurlmain + url
    patchHeaders = makeCFHeaders()

    try:
        r = requests.patch(url=patchURL, headers=patchHeaders,data=json.dumps(patchData),verify=False)
        #r = requests.patch(url=patchURL, headers=patchHeaders,data=json.dumps(patchData))
    except requests.exceptions.SSLError as err:
        print("SSL Error...Certificate Pinning issue has occurred, handle request differently...")
        sys.exit(-1)
    except Exception as exception:
        print ("Exception occurred using patch API Call: " + patchURL + " with exception" + exception)
        sys.exit(-1)
    
    data = r.json()
    if(data['success'] == False):
        print("patch API Call: " + patchURL + " was unsuccessful for data: " + json.dumps(patchData) )
        print("returned data was: " + json.dumps(data))
        sys.exit(-1)

    return data

# CFdeleteCall Function
# uses the request.delete function to call CloudFlare API post functions
# returns status of the call
def CFdeleteCall(url=''):
    """CFdeleteCall(url)

        Uses the requests.delete function to call CloudFlare API get functions

        It references global variables:
        - cfurlmain : root CloudFlare URL

        It takes the following variables:
        - url (string): substring component / API tree portions
            to complete the API invocation
        Returns json version of patch request response
    """

    deleteURL = cf_variables.cfurlmain + url
    deleteHeaders = makeCFHeaders()

    try:
        r = requests.delete(url=deleteURL, headers=deleteHeaders,verify=False)
        #r = requests.delete(url=deleteURL, headers=deleteHeaders)
    except requests.exceptions.SSLError as err:
        print("SSL Error...Certificate Pinning issue has occurred, handle request differently...")
        sys.exit(-1)
    except Exception as exception:
        print ("Exception occurred using patch API Call: " + deleteURL + " with exception" + exception)
        sys.exit(-1)
    
    data = r.json()
    if(data['success'] == False):
        print("delete API Call: " + deleteURL + " was unsuccessful.")
        print("returned data was: " + json.dumps(data))
        sys.exit(-1)

    return data
# makes the CloudFlare Header dictionary for authentication
def makeCFHeaders(useToken=False):
    """makeCFHeaders(useToken=False)

        Creates and returns a dict variable, which has the
        CloudFlare Header info for any CF API Call

        It references global variables:
        - personalAPItoken (string): personal API token
        - personalAPIkey (string): personal API key
        - personalEmailid (string): personal email address / login id

        It takes the following variables:
        - useToken (boolean) : Because there is the potential 
            a CloudFlare may use the personal token or the 
            combination of email id and api key, a reference to
            know which to use is required.
           
        Returns dictionary variable of header information
    """
    if(useToken): 
        return dict({ "Authorization" : "Bearer " + cf_variables.personalAPItoken, "Content-Type": "application/json"})
    else: 
        return dict({ 'X-Auth-Email' : cf_variables.personalEmailid, 'X-Auth-Key' : cf_variables.personalAPIkey, 'Content-Type': 'application/json' })

# retreives personal id using token validation
def getPersonalcfID():
    """getPersonalcfID()

        Retrieves CloudFlare personal ID using the token
        validation API call

    """

    cfHeaders = makeCFHeaders(useToken=True)

    data = CFgetCall(url='user/tokens/verify', getHeaders=cfHeaders)
    cfid = data['result'][0]['id']

    return cfid

def getcfAccountID():
    """getcfAccountID()

        Retieves CloudFlare Account ID by reviewing personal
        user rights

    """

    cfHeaders=makeCFHeaders()
    cfaccountid=""
    i=0

    #print(cfHeaders)
    
    while(True):
        
        tmpOrg = (CFgetCall("user",getHeaders=cfHeaders))['result']['organizations'][i]
    
        if (tmpOrg['name'] == cf_variables.gbaccountName):
            cfaccountid = tmpOrg['id']
            break
        else: i += 1

    return cfaccountid
