def primary():
  import random
  #print("Keep it logically awesome.")


  f = open("quotes.txt")
  quotes = f.readlines()
  #f.write ("Le boss est de retour - ", random.randint(1, 300))
  f.close()

  print ("il y a ", len(quotes),"citations")
  #print(quotes[3].replace("\n", ""),quotes[4].replace("\n", ""))
  compteur = 0
  for x in quotes:
  	compteur +=1
  	print (compteur,"- ", x.replace("\n", ""))

  f = open("quotes.txt", "a")
  citation = "Le boss est de retour - " + str(random.randint(1, 300)) +"\n"
  f.write (citation)
  f.close()


if __name__== "__main__":
  primary()
