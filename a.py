s="54367+-*+"
st=[]
for i in s:
    if i.isdigit():
        st.append(int(i))
    else:
        a=st.pop()
        b=st.pop()
        if i =="+":
            st.append(a+b)
        elif i=="-":
            st.append(a-b)
        elif i=="*":
            st.append(a*b)
print(st)