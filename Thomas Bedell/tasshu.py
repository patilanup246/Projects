fout=open("data/csv_all/zillow_merged_file.csv","a")
# first file:
for line in open("data/csv_all/Zillow_Listing_0.csv"):
    fout.write(line)
# now the rest:
for num in range(1,50):
    f = open("data/csv_all/Zillow_Listing_"+str(num)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()