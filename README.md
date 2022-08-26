# aws-mlops-assignments

Create a folder inside the S3 location tiger-mle-pg/home/ with your name in the format
<first_name>.<last_name>
Create three folders inside the folder you created (A, B, C)
Put in files inside each of the folders.
Create a flask app that gets the folder name and lists the filename present in the corresponding
folder. (Use Boto3 for reading the contents of the folder) and test the code in local. 
![ip2](https://user-images.githubusercontent.com/100826424/183100640-3fbf3ee8-261e-4112-96b8-de09355fb4bb.JPG)

Once local execution and testing are completed, deploy the same code in t3.micro EC2 instance(Use Free Tier).
Please make sure to create EC2 instances in the same region where the S3 bucket has been
created.
Configure the security group to allow incoming traffic only through 8085.
Access the EC2-deployed flask app via the EC2-public URL at port 8085.

![ip](https://user-images.githubusercontent.com/100826424/183100753-f61ebd72-7dd0-4569-ac84-cad66d924db7.JPG)

# Assignment2:

![public ip](https://user-images.githubusercontent.com/100826424/186869278-78d78ac3-ff90-4435-b56c-01198bb2048d.JPG)

load balancer
![loadbalancer](https://user-images.githubusercontent.com/100826424/186869322-3815498f-caa6-4ad5-828b-929e5c6120ee.JPG)

targets
![targets](https://user-images.githubusercontent.com/100826424/186869357-681e69ee-a808-412f-8233-9a6d9f4c1674.JPG)

stopping lambda function
![stopping](https://user-images.githubusercontent.com/100826424/186869400-6f60008b-8f36-4743-a75d-8e74088e2b23.JPG)
