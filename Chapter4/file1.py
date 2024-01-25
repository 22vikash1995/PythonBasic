msg1 = "Pay the attention with smile\n"
msg2="I tried but they wanted a lot of money\n"
msg3="Don't feel bad"
f=open("message",'w')
f.write(msg1)
f.write(msg2)
f.write(msg3)
f.close()
f=open('message','r')
data=f.read()
print(data)
f.close()
