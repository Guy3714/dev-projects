School Weekly Plan – Exact Structure Explanation
🔹 The table has 4 columns total
Day
9–10
10–11
11–12
🔹 First Row (Header Row)
You will have 4 header cells:
Day
9–10
10–11
11–12
So this row has 4 separate <th> cells.
🔹 Second Row (Monday)
This row has 4 normal cells:
Monday
Math
Science
English
No rowspan or colspan here.
🔹 Third Row (Tuesday)
This row works like this:
First cell → Tuesday
Second cell → Hindi
Third cell → Lab (2 Hours)
Now important part:
👉 “Lab (2 Hours)” should cover 10–11 and 11–12
That means:
It replaces TWO cells
You must use colspan="2"
So Tuesday row has:
1 normal cell (Day)
1 normal cell (9–10)
1 cell with colspan="2"
Total visible columns still = 4.
🔹 Fourth Row (Wednesday)
This row works like this:
First cell → Wednesday
Second cell → Sports (3 Hours)
Now important:
👉 “Sports (3 Hours)” covers:
9–10
10–11
11–12
That means it replaces THREE cells.
So you must use:
colspan="3"
So Wednesday row has:
1 normal cell (Day)
1 cell with colspan="3"
Again total visible columns = 4.