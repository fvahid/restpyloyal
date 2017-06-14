DOMAIN = {
    'user': {
        'schema': {
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
                'type': 'datetime',
				'required': True
				
            }			
        }
    },
	'coinInfo': {
        'schema': {
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
				'required': True,
                'type': 'datetime'
				
            }			
        }
    },
    'transactions': {
        'schema': {
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
				'required': True,
                'type': 'datetime'
				
            }			
        }
    },	
	'merchant': {
        'schema': {
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
				'required': True,
                'type': 'datetime'
				
            }			
        }
    },	
	
}



