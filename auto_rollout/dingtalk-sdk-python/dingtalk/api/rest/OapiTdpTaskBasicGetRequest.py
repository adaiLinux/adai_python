'''
Created by auto_sdk on 2020.03.31
'''
from dingtalk.api.base import RestApi
class OapiTdpTaskBasicGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.microapp_agent_id = None
		self.task_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.tdp.task.basic.get'
