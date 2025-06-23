# The `page` is the adress where you are getting cloudfare captcha

# Locate an element using a CSS selector with a timeout of 10 seconds
# The element is under some specific structure identified by #PKVDd5
a = page.ele("css:#PKVDd5 > div > div", timeout=10)

# Search within element 'a' for a sub-element whose 'src' attribute starts with the specified Cloudflare URL
# This could be looking for a challenge iframe or image from Cloudflare
i = a.sr("@src^https://challenges.cloudflare.com/cdn-cgi",  timeout=10)

# Get the 'body' element inside the found iframe/document
body = i.ele('tag:body')

# If the body exists, proceed to look for elements with class '.cb-i', likely related to checkbox or interaction
if body:
    # Search for one more sr with class '.cb-i' (a checkbox in a Cloudflare challenge)
    e = body.sr('.cb-i')
    
    # Wait for 2 seconds before interacting; gives time for rendering or animations
    sleep(2)
    
    # Click on the found element, possibly solving the challenge
    e.click()
