 
userschema= {
	'firstname': {
                'type': 'string',
		'minlength': 1,
		'maxlength': 100,
		'required': True
	},
       'lastname': {
                'type': 'string',
		'minlength': 1,
		'maxlength': 100,
		'required': True,
        },
       'username': {
                'type': 'string',
		'minlength': 1,
		'maxlength': 100,
		'unique': True
        },
       'password': {
                'type': 'string'
        },
       'phone': {
                'type': 'string',
		'minlength': 11,
		'maxlength': 12,
		'required': True,
		'unique': True
        },
	'coinId': {
                'type': 'string',
				'minlength': 99,
				'maxlength': 101,
				'unique': True
        },
	'location': {
		'type': 'dict',
		'schema': {
			'address': {'type': 'string'},
			'city': {'type': 'string'}
		},
	},
	'role': {
		'type': 'list',
		'allowed': ["cardHolder", "merchant", "admin"],
	},
        'creatDate': {
                'type': 'datetime'
        }			
}

coinInfoschema = {
            'currentBalance': {
                'type': 'string'
            },
            'lastBalance': {
                'type': 'string'
            },
            'phone': {
                'type': 'string',
				'minlength': 11,
				'maxlength': 12,
				'required': True,
				'unique': True
            },
			'coinId': {
                'type': 'string',
				'minlength': 99,
				'maxlength': 101,
				'unique': True,
				'required': True,
            },
            'creatDate': {
                'type': 'datetime'
				
            }			
        }


transactionsschema = {
            'srcPhone': {
                'type': 'string',
				'minlength': 11,
				'maxlength': 12,
				'required': True,
				'unique': True
            },
            'desPhone': {
                'type': 'string',
				'minlength': 11,
				'maxlength': 12,
				'required': True,
				'unique': True
            },
            'srcCoin': {
                'type': 'string',
				'minlength': 99,
				'maxlength': 101,
				'unique': True
            },
			'desCoin': {
                'type': 'string',
				'minlength': 99,
				'maxlength': 101,
				'unique': True
            },
            'amount': {
                'type': 'string'
				
            },
            'merchantId': {
                'type': 'string',
				'minlength': 8,
				'maxlength': 10,
				'unique': True
            },

            'creatDate': {
                'type': 'datetime'
				
            }			
    }

merchantschema = {
		    'merchantId': {
                'type': 'string',
				'minlength': 8,
				'maxlength': 10,
				'unique': True
            },
            'merchantBussines': {
                'type': 'dict',
				'schema': {
						'cat1': {'type': 'string'},
						'cat2': {'type': 'string'}
				},
            },
            'merchantFirstname': {
                'type': 'string'
            },
            'merchantLastname': {
                'type': 'string'
            },
            'merchantUsername': {
                'type': 'string',
                 'unique': True
            },
            'merchantPassword': {
                'type': 'string'
            },
            'merchantPhone': {
                'type': 'string',
				'unique': True
            },
			'merchantCoinId': {
                'type': 'string',
				'unique': True
            },
            'merchantCreatDate': {
                'type': 'datetime'
	    }			
}
 

userend = {
    'item_title': 'user',
    'allow_unknown': True,
    'RESOURCE_METHODS' : ['GET', 'POST', 'DELETE'],
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'schema': userschema,
    }
coinInfoend = {
    'item_title': 'coinInfo',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': coinInfoschema,
     }
transactionsend = {
    'item_title': 'transactions',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': transactionsschema,
     }
merchantend = {
    'item_title': 'merchant',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': merchantschema,
     }
 

DOMAIN = {
    'user': userend,
    'coinInfo': coinInfoend,
    'transactions': transactionsend ,
    'merchant': merchantend,
}

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
