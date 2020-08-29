# cloudflare
Cloudflare API Library

This API library permits someone working with Cloudflare to have a wrapper around the requests library.

It helps one to use the Cloudflare API Documentation, https://api.cloudflare.com/, in a similar manner to the examples, which are done using curl statements.

NOTHING in this library can or should be deemed as protected code by any organization.

The functions were developed to return the data from succesful attempts at running python scripts against the Cloudflare API.

It will crash/exit a program if there was an unsuccessful call made to the Cloudflare API so that appropriate syntax troubleshooting can be done.

If someone does not have the requests library, it can be found at https://github.com/psf/requests or https://pypi.org/project/requests/

The Library includes a variables file that can be uses to store all of the approrpiate credentials, which might be enabled or retrieved from a vault.

NOTES:

29 AUG 2020
The library has be updated to get passed python SSL/TLS verifications, which might occur because of the requests SSl/TLS inspection occuring related to SecaaS services such as Zscaler or Umbrella. When using this library with this disabled, you will need to run your python script with a "-W ignore" to hide the warning messages.

If you wish to re-enable SSL/TLS verifications, search for each r = request. line. You will find the appropriate other version below commented out. Simply comment the lines that have verify=False. (Line 66, 108, 149, 192, 230
