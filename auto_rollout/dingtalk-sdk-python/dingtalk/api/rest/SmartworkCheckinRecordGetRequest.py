'''
Created by auto_sdk on 2019.07.03
'''
from dingtalk.api.base import RestApi
class SmartworkCheckinRecordGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.cursor = None
		self.end_time = None
		self.size = None
		self.start_time = None
		self.userid_list = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.smartwork.checkin.record.get'
