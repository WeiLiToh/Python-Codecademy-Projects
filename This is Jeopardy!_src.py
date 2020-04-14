import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv("jeopardy.csv")

#format jeopardy column names
#print(jeopardy.columns)

jeopardy = jeopardy.rename(columns={" Air Date":"Air Date"," Round":"Round"," Category":"Category"," Value":"Value"," Question":"Question"," Answer":"Answer"})

#print(jeopardy.columns)

def filtered_data (words, data):
  #jeopardy_filtered is a boolean array for the column "Question"
  jeopardy_filtered = data.Question.apply(lambda x: all(word.lower() in x.lower() for word in words))
  #returns the column where condition is True 
  return data.loc[jeopardy_filtered]
#return data.Question.loc[jeopardy_filtered] returns the exact column where all condition is True.

filtered_ke = filtered_data(["King", "England"], jeopardy)

print(filtered_ke["Question"])

#narrow down the column value we are looking for by specifying it's name

#String surgery 
jeopardy["Value"]  = jeopardy.Value.str.replace("$","")

jeopardy["Value"]  = jeopardy.Value.str.replace(",", "")
                                              
jeopardy["Value"] = jeopardy.Value.replace("None",0)
                                                
jeopardy["Value"] = pd.to_numeric(jeopardy["Value"]) 

filtered_k = filtered_data(["King"], jeopardy)

print(filtered_k["Value"].mean())

def get_answer_counts(data):
    return data["Answer"].value_counts()

print(get_answer_counts(filtered_k))




 


      





  
