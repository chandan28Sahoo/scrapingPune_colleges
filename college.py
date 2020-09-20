from bs4 import BeautifulSoup
from pprint import pprint as print
import requests,json,string,csv
with open("pune.html","r") as f:
    html=f.read()

soup = BeautifulSoup(html, "html.parser")

main=soup.find("div",class_="listing-content rightside")
div=main.find_all("div",class_="col-md-12")


links=[]
for i in div:
    x=i.find("div",class_="title").a["href"]
    y='https://www.collegedekho.com'+x
    links.append(y)
names=[]
list_of_data=[]
data1={}
count=0
for j in links:
    count+=1
    print(count)
   
    z=requests.get(j).text
    soup1 = BeautifulSoup(z, "html.parser")
    div=soup1.find("div",class_="infraList")
    try:
        div_s=div.find("table",class_="notScrollTable")
        di=div_s.find_all("td",class_="data")
    except AttributeError:
        pass

    type_of_str = di[0].text
    if type_of_str.isalpha():
        strp=(type_of_str)
    else:
        strp=" "

    try:
        df=soup1.find("div",class_="header collegeDetails")
        a=df.find("div",class_="collegeDesc")
        ab=a.find("h1",class_="tooltip").text.strip().split()
        st=""
        for i in ab:
            if i=='Pune':
                break
            else:
                st+=i
        clgs=st+"pune"
        print(clgs)
     
    except:
        pass
    
    list_facilities=""
    try:
        main=soup1.find("div",class_="block facilitiesBlock")
        sub=main.find("ul",class_="owl-acilities owl-carousel owl-theme")
        div=sub.find_all("div",class_="box")

    except AttributeError:
        pass

    for i in div:
        try:
            a1=i.text
            list_facilities+=(a1+" ")

        except AttributeError:
            a1=" "
            list_facilities+=(a1+" ")
  
    contact_n0=""
    contact_n1=""
    contact_n2=""
    contact_n3=""
    main1=soup1.find("div",class_="collegeContacts")
    main2=main1.find("ul",class_="addressList")
    for data in main2:
        label = data.find("div",class_="label")
        label=label.text.strip()
        if(label=="Contact No:"):
            labelData=data.find("div",class_="data")
            # c = [x for x in labelData.text.strip().split() if len(x)>7]
            for x in labelData.text.strip().split():
                if len(x)>7:
                    contact_n0+=x
                else:
                    contact_n0+=" "
        
        elif label=="Email ID:":
            labelData=data.find("div",class_="data")
            c=labelData.text.strip()
            contact_n1+=c
          
        elif label=="Website:":
            labelData=data.find("div",class_="data")
            c=labelData.text.strip()
            contact_n2+=c

        elif label=="Address:":
            labelData=data.find("div",class_="data")
            c=labelData.text.strip()
            contact_n3+=c

    data={}
    data["college name"]=clgs
    data["link"]=j
    data["college type"]=strp
    data["facilities"]=list_facilities
    data["contact_no"]=contact_n0
    data["Email_id"]=contact_n1
    data["Website"]=contact_n2
    data["Address"]=contact_n3
    list_of_data.append(data)
    data1["result"]=list_of_data

    with open('colleges.json','w+') as write_file:
        json.dump(data1,write_file,indent=2)
        write_file.close()

with open("colleges.json","r") as file:
    data=json.load(file)
  
with open("clg.csv","w+") as wr:
    w=csv.writer(wr)
    w.writerow(['college_name','link','college_type','facilities','contact_no','Email_id','Website','address'])
    for d in data["result"]:
        w.writerow([d['college name'],d['link'],d['college type'],d['facilities'],d['contact_no'],d['Email_id'],d['Website'],d['Address']])
 
