from bs4 import BeautifulSoup
import requests
import csv
import lxml
import time
import random


"""
give the url,file name
greetings,start scrapping,
hotel_name,
price,
ratings,
location,
reviews,
link,
save the file
"""

copenheagen="https://www.booking.com/searchresults.html?ss=Copenhagen%2C+Denmark&efdco=1&label=gen173nr-10CAEoggI46AdIM1gEaD2IAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4ApKCv8cGwAIB0gIkOWE1Y2MzNWMtNmI4Mi00YzAwLTlmZmMtMDIwMGIxODNjNmQz2AIB4AIB&sid=6d20968da55ab1301940b53b7fdc2df8&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2745636&dest_type=city&checkin=2025-10-17&checkout=2025-10-20&group_adults=2&no_rooms=1&group_children=0"

def web_scrapper2(url,f_name):
   print("thanl you for the url and file name")

   num=random.randint(3,7)

   #processing
   time.sleep(num)

   header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}

   response=requests.get(url,headers=header)

 
   if response.status_code==200:
     print(response.status_code)
     html_content =  response.text

     soup=BeautifulSoup(html_content,'lxml')
     # print(soup.prettify())


     hotel_divs=soup.find_all("div",role="listitem")
     with open(f'{f_name}.csv','w',newline='', encoding='utf-8')as file_csv:
        writer=csv.writer(file_csv)


        writer.writerow(['hotel_name','hotel_location','hotel_price','rating','total_review','link'])
        for hotel in hotel_divs:
         hotel_name_tag = hotel.find('div', class_="b87c397a13 a3e0b4ffd1")
         hotel_name = hotel_name_tag.text.strip() if hotel_name_tag else "NA"

         hotel_location_tag = hotel.find('span', class_="d823fbbeed f9b3563dd4")
         hotel_location = hotel_location_tag.text.strip() if hotel_location_tag else "NA"

         hotel_price_tag = hotel.find('span', class_="b87c397a13 f2f358d1de ab607752a2")
         hotel_price = hotel_price_tag.text.strip().replace('DKK','') if hotel_price_tag else "NA"

         rating_tag = hotel.find('div', class_="f63b14ab7a f546354b44 becbee2f63")
         rating = rating_tag.text.strip() if rating_tag else "NA"

         review_tag = hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879")
         total_review = review_tag.text.strip() if review_tag else "NA"

         link_tag = hotel.find('a', href=True)
         link = link_tag.get('href') if link_tag else "NA"

        #  in this code below we have not store the "na" value we wnat to check condition if true we wnat tha value to get correct value or else want na so we store the value and pass it to the csv file




        #  hotel_name=hotel.find('div',class_="b87c397a13 a3e0b4ffd1").text.strip()
        #  hotel_name if hotel_name else "NA"
        # #  is a short (one-line) conditional statement in Python.
        # # It’s called a ternary operator, and it works like this  its like if link has value use link if there is no value then use "NA" link if "jack" else "NA"
        #  hotel_location=hotel.find('span',class_="d823fbbeed f9b3563dd4").text.strip()
        #  hotel_location if hotel_location else "NA"
        #  hotel_price=hotel.find('span',class_="b87c397a13 f2f358d1de ab607752a2").text.strip().replace('DKK','')
        #  hotel_price if hotel_price else "NA"
        #  rating=hotel.find('div',class_="f63b14ab7a f546354b44 becbee2f63").text.strip()
        #  rating if rating else "NA"
        #  total_review=hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879").text.strip()
        #  total_review if total_review else "NA"
        #  link=hotel.find('a',href=True).get('href')
        #  link if link else "NA"
         writer.writerow([hotel_name,hotel_location,hotel_price,rating,total_review,link])
       
        print("saved sucessfully")
        

     # for hotel in hotel_divs:
     #     hotel_name=hotel.find('div',class_="b87c397a13 a3e0b4ffd1").text.strip()
     #     hotel_location=hotel.find('span',class_="d823fbbeed f9b3563dd4").text.strip()
     #     hotel_price=hotel.find('span',class_="b87c397a13 f2f358d1de ab607752a2").text.strip().replace('DKK','')
     #     rating=hotel.find('div',class_="f63b14ab7a f546354b44 becbee2f63").text.strip()
     #     total_review=hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879").text.strip()
     #     link=hotel.find('a',href=True).get('href')
     #     print(hotel_price)
     #     print(hotel_location)
     #     print(hotel_name)
     #     print(rating)
     #     print(total_review)
     #     print(link)
     #     print(" ")
 
   else:
     print(response.status_code)

if __name__=='__main__':
  url=input("please enter the url :")
  fn=input("please give file name :")
  web_scrapper2(url,fn)
     

