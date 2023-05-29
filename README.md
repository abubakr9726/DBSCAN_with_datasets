# DBSCAN_with_datasets
DBSCAN_with_datasets

==> Data_annotation.ipynb		---->		for data annotation for raw data

==> DBSCAN_algo.ipynb			---->		for filtering and clustering of data



==> 1,2,3,5,6,8,9,10,11,12		---->		x
	
	--> each folder is a dataset and has 4 subfolder
	
		--> map:		contains map file with player trajectory in .csv format				(1_TRAJECTORY.csv)
		
		--> ROAD_POINTS: 	contains road points
		
		--> SIDEWALK_POINTS:	contains sidewalk points
		
		--> CAR_PONTS:		contains car points
			--> each CAR_POINT folder has 3 folders
				--> RAW_CAR_POINTS:		contains 
								1) raw car points in .csv format				(car_points.csv)
								2) picture of points in .png format				(x.png)
								3) bounding boxes for ground truth for whole dataset 	(x_real_bb)
				
				--> LEFT_SIDE_CAR_POINTS: 	contains
								1) LEFT_POINTS folder having left side car points (x_neg.csv) with pictures of points in .png format 	(x_neg.png)
								2) RAW_BOUNDING_BOXES folder have raw bounding boxes for ground truth for left side car points 		(raw_x_neg)
								3) REAL_BOUNDING_BOXES folder have real bounding boxes for ground truth for left side car points 		(real_x_neg)
				
				--> RIGHT_SIDE_CAR_POINTS: 	contains
								1) RIGHT_POINTS folder have right side car points (x_pos.csv) with pictures of points in .png format 	(x_pos.png)
								2) RAW_BOUNDING_BOXES folder have raw bounding boxes for ground truth for right side car points 		(raw_x_pos)
								3) REAL_BOUNDING_BOXES folder have real bounding boxes for ground truth for right side car points 		(real_x_pos)
		
		--> DATASETx_readme:	contains actual number of left and right cars present in the scene						
								
								
---------------------------------------------------------------------------------NOTE---------------------------------------------------------------------------------
-->	for testing of clustering use car_points.csv file in RAW_CAR_POINTS folder and for bounding boxes data (for ground truth) use x_real_bb.txt file in same folder	
-->	for DBSCAN clustering, for all datasets:	ep = 1,	min_samples = 10	   						
-------------------------------------------------------------------------------END NOTE-------------------------------------------------------------------------------
