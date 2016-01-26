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
				},
				'status_node_started':{ #notification from the status node that it has started properly
					'id':'35',
					'data':'',
				},
				'power_distribution_node_started':{ #notification from the power dist node that it has started properly
					'id':'36',
					'data':'',
				},
				'control_node_started':{ #notification from the control node that it has started properly
					'id':'37',
					'data':'',
				},
				'is_brake_engaged':{ #is mech brake is engaged request
					'id':'38',
					'data':'',
				},
				'is_brake_engaged_rep':{ #reply to mech brake engaged request
					'id':'39',
					'data':'',
				},
				'get_brake_force':{ #mech brake force request
					'id':'40',
					'data':'',
				},
				'get_brake_force_rep':{ #reply to mech brake force request
					'id':'41',
					'data':'',
				},
				'set_brake_force':{ #request mech brake be set to 'data' force
					'id':'42',
					'data':'',
				},
				'get_eddy_brake_angle':{ #eddy brake angle request
					'id':'43',
					'data':'',
				},
				'get_eddy_brake_angle_rep':{ #reply to eddy brake angle request
					'id':'44',
					'data':'',
				},
				'get_eddy_brake_power':{ #eddy brake power request
					'id':'45',
					'data':'',
				},
				'get_eddy_brake_power_rep':{ #reply to eddy brake power request
					'id':'46',
					'data':'',
				},
				'get_eddy_brake_temp':{ #eddy brake temperature request
					'id':'47',
					'data':'',
				},
				'get_eddy_brake_temp_rep':{ #reply to eddy brake temperature request
					'id':'48',
					'data':'',
				},
				'set_eddy_brake_angle':{ #request eddy brake's angle be set to 'data' degrees
					'id':'49',
					'data':'',
				},
				'set_eddy_brake_power':{ #request eddy brake's power be set to 'data' percent
					'id':'50',
					'data':'',
				},
				'get_hover_eng_angle':{ #hover engine angle request
					'id':'51',
					'data':'',
				},
				'get_hover_eng_angle_rep':{ #reply to hover engine angle request
					'id':'52',
					'data':'',
				},
				'get_hover_eng_power':{ #hover engine power request
					'id':'53',
					'data':'',
				},
				'get_hover_eng_power_rep':{ #reply to hover engine power request
					'id':'54',
					'data':'',
				},
				'set_hover_eng_angle':{ #request hover engine's angle be set to 'data' degrees
					'id':'55',
					'data':'',
				},
				'set_hover_eng_power':{ #request hover engine's power be set to 'data' percent
					'id':'56',
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
				},
				'35':{ #notification from the status node that it has started properly
					'name':'status_node_started',
					'data':'',
				},
				'36':{ #notification from the power dist node that it has started properly
					'name':'power_distribution_node_started',
					'data':'',
				},
				'37':{ #notification from the control node that it has started properly
					'name':'control_node_started',
					'data':'',
				}
				'38':{ #is mech brake is engaged request
					'name':'is_brake_engaged',
					'data':'',
				},
				'39':{ #reply to mech brake engaged request
					'name':'is_brake_engaged_rep',
					'data':'',
				},
				'40':{ #mech brake force request
					'name':'get_brake_force',
					'data':'',
				},
				'41':{ #reply to mech brake force request
					'name':'get_brake_force_rep',
					'data':'',
				},
				'42':{ #request mech brake be set to 'data' force
					'name':'set_brake_force',
					'data':'',
					'input_data': True
				},
				'43':{ #eddy brake angle request
					'name':'get_eddy_brake_angle',
					'data':'',
				},
				'44':{ #reply to eddy brake angle request
					'name':'get_eddy_brake_angle_rep',
					'data':'',
				},
				'45':{ #eddy brake power request
					'name':'get_eddy_brake_power',
					'data':'',
				},
				'46':{ #reply to eddy brake power request
					'name':'get_eddy_brake_power_rep',
					'data':'',
				},
				'47':{ #eddy brake temperature request
					'name':'get_eddy_brake_temp',
					'data':'',
				},
				'48':{ #reply to eddy brake temperature request
					'name':'get_eddy_brake_temp_rep',
					'data':'',
				},
				'49':{ #request eddy brake's angle be set to 'data' degrees
					'name':'set_eddy_brake_angle',
					'data':'',
					'input_data': True
				},
				'50':{ #request eddy brake's power be set to 'data' percent
					'name':'set_eddy_brake_power',
					'data':'',
					'input_data': True
				},
				'51':{ #hover engine angle request
					'id':'get_hover_eng_angle',
					'data':'',
				},
				'52':{ #reply to hover engine angle request
					'id':'get_hover_eng_angle_rep',
					'data':'',
				},
				'53':{ #hover engine power request
					'id':'get_hover_eng_power',
					'data':'',
				},
				'54':{ #reply to hover engine power request
					'id':'get_hover_eng_power_rep',
					'data':'',
				},
				'55':{ #request hover engine's angle be set to 'data' degrees
					'id':'set_hover_eng_angle',
					'data':'',
					'input_data': True
				},
				'56':{ #request hover engine's power be set to 'data' percent
					'id':'set_hover_eng_power',
					'data':'',
					'input_data': True
				}
			}


