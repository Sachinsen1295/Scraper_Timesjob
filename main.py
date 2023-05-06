from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

print('Put some skills which you are not famaliar with')
unfamaliar_skill = input('>')
print(f'filter out {unfamaliar_skill}')

def find_job():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    #jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    """for job in jobs:
        a = job.h3.text
        print(a)"""

    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
    #for job in jobs:
        job_published_date =  job.find('span',class_='sim-posted').text.strip()
        if 'few' in job_published_date:
            company_name  = job.find('h3',class_='joblist-comp-name').text.strip()
            skill_req = job.find('span', class_='srp-skills').text.strip()
            job_published_date =  job.find('span',class_='sim-posted').text.strip()
            #job_published_date =  job.find('span',text='Posted a month ago').text
            #job_description = job.find('ul',class_='list-job-dtl clearfix').li.text.strip()
            more_info = job.header.h2.a['href']

            if unfamaliar_skill not in skill_req:
                df=pd.DataFrame({"Index":index,"Company_Name":company_name,"Required skill":skill_req,'Job Date':job_published_date,"more info":more_info},index=[0])
                df.to_csv("Save.csv",mode='a',header=False)
            else:
                pass


            #print(job_published_date)
            #if unfamaliar_skill not in skill_req:

                # with open(f'post/{index}.txt','w') as f: 
                #     f.write(f'company name :{company_name} \n')
                #     f.write(f'Required skills :  {skill_req} \n')
                #     f.write(f'posted date :{job_published_date} \n')
                #     f.write(f'more info : {more_info} \n')
                # print(f'save file :{index}')

                    #print("company name :" ,company_name)
                    #print('Required skills : ', skill_req)
                    #print('Job Description :', job_description)
                    #print('posted date :' ,job_published_date)
                    #print(f'more info : {more_info}')

                #print("---"*20)

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'waiting {time_wait} minutes ....')
        time.sleep(time_wait * 60)