##    سال کبیسه
year = int(input("sal ra vared konid:")) 
if year%400==0:
    print(year," kabise ast")
elif year%100==0:
    print(year,"kabise nist ")
elif year%4==0:
    print(year, "  kabise ast")
else:
    print(year, "kabise nist ")
########################################
#   مثبت / منفی / صفر
adad=int(input("adaravared konid"))
if adad>0:
    print("adad mosbate")
elif adad<0:
    print("adad manfiye")
else:
    print("adad sefre")
##############################################
        ## ## #مثلث تشخیص# ## ##
a=float(input("zela1="))
b=float(input("zela2="))
c=float(input("zela3="))
    # --- پیدا کردن بزرگ‌ترین ضلع ---
if a>=b and a>=c:
    z=a
    y=b
    x=c
elif b>=a and b>=c:
    z=b
    y=a
    x=c
else:
    z=c
    y=b
    x=a
# --- بررسی مثلث ---
if x+y>z:
    print("moslas")
 # --- نوع مثلث ---   
    if a==b and b==c:
        print("motsaviazlae")
    elif a==b or b==c or c==a:
       print("motesaviolsaghein")
    else:
       print("mokhtalefolazlae")
    # --- قائم‌الزاویه؟ ---#
    if x**2 + y**2==z**2:
       print("ghaemzavie ast")
    else:
       print("ghaemzavie nist")
else:
   print("mosalas nist")

       