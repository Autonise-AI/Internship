# count the number of distict characters in a string
s = "elephant"
st = set()  # initialize with set command
lst = []
for c in s:
    st.add(c)

print(len(st))
