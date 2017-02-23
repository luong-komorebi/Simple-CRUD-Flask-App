class Config(object):
	"""
	Common Configuration
	"""

	# Put any configurations here that are common  accross all environments
	
class DevelopmentConfig(Config):
	"""
	Development configurations
	"""
	DEBUG = True
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
