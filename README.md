# aws-mlops-assignments

Create a folder inside the S3 location tiger-mle-pg/home/ with your name in the format
<first_name>.<last_name>
Create three folders inside the folder you created (A, B, C)
Put in files inside each of the folders.
Create a flask app that gets the folder name and lists the filename present in the corresponding
folder. (Use Boto3 for reading the contents of the folder) and test the code in local. 

Once local execution and testing are completed, deploy the same code in t3.micro EC2 instance(Use Free Tier).
Please make sure to create EC2 instances in the same region where the S3 bucket has been
created.
Configure the security group to allow incoming traffic only through 8085.
Access the EC2-deployed flask app via the EC2-public URL at port 8085.


