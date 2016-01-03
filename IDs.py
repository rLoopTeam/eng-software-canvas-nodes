class MessageList():
	messages = 	{
				'stop':{ #stop
					'id':'1',
					'data':''
				},
				'get_engine_status':{ #get engine status
					'id':'2',
					'data':''
				},
				'move':{ #move pod at given speed
					'id':'4',
					'data':'',
					'input_data': True
				},
				'get_engine_status_l':{ #get status of all engines
					'id':'5',
					'data':''
				},
				'engine_status_l':{ #engine L status
					'id':'6',
					'data':''
				},
				'engine_status_r':{ #engine R status
					'id':'7',
					'data':''
				},
				'tilt_l':{ #tilt engine L
					'id':'8',
					'data':'',
					'input_data': True
				},
				'tilt_r':{ #tilt engine R
					'id':'9',
					'data':'',
					'input_data': True
				},
				'start_l':{ #start engine L
					'id':'10',
					'data':'',
				},
				'start_r':{ #start engine R
					'id':'11',
					'data':'',
				},
				'stop_l':{ #stop engine L
					'id':'12',
					'data':'',
				},
				'stop_r':{ #stop engine R
					'id':'13',
					'data':'',
				},
				'start':{ #startup sequnce of pod
					'id':'14',
					'data':'',
				},
				'uc_temp_req':{ #umbillical connector temp request message
					'id':'15',
					'data':'',
				},
				'uc_temp_data':{ #umbillical connector temp data response
					'id':'16',
					'data':'',
				},
				'batt_temp_req':{ #battery temp request
					'id':'17',
					'data':'',
				},
				'batt_temp_data':{ #battery temp data response
					'id':'18',
					'data':'',
				},
				'batt_power_req':{ #battery power level request
					'id':'19',
					'data':'',
				},
				'batt_power_data':{ #battery power data level response
					'id':'20',
					'data':'',
				},
				'so_temp_req':{ #standard outlet temperature request
					'id':'21',
					'data':'',
				},
				'so_temp_data':{ #standard outlet temperature data response
					'id':'22',
					'data':'',
				},
				'hover_height_req':{ #hover height request message
					'id':'23',
					'data':'',
				},
				'hover_height_data':{ #hover height data response
					'id':'24',
					'data':'',
				},
				'get_hover_height':{ #hover height request from ground station
					'id':'25',
					'data':'',
				},
				'pod_temp_req':{ #pod cabin internal temperature request
					'id':'26',
					'data':'',
				},
				'pod_temp_data':{ #pod cabin internal temperature data
					'id':'27',
					'data':'',
				},
				'pod_attitude_req':{ #pod attitude request
					'id':'28',
					'data':'',
				},
				'pod_attitude_data':{ #pod attitude data
					'id':'29',
					'data':'',
				},
				'pod_pressure_req':{ #pod cabin internal pressure req
					'id':'30',
					'data':'',
				},
				'pod_pressure_data':{ #pod cabin internal pressure data
					'id':'31',
					'data':'',
				},
				'pod_position_req':{ #pod position request
					'id':'32',
					'data':'',
				},
				'pod_position_data':{ #pod positon data
					'id':'33',
					'data':'',
				},
				'get_pod_status':{ #pod positon data
					'id':'34',
					'data':'',
				}
			}

	ids = 	{
				'1':{ #stop
					'name':'stop',
					'data':''
				},
				'2':{ #get engine status
					'name':'get_engine_status',
					'data':''
				},
				'4':{ #move pod at given speed
					'name':'move',
					'data':'',
					'input_data': True
				},
				'5':{ #get status of all engines
					'name':'get_engine_status_l',
					'data':''
				},
				'6':{ #engine L status
					'name':'engine_status_l',
					'data':''
				},
				'7':{ #engine R status
					'name':'engine_status_r',
					'data':''
				},
				'8':{ #tilt engine L
					'name':'tilt_l',
					'data':'',
					'input_data': True
				},
				'9':{ #tilt engine R
					'name':'tilt_r',
					'data':'',
					'input_data': True
				},
				'10':{ #start engine L
					'name':'start_l',
					'data':'',
				},
				'11':{ #start engine R
					'name':'start_r',
					'data':'',
				},
				'12':{ #stop engine L
					'name':'stop_l',
					'data':'',
				},
				'13':{ #stop engine R
					'name':'stop_r',
					'data':'',
				},
				'14':{ #startup sequnce of pod
					'name':'start',
					'data':'',
				},
				'15':{ #umbillical connector temp request message
					'name':'uc_temp_req',
					'data':'',
				},
				'16':{ #umbillical connector temp data response
					'name':'uc_temp_data',
					'data':'',
				},
				'17':{ #battery temp request
					'name':'batt_temp_req',
					'data':'',
				},
				'18':{ #battery temp data response
					'name':'batt_temp_data',
					'data':'',
				},
				'19':{ #battery power level request
					'name':'batt_power_req',
					'data':'',
				},
				'20':{ #battery power data level response
					'name':'batt_power_data',
					'data':'',
				},
				'21':{ #standard outlet temperature request
					'name':'so_temp_req',
					'data':'',
				},
				'22':{ #standard outlet temperature data response
					'name':'so_temp_data',
					'data':'',
				},
				'23':{ #hover height request message
					'name':'hover_height_req',
					'data':'',
				},
				'24':{ #hover height data response
					'name':'hover_height_data',
					'data':'',
				},
				'25':{ #hover height request from ground station
					'name':'get_hover_height',
					'data':'',
				},
				'26':{ #pod cabin internal temperature request
					'name':'pod_temp_req',
					'data':'',
				},
				'27':{ #pod cabin internal temperature data
					'name':'pod_temp_data',
					'data':'',
				},
				'28':{ #pod attitude request
					'name':'pod_attitude_req',
					'data':'',
				},
				'29':{ #pod attitude data
					'name':'pod_attitude_data',
					'data':'',
				},
				'30':{ #pod cabin internal pressure req
					'name':'pod_pressure_req',
					'data':'',
				},
				'31':{ #pod cabin internal pressure data
					'name':'pod_pressure_data',
					'data':'',
				},
				'32':{ #pod position request
					'name':'pod_position_req',
					'data':'',
				},
				'33':{ #pod positon data
					'name':'pod_position_data',
					'data':'',
				},
				'34':{ #pod positon data
					'name':'get_pod_status',
					'data':'',
				}
			}


