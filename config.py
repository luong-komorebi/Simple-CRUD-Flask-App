class Config(object):
	"""
	Common Configuration
	"""

	# Put any configurations here that are common  accross all environments
	DEBUG = True
class DevelopmentConfig(Config):
	"""
	Development configurations
	"""
	
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	"""
	Production configuration
	"""

	DEBUG = False

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}

class TestingConfig(Config):
	"""
	Production configurations
	"""
	TESTING = True

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}