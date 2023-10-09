import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('notices.xml')

root = tree.getroot()

published_date = []
awarded_date = []
title = []
description = []
awarded_company = []
company_address = []
awarded_value = []
url = []

for notice in root.findall('.//FullNotice'):
    published_date.append(notice.find('.//PublishedDate').text)
    awarded_date.append(notice.find('.//AwardedDate').text)
    title.append(notice.find('.//Title').text)
    description.append(notice.find('.//CpvDescription').text)
    awarded_company.append(notice.find('.//OrganisationName').text)
    company_address.append(notice.find('.//Address1').text)
    awarded_value.append(notice.find('.//Value').text)
    url.append(notice.find('.//WebAddress').text)

data = {
    'Publish Date': published_date,
    'Award Date': awarded_date,
    'Title': title,
    'Short Description': description,
    'Awarded Company': awarded_company,
    'Company Address': company_address,
    'Awarded Value': awarded_value,
    'URL': url
}

df = pd.DataFrame(data)

df.to_excel('task_2_output.xlsx', index=False)
