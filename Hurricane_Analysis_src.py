# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

billion = 10 ** 9
million = 10 ** 6
  
updated_damages = []
# write your update damages function here:
def damage (damages_list):
  
  for value in damages_list:
    if value == "Damages not recorded":
      updated_damages.append(value)
    elif "M" in value:
        x = value.strip("M").strip()
        updated_damages.append(float(x)*million) 
    else:
        y = value.strip("B").strip()
        updated_damages.append(float(y)*billion)
  return updated_damages

damage(damages)

# write your construct hurricane dictionary function here:
hurricanes = {}

def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  
  num_hurricanes = len(names)

  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Updated Damages": updated_damages[i],
                          "Deaths": deaths[i]}
  return hurricanes

create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# write your construct hurricane by year dictionary function here:
keys_for_hurricane = {}

def years_as_keys(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  
  num_hurricanes = len(years)

  for i in range(num_hurricanes):
    keys_for_hurricane[years[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Updated Damages": updated_damages[i],
                          "Deaths": deaths[i]}
  return keys_for_hurricane
    
years_as_keys(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

#print(keys_for_hurricane[1924])

count_areas_affected = {}

# write your count affected areas function here:
#count_affected_areas returns the dictionary value consisting of number of times an area is affected by a hurricane.
def count_affected_areas(area_selected, areas_affected):
  count = 0
  for area in areas_affected:
    for each_area in area:
      if each_area == area_selected:
        count += 1
        count_areas_affected[area_selected] = count
  return count_areas_affected

count_affected_areas("Central America", areas_affected) 

#returns count for comparison in most_affected_area function
def count_areas(area_selected, areas_affected):
  count = 0
  for area in areas_affected:
    for each_area in area:
      if each_area == area_selected:
        count += 1
  return count

#print(count_areas_affected["Central America"])

# write your find most affected area function here:
def most_affected_area(count_areas_affected):
  area_affected_count = 0
  area_most_affected = "Central America"
  for areas in areas_affected:
    for each_area in areas:
      if count_areas(area_most_affected, areas_affected) > area_affected_count:
        area_affected_count = count_areas(each_area, areas_affected)
        area_most_affected = each_area
  return area_most_affected, area_affected_count

list_of_deaths = []
#print(most_affected_area(areas_affected))
# write your greatest number of deaths function here:
def greatest_number_of_deaths(hurricane_dic):
  most_deaths = 0
  most_fatal_hurricane = ""
  
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Deaths"] > most_deaths:
      most_deaths = hurricanes[hurricane]["Deaths"]
      most_fatal_hurricane = hurricane
  return most_fatal_hurricane, most_deaths

#print(greatest_number_of_deaths(hurricanes))

mortality_scale = {}

# write your catgeorize by mortality function here:
def mortality_rate(hurricanes): 
  zero_list = []
  one_list = []
  two_list = []
  three_list = []
  four_list = []
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Deaths"] <= 100:
      zero_list.append(hurricane)
    elif hurricanes[hurricane]["Deaths"] <= 500:
      one_list.append(hurricane)
    elif hurricanes[hurricane]["Deaths"] <= 1000:
      two_list.append(hurricane)
    else:
      three_list.append(hurricane)
    mortality_scale = {0:zero_list,
                       1:one_list,
                       2:two_list,
                       3:three_list}
  return mortality_scale
      
#print(mortality_rate(hurricanes))

# write your greatest damage function here:
def greatest_damage(hurricanes):
  greatest_damage = 0
  worst_hurricane = ""
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Updated Damages"] == "Damages not recorded":
      continue
    elif hurricanes[hurricane]["Updated Damages"] > greatest_damage:
      greatest_damage = hurricanes[hurricane]["Updated Damages"]
      worst_hurricane = hurricane
  return greatest_damage, worst_hurricane  
    
#print(greatest_damage(hurricanes)) 
damage_scale = {}
# write your catgeorize by damage function here:
def rate_hurricanes(hurricanes):
  rating_zero = []
  rating_one = []
  rating_two = []
  rating_three = []
  rating_four = []
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Updated Damages"] == "Damages not recorded":
      rating_zero.append(hurricane)
    elif hurricanes[hurricane]["Updated Damages"] <= 100000000:
      rating_one.append(hurricane)
    elif hurricanes[hurricane]["Updated Damages"] <= 1000000000:
      rating_two.append(hurricane)
    elif hurricanes[hurricane]["Updated Damages"] <= 10000000000:
      rating_three.append(hurricane)
    elif hurricanes[hurricane]["Updated Damages"] <= 50000000000:
      rating_four.append(hurricane)
    mortality_scale = {0:rating_zero,
                       1:rating_one,
                       2:rating_two,
                       3:rating_three,
                       4:rating_four}
  return mortality_scale
    
print(rate_hurricanes(hurricanes))     
      