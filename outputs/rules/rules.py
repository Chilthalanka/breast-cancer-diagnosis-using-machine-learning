def findDecision(obj): #obj[0]: clump_thickness, obj[1]: size_uniformity, obj[2]: shape_uniformity, obj[3]: marginal_adhesion, obj[4]: epithelial_size, obj[5]: bare_nucleoli, obj[6]: bland_chromatin, obj[7]: normal_nucleoli, obj[8]: mitoses
	# {"feature": "size_uniformity", "instances": 455, "metric_value": 0.9275, "depth": 1}
	if obj[1]<=2:
		# {"feature": "clump_thickness", "instances": 285, "metric_value": 0.2022, "depth": 2}
		if obj[0]<=7:
			# {"feature": "epithelial_size", "instances": 280, "metric_value": 0.108, "depth": 3}
			if obj[4]<=5:
				# {"feature": "bare_nucleoli", "instances": 277, "metric_value": 0.0617, "depth": 4}
				if obj[5]<=3:
					return '0'
				elif obj[5]>3:
					# {"feature": "shape_uniformity", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=2:
						# {"feature": "marginal_adhesion", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[3]<=2:
							return '0'
						elif obj[3]>2:
							# {"feature": "bland_chromatin", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>1:
								# {"feature": "normal_nucleoli", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									# {"feature": "mitoses", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return '0'
									else: return '0'
								else: return '0'
							elif obj[6]<=1:
								return '0'
							else: return '0'
						else: return '0'
					elif obj[2]>2:
						return '1'
					else: return '1'
				else: return '0'
			elif obj[4]>5:
				# {"feature": "shape_uniformity", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>1:
					return '1'
				elif obj[2]<=1:
					return '0'
				else: return '0'
			else: return '1'
		elif obj[0]>7:
			return '1'
		else: return '1'
	elif obj[1]>2:
		# {"feature": "shape_uniformity", "instances": 170, "metric_value": 0.5718, "depth": 2}
		if obj[2]>1:
			# {"feature": "bland_chromatin", "instances": 166, "metric_value": 0.5132, "depth": 3}
			if obj[6]>1:
				# {"feature": "bare_nucleoli", "instances": 165, "metric_value": 0.4972, "depth": 4}
				if obj[5]>1:
					# {"feature": "epithelial_size", "instances": 149, "metric_value": 0.38, "depth": 5}
					if obj[4]>2:
						# {"feature": "marginal_adhesion", "instances": 132, "metric_value": 0.2668, "depth": 6}
						if obj[3]<=5:
							# {"feature": "clump_thickness", "instances": 68, "metric_value": 0.4306, "depth": 7}
							if obj[0]>6:
								# {"feature": "normal_nucleoli", "instances": 43, "metric_value": 0.1594, "depth": 8}
								if obj[7]<=7:
									return '1'
								elif obj[7]>7:
									# {"feature": "mitoses", "instances": 18, "metric_value": 0.3095, "depth": 9}
									if obj[8]<=2:
										return '1'
									elif obj[8]>2:
										return '1'
									else: return '1'
								else: return '1'
							elif obj[0]<=6:
								# {"feature": "normal_nucleoli", "instances": 25, "metric_value": 0.7219, "depth": 8}
								if obj[7]<=6:
									# {"feature": "mitoses", "instances": 18, "metric_value": 0.8524, "depth": 9}
									if obj[8]<=1:
										return '1'
									else: return '1'
								elif obj[7]>6:
									return '1'
								else: return '1'
							else: return '1'
						elif obj[3]>5:
							return '1'
						else: return '1'
					elif obj[4]<=2:
						# {"feature": "marginal_adhesion", "instances": 17, "metric_value": 0.874, "depth": 6}
						if obj[3]>2:
							return '1'
						elif obj[3]<=2:
							# {"feature": "clump_thickness", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[0]<=8:
								return '0'
							elif obj[0]>8:
								return '1'
							else: return '1'
						else: return '0'
					else: return '1'
				elif obj[5]<=1:
					# {"feature": "epithelial_size", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[4]>3:
						# {"feature": "clump_thickness", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[0]<=6:
							# {"feature": "marginal_adhesion", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=8:
								# {"feature": "normal_nucleoli", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[7]>1:
									return '1'
								elif obj[7]<=1:
									# {"feature": "mitoses", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return '0'
									else: return '0'
								else: return '0'
							elif obj[3]>8:
								return '0'
							else: return '0'
						elif obj[0]>6:
							return '1'
						else: return '1'
					elif obj[4]<=3:
						return '0'
					else: return '0'
				else: return '1'
			elif obj[6]<=1:
				return '0'
			else: return '0'
		elif obj[2]<=1:
			return '0'
		else: return '0'
	else: return '1'
