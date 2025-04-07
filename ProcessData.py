#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    #print(data)
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    
    major = data[6]
    majorShort = major[0:3]
    #print(majorShort)

    if year == "Freshman":
      yearAbbr = "FR"
    elif year == "Sophomore":
      yearAbbr = "SO"
    elif year == "Junior":
      yearAbbr = "JR"
    elif year == "Senior":
      yearAbbr = "SR"

    majorYear = majorShort + "-" + yearAbbr

    #print(majorYear)

    student_id = makeID(first, last, idNum)
    output = last + "," + first + "," + student_id + "," + majorYear + "\n"
    outFile.write(output)

    #print(student_id)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()


def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]
  #print(id)
  return id


if __name__ == '__main__':
  main()
