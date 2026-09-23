from datetime import datetime
#Allowed values for the multiple choice style fields
cats=["GEN","OBC","SC","ST","EWS"]
genders= ["M","F","T"]
papers= ["B.E","B.Tech","B.Arch","B.Planning"]

#Just checks the shape (YYYY-MM-DD), not that it's a real calendar date
def valid_dob(dob):
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def valid_category(cat):
    return cat.upper() in cats

def valid_gender(g):
    return g.upper() in genders

#Aadhaar (Indian ID) numbers are always 12 digits
def valid_aadhaar(a):
    return a.isdigit() and len(a) == 12

#Only allow a small whitelist of email domain
def valid_email(e):
    return "@gmail.com" in e or "@zoho.com" in e or "@vitbhopal.ac.in" in e or "@proton.me"  in e

def valid_mobile(m):
    return m.isdigit() and len(m)==10

def valid_pincode(p):
    return p.isdigit() and len(p)==6

# Note: case-sensitive, unlike category/gender
def valid_paper(p):
    return p in papers
