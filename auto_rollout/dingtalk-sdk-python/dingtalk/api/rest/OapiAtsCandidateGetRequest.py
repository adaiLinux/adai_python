'''
Created by auto_sdk on 2020.07.30
'''
from dingtalk.api.base import RestApi
class OapiAtsCandidateGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.biz_code = None
		self.candidate_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.ats.candidate.get'
