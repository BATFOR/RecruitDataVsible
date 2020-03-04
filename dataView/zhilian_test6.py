# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:09:29 2019

@author: 徐斌倩
"""
import time
import requests
import json
import random
import datetime
# import mysql.connector
import threading
import urllib.request as urllib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
mutex_lock = threading.Lock()
#import csv

class EmptyError(Exception):#自定义异常模块
    def __init__(self):
        self.str="无定义"
def get_ualist():#定制请求头
    ualist = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
              "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
              "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
              "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
              "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
              "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
              "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
              "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
              "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24" ]
    return ualist

def get_json(json_type):#json链接
    if json_type=="全部":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&_v=0.43805647&x-zp-page-request-id=702f598c26d4422dab4487077567e9ce-1561375967565-59122&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&_v=0.08285882&x-zp-page-request-id=5dbee3e89b79429b81338667cd418cd0-1561427590950-580473&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&_v=0.84229539&x-zp-page-request-id=6ca8b65190d84f6ba76b706bce3b3a78-1561427639204-649521&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=PHP&kt=3&_v=0.77647866&x-zp-page-request-id=ad766b671cc249e491427475ce5c13c1-1561427717246-715840&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.26935733&x-zp-page-request-id=2a464dff56d94245aceaafbf5234fc1c-1561427775006-883434&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Android&kt=3&_v=0.70506962&x-zp-page-request-id=dec0f1d5024e46549199cfecfe7171ec-1561427810520-619315&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%BE%8E%E5%B7%A5&kt=3&_v=0.25843809&x-zp-page-request-id=d6d120ade17b42e38c940ea6713a9fed-1561428019976-859715&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&_v=0.65199902&x-zp-page-request-id=772f02f6b31b424fbd56143437bc467b-1561428137360-813906&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.32126084&x-zp-page-request-id=d5f7bae8486f4cea998e881932115eaa-1561428167946-783898&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Hadoop&kt=3&_v=0.31026025&x-zp-page-request-id=5914460187114d989adbd8bc1e7c6f40-1561428205910-13049&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Node.js&kt=3&_v=0.06193946&x-zp-page-request-id=1b1aa6280fef493894190f001ba365f3-1561428245863-214520&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%BC%80%E5%8F%91&kt=3&_v=0.86253703&x-zp-page-request-id=a93011e4b0a8455b95f9340bd22ed72b-1561428281985-384269&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&_v=0.68691076&x-zp-page-request-id=0005f4970c64483bbaa737a55d7675bc-1561428315649-247494&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84&kt=3&_v=0.57123794&x-zp-page-request-id=a2d5327c36524fbaabce25ccb1ede75c-1561428344047-16394&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&kt=3&_v=0.85384198&x-zp-page-request-id=596e840d201e4498b67e843efdd0ad2c-1561428376372-511875&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%8C%BA%E5%9D%97%E9%93%BE&kt=3&_v=0.70664381&x-zp-page-request-id=447205a84abf4c698604310064897869-1561428411437-72494&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%94%B5%E6%B0%94%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.29670226&x-zp-page-request-id=0e07647c549f4b5fbb2e88970e93eda6-1561445379429-419361&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%94%B5%E5%AD%90%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.43381133&x-zp-page-request-id=c34950c49a69492db118a4b853d21523-1561445521128-367031&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=PLC&kt=3&_v=0.93342143&x-zp-page-request-id=bc7126f7263d413ba4054343fc06cc0d-1561445583837-429588&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.27712980&x-zp-page-request-id=8a58bcf6b35f4c92ac1994be5d1a3ba8-1561445642734-583581&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%AE%BE%E5%A4%87%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.95740762&x-zp-page-request-id=3829f15dbf784f9f9eb1cc10b324cea7-1561445694069-974699&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.73119676&x-zp-page-request-id=e7df354653f24840b43d2dfedda65e0a-1561445748286-255694&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%BB%93%E6%9E%84%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.55616875&x-zp-page-request-id=272565b0687f468c90cfca1ba857eb1e-1561446129108-652229&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%B7%A5%E8%89%BA%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.41084008&x-zp-page-request-id=ea153ef612ed47529c2c0758c96f49ce-1561446229059-964365&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&kt=3&_v=0.14466501&x-zp-page-request-id=c237bae9d569473593cd59e7b15d6ca1-1561446430469-692038&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%96%B0%E5%AA%92%E4%BD%93%E8%BF%90%E8%90%A5&kt=3&_v=0.52762528&x-zp-page-request-id=85b048d95eac4955b287ab52eeb385e9-1561446514230-907203&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BF%90%E8%90%A5%E4%B8%93%E5%91%98&kt=3&_v=0.43887845&x-zp-page-request-id=9e27d782a9494d33a0bb4b7f8bea651c-1561446690076-809941&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%98%E5%AE%9D%E8%BF%90%E8%90%A5&kt=3&_v=0.94565798&x-zp-page-request-id=d8ceb74f352d49d78dbcab02e9ccd20c-1561447253301-170874&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%A4%A9%E7%8C%AB%E8%BF%90%E8%90%A5&kt=3&_v=0.09939334&x-zp-page-request-id=1a500702102b4d8697a31732b139eb69-1561447438636-912695&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%A7%E5%93%81%E5%8A%A9%E7%90%86&kt=3&_v=0.86969356&x-zp-page-request-id=5c2087268a2d4df0b63af9542a8c5dfe-1561447680725-884492&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%A7%E5%93%81%E8%BF%90%E8%90%A5&kt=3&_v=0.04552793&x-zp-page-request-id=9f6d3f1d13be409798d8f73d7c50ca3d-1561447866038-713381&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%98%E5%AE%9D%E5%AE%A2%E6%9C%8D&kt=3&_v=0.05878136&x-zp-page-request-id=2dde9495cbeb46fab3467aec26f65801-1561447923508-956511&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B8%B8%E6%88%8F%E8%BF%90%E8%90%A5&kt=3&_v=0.89578496&x-zp-page-request-id=f0f2bef5efe9445fa9e30d3545375f72-1561448161240-46344&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0",
                  "pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%BC%96%E8%BE%91&kt=3&_v=0.01926327&x-zp-page-request-id=a104f381953b4e6d9b05f5d0cac907f7-1561448524665-84765&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="Java开发":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&_v=0.43805647&x-zp-page-request-id=702f598c26d4422dab4487077567e9ce-1561375967565-59122&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="UI设计师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&_v=0.08285882&x-zp-page-request-id=5dbee3e89b79429b81338667cd418cd0-1561427590950-580473&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="Web前端":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&_v=0.84229539&x-zp-page-request-id=6ca8b65190d84f6ba76b706bce3b3a78-1561427639204-649521&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="PHP":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=PHP&kt=3&_v=0.77647866&x-zp-page-request-id=ad766b671cc249e491427475ce5c13c1-1561427717246-715840&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="Python":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.26935733&x-zp-page-request-id=2a464dff56d94245aceaafbf5234fc1c-1561427775006-883434&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="Android":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Android&kt=3&_v=0.70506962&x-zp-page-request-id=dec0f1d5024e46549199cfecfe7171ec-1561427810520-619315&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="美工":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%BE%8E%E5%B7%A5&kt=3&_v=0.25843809&x-zp-page-request-id=d6d120ade17b42e38c940ea6713a9fed-1561428019976-859715&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="深度学习":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&_v=0.65199902&x-zp-page-request-id=772f02f6b31b424fbd56143437bc467b-1561428137360-813906&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="算法工程师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.32126084&x-zp-page-request-id=d5f7bae8486f4cea998e881932115eaa-1561428167946-783898&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="Hadoop":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Hadoop&kt=3&_v=0.31026025&x-zp-page-request-id=5914460187114d989adbd8bc1e7c6f40-1561428205910-13049&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="Node.js":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Node.js&kt=3&_v=0.06193946&x-zp-page-request-id=1b1aa6280fef493894190f001ba365f3-1561428245863-214520&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="数据开发":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%BC%80%E5%8F%91&kt=3&_v=0.86253703&x-zp-page-request-id=a93011e4b0a8455b95f9340bd22ed72b-1561428281985-384269&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="数据分析师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&_v=0.68691076&x-zp-page-request-id=0005f4970c64483bbaa737a55d7675bc-1561428315649-247494&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="数据架构":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84&kt=3&_v=0.57123794&x-zp-page-request-id=a2d5327c36524fbaabce25ccb1ede75c-1561428344047-16394&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="人工智能":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&kt=3&_v=0.85384198&x-zp-page-request-id=596e840d201e4498b67e843efdd0ad2c-1561428376372-511875&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="区块链":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%8C%BA%E5%9D%97%E9%93%BE&kt=3&_v=0.70664381&x-zp-page-request-id=447205a84abf4c698604310064897869-1561428411437-72494&x-zp-client-id=e6a0d1ba-f26b-42ff-b3ca-8fd4ee116513"]
    elif json_type=="电气工程师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%94%B5%E6%B0%94%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.29670226&x-zp-page-request-id=0e07647c549f4b5fbb2e88970e93eda6-1561445379429-419361&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="电子工程师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%94%B5%E5%AD%90%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.43381133&x-zp-page-request-id=c34950c49a69492db118a4b853d21523-1561445521128-367031&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="PLC":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=PLC&kt=3&_v=0.93342143&x-zp-page-request-id=bc7126f7263d413ba4054343fc06cc0d-1561445583837-429588&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="测试工程师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.27712980&x-zp-page-request-id=8a58bcf6b35f4c92ac1994be5d1a3ba8-1561445642734-583581&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="设备工程师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%AE%BE%E5%A4%87%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.95740762&x-zp-page-request-id=3829f15dbf784f9f9eb1cc10b324cea7-1561445694069-974699&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="硬件工程师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%A1%AC%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.73119676&x-zp-page-request-id=e7df354653f24840b43d2dfedda65e0a-1561445748286-255694&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="结构工程师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%BB%93%E6%9E%84%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.55616875&x-zp-page-request-id=272565b0687f468c90cfca1ba857eb1e-1561446129108-652229&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="工艺工程师":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%B7%A5%E8%89%BA%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.41084008&x-zp-page-request-id=ea153ef612ed47529c2c0758c96f49ce-1561446229059-964365&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="产品经理":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&kt=3&_v=0.14466501&x-zp-page-request-id=c237bae9d569473593cd59e7b15d6ca1-1561446430469-692038&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="新媒体运营":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%96%B0%E5%AA%92%E4%BD%93%E8%BF%90%E8%90%A5&kt=3&_v=0.52762528&x-zp-page-request-id=85b048d95eac4955b287ab52eeb385e9-1561446514230-907203&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="运营专员":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BF%90%E8%90%A5%E4%B8%93%E5%91%98&kt=3&_v=0.43887845&x-zp-page-request-id=9e27d782a9494d33a0bb4b7f8bea651c-1561446690076-809941&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="淘宝运营":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%98%E5%AE%9D%E8%BF%90%E8%90%A5&kt=3&_v=0.94565798&x-zp-page-request-id=d8ceb74f352d49d78dbcab02e9ccd20c-1561447253301-170874&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="天猫运营":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%A4%A9%E7%8C%AB%E8%BF%90%E8%90%A5&kt=3&_v=0.09939334&x-zp-page-request-id=1a500702102b4d8697a31732b139eb69-1561447438636-912695&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="产品助理":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%A7%E5%93%81%E5%8A%A9%E7%90%86&kt=3&_v=0.86969356&x-zp-page-request-id=5c2087268a2d4df0b63af9542a8c5dfe-1561447680725-884492&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="产品运营":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%A7%E5%93%81%E8%BF%90%E8%90%A5&kt=3&_v=0.04552793&x-zp-page-request-id=9f6d3f1d13be409798d8f73d7c50ca3d-1561447866038-713381&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="淘宝客服":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%98%E5%AE%9D%E5%AE%A2%E6%9C%8D&kt=3&_v=0.05878136&x-zp-page-request-id=2dde9495cbeb46fab3467aec26f65801-1561447923508-956511&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="游戏运营":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B8%B8%E6%88%8F%E8%BF%90%E8%90%A5&kt=3&_v=0.89578496&x-zp-page-request-id=f0f2bef5efe9445fa9e30d3545375f72-1561448161240-46344&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    elif json_type=="编辑":
        urlliste=["pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%BC%96%E8%BE%91&kt=3&_v=0.01926327&x-zp-page-request-id=a104f381953b4e6d9b05f5d0cac907f7-1561448524665-84765&x-zp-client-id=9c8b6b70-ffa9-46ed-8eb9-eea125edd4a0"]
    return urlliste

# def get_sql_conn():#获取操作数据库对象
#     mydb = mysql.connector.connect(
#                     host="xxx.xxx.xxx.xxx",
#                     user="root",
#                     passwd="root",
#                     database="zhaopin_test"
#                     )
#     mycursor = mydb.cursor()
#     return mydb,mycursor
filePath = ""
def write_txt(data_row):#写入日志
    # filePath  = settings.STATICFILES_DIRS[0]+"/zllog"+str(time.time())+".txt"
    #print("asda------------" + filePath)
    try:
        with open(filePath, 'a+',encoding='utf-8') as f:
          f.write(data_row)
    except Exception:
        pass


def data_analysis(info,name,post_type):#分析获取数据,数据处理
    # mydb,mycursor = get_sql_conn()
    for inf in info["data"]["results"]:
            mutex_lock.acquire()
            inf_record=""
            print(datetime.datetime.now())
            inf_record=inf_record+str(datetime.datetime.now())+"\n"
            print('子线程：{}正在爬取信息...'.format(name))
            inf_record=inf_record+str('子线程：{}正在爬取信息...\n'.format(name))
            try:
                strinf=inf["company"]["name"]
                if strinf=="":
                    raise EmptyError()
                company=strinf
            except EmptyError as e:
                company=e.str
                print("公司名字为空..")
                inf_record=inf_record+"公司名字为空..\n"
            try:
                strinf=inf["jobName"]
                if strinf=="":
                    raise EmptyError()
                job=strinf
            except EmptyError as e:
                job=e.str
                print("职位名称为空..")
                inf_record=inf_record+"职位名称为空..\n"
            try:
                strinf=inf["city"]["items"][0]["name"]
                if strinf=="":
                    raise EmptyError()
                city=strinf
            except EmptyError as e:
                city=e.str
                print("工作城市为空..")
                inf_record=inf_record+"工作城市为空..\n"
            try:
                job_place=""
                for i in range(1,len(inf["city"]["items"])):
                    job_place=job_place+inf["city"]["items"][i]["name"]+"-"
                strinf=inf["businessArea"]
                if strinf=="":
                    raise EmptyError()
                job_place=job_place+strinf
            except EmptyError as e:
                job_place=e.str
                print("工作地点为空..")
                inf_record=inf_record+"工作地点为空..\n"
            try:
                strinf=inf["workingExp"]["name"]
                if strinf=="":
                    raise EmptyError()
                job_experience=strinf
            except EmptyError as e:
                job_experience=e.str
                print("工作经验为空..")
                inf_record=inf_record+"工作经验为空..\n"
            try:
                strinf=inf["eduLevel"]["name"]
                if strinf=="":
                    raise EmptyError()
                education=strinf
            except EmptyError as e:
                education=e.str
                print("学历要求为空..")
                inf_record=inf_record+"学历要求为空..\n"
            try:
                scale=inf["company"]["size"]["name"]
            except:
                scale="无定义"
                print("公司规模信息出现异常..")
                inf_record=inf_record+"公司规模信息出现异常..\n"
            try:
                strinf=inf["jobType"]["items"][0]["name"]
                if strinf=="":
                    raise EmptyError()
                industry=strinf
            except EmptyError as e:
                industry=e.str
                print("行业领域为空..")
                inf_record=inf_record+"行业领域为空..\n"
            try:
                strinf=inf["salary"]
                if strinf=="":
                    raise EmptyError()
                #print("薪酬："+strinf)
                wage=strinf.split('-')
                min_wage=float(wage[0][:-1])
                #print("最低薪酬："+min_wage)
                max_wage=float(wage[1][:-1])
                #print("最高薪酬："+max_wage)
            except:
                #wage=e.str
                min_wage=0.0
                max_wage=0.0
                print("工资薪酬出现异常..")
                inf_record=inf_record+"工资薪酬出现异常..\n"
            try:
                strinf=inf["emplType"]
                if strinf=="":
                    raise EmptyError()
                job_duty=strinf
            except EmptyError as e:
                job_duty=e.str
                print("工作性质为空..")
                inf_record=inf_record+"工作性质为空..\n"
            try:
                strinf=','.join(inf["welfare"])
                if strinf=="":
                    raise EmptyError()
                job_benefits=strinf
            except EmptyError as e:
                job_benefits=e.str
                print("职位福利为空..")
                inf_record=inf_record+"职位福利为空..\n"
            try:
                strinf=inf["company"]["url"]
                if strinf=="":
                    raise EmptyError()
                website=strinf
            except EmptyError as e:
                website=e.str
                print("公司网址为空..")
                inf_record=inf_record+"公司网址为空..\n"
            try:
                strinf=inf["companyLogo"]
                if strinf=="":
                    raise EmptyError()
                logo=strinf
            except EmptyError as e:
                logo=e.str
                print("公司logo为空..")
                inf_record=inf_record+"公司logo为空..\n"
            try:
                strinf=inf["updateDate"]
                if strinf=="":
                    raise EmptyError()
                update_time=strinf
            except EmptyError as e:
                update_time=e.str
                print("职位更新时间为空..")
                inf_record=inf_record+"职位更新时间为空..\n"
            try:
                strinf=inf["company"]["number"]
                if strinf=="":
                    raise EmptyError()
                number=strinf
            except EmptyError as e:
                number=e.str
                print("公司编号为空..")
                inf_record=inf_record+"公司编号为空..\n"
            
            #print(pag)
            print("公司名字："+company)
            inf_record=inf_record+"公司名字："+company+"\n"
            print("职位名称："+job)
            inf_record=inf_record+"职位名称："+job+"\n"
            print("岗位类型："+post_type)
            inf_record=inf_record+"岗位类型："+post_type+"\n"
            print("工作城市："+city)
            inf_record=inf_record+"工作城市："+city+"\n"
            print("工作地点："+job_place)
            inf_record=inf_record+"工作地点："+job_place+"\n"
            print("工作经验："+job_experience)
            inf_record=inf_record+"工作经验："+job_experience+"\n"
            print("学历要求："+education)
            inf_record=inf_record+"学历要求："+education+"\n"
            print("公司规模："+scale)
            inf_record=inf_record+"公司规模："+scale+"\n"
            print("行业领域："+industry)
            inf_record=inf_record+"行业领域："+industry+"\n"
            #print("工资薪酬："+wage)
            print("最低工资薪酬："+str(min_wage))
            inf_record=inf_record+"最低工资薪酬："+str(min_wage)+"\n"
            print("最高工资薪酬："+str(max_wage))
            inf_record=inf_record+"最高工资薪酬："+str(max_wage)+"\n"
            
            print("工作性质："+job_duty)
            inf_record=inf_record+"工作性质："+job_duty+"\n"
            print("职位福利："+job_benefits)
            inf_record=inf_record+"职位福利："+job_benefits+"\n"
            print("公司网址："+website)
            inf_record=inf_record+"公司网址："+website+"\n"
            print("公司logo："+logo)
            inf_record=inf_record+"公司logo："+logo+"\n"
            print("职位更新时间："+update_time)
            inf_record=inf_record+"职位更新时间："+update_time+"\n"
            print("公司编号："+number)
            inf_record=inf_record+"公司编号："+number+"\n"
            print("--------------------")
            inf_record=inf_record+"--------------------"+"\n"
            write_txt(inf_record)
            mutex_lock.release()
            
            #存入mysql数据库
#            mutex_lock.acquire()
#            val = (number,company,scale,industry,website,logo,post_type,job,city,job_place,job_experience,education,min_wage,max_wage,job_duty,job_benefits,update_time)
#            write_mysql(mycursor,val,mydb)
#            mutex_lock.release()

def climb(url,pag,headers,post_type):#爬取页面信息
    r=requests.post(url,headers=headers,verify=False)
    if r.status_code==200:
        name = threading.current_thread().name
        mutex_lock.acquire()
        print(datetime.datetime.now())
        write_txt(str(datetime.datetime.now()))
        write_txt("\n")
        print('子线程：{}爬取网页成功!'.format(name))
        write_txt('子线程：{}爬取网页成功!\n'.format(name))
        mutex_lock.release()
        r.encoding='utf-8'
        info=json.loads(r.text)
        data_analysis(info,name,post_type)
    else:
        mutex_lock.acquire()
        print(datetime.datetime.now())
        write_txt(datetime.datetime.now())
        write_txt("\n")
        print("子线程：{}网页爬取失败...".format(name))
        write_txt("子线程：{}网页爬取失败...\n".format(name))
        mutex_lock.release()

def main(json_type,file):#json_type为爬取页面传入的爬取数据类型，比如全部，Java开发等等字符串
    global filePath
    filePath = file

    ualist=get_ualist()
    ua = random.choice(ualist)
    headers = {"Connection":"Keep-alive", "User-Agent":ua}
    urlliste=get_json(json_type)
    for i in range(len(urlliste)):
        urls="https://fe-api.zhaopin.com/c/i/sou?"
        urle=urlliste[i]
        post_lists=urle.split('&')
        for pos in post_lists:
            pos_str=pos.split('=')
            if pos_str[0]=='kw':
                post_type=urllib.unquote(pos_str[1])
        t = threading.Thread(target=climb,name='LoopThread'+str(i),args=(urls+urle,1,headers,post_type))#开启多线程
        t.start()
        t.join()
        for i in range(2,13):
            urr=urls+"start="+str((i-1)*90)+"&"+urle
            t = threading.Thread(target=climb,name='LoopThread'+str(i),args=(urr,i,headers,post_type))
            t.start()
            t.join()


if __name__=="__main__":
    main("Java开发","test.txt")
    print("123")