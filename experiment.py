n = 0
answers = []

def diff(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    l1 = []
    for i in range(len(w1) - 2):
        l1.append(w1[i:i + 2])
    l2 = []
    for j in range(len(w2) - 2):
        l2.append(w2[j:j + 2])
    res = len([key for key, val in enumerate(l1) if val in set(l2)])
    try:
        s = (2*res)/(len(l1)+len(l2))
    except:
        s = 0
    return s

def LD(s, t):
    s = s.lower()
    t = t.lower()
    """ 
        iterative_levenshtein(s, t) -> ldist
        ldist is the Levenshtein distance between the strings 
        s and t.
        For all i and j, dist[i,j] will contain the Levenshtein 
        distance between the first i characters of s and the 
        first j characters of t
    """

    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    # source prefixes can be transformed into empty strings 
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = i

    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = i
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                                 dist[row][col-1] + 1,      # insertion
                                 dist[row-1][col-1] + cost) # substitution

    #for r in range(rows):
    #    print(dist[r])
    
 
    return dist[row][col]

file_01 = open('C:\\Users\\emile\\Desktop\\python programs\\nl_experiment\\basiswoorden-gekeurd-da.txt')
lines_01 = file_01.readlines()
file_02 = open('C:\\Users\\emile\\Desktop\\python programs\\nl_experiment\\basiswoorden-gekeurd-sv.txt')
lines_02 = file_02.readlines()

for i in range(198960):
    ans = diff(lines_01[i], lines_02[i])
    answers.append(ans)
    print(i, ans)
    n = n + ans

print("Gemiddeld: " + str(n / 198960))

# import xlsxwriter module 
import xlsxwriter 
  
workbook = xlsxwriter.Workbook('C:\\Users\\emile\\Desktop\\python programs\\nl_experiment\\resultaten-temp.xlsx') 
worksheet = workbook.add_worksheet() 
  
# Start from the first cell. 
# Rows and columns are zero indexed. 
row = 0
column = 0

# iterating through content list 
for item in answers : 
  
    # write operation perform 
    worksheet.write(row, column, item) 
  
    # incrementing the value of row by one 
    # with each iteratons. 
    row += 1
      
workbook.close()