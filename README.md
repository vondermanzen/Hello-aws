© The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved.

A modified version of this workshop was offered in-person to a cohort of researchers by the Competency Centre in 2025. 

Everyone has moved on to other projects within the university and new courses and support are now offered by [OxRSE](https://train.rse.ox.ac.uk/material/HPCu/cloud_computing).

# Explore different providers

This course is available for multiple cloud providers. Choose your preferred platform:

- [Hello Google Cloud](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-gcloud)
- [Hello Microsoft Azure](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-mazure)
- [Hello Amazon Web Services](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws) (You are here) (⭐ Most popular)

# Instructions

<details>
<summary>Copy this repository (Optional: fork it)</summary>

![Step 2](README_images/download.png)

***
</details>
<details>
<summary>Go to the AWS Console and type "app runner" in the search bar</summary>

![Step 2](README_images/img1.png)

***
</details>
<details>
<summary>Create a new service</summary>

![Step 3](README_images/img2.png)

***
</details>
<details>
<summary>Select source code repository and link your repository</summary>

![Step 4](README_images/img3.png)

***
</details>
<details>
<summary>Set deployment to automatic</summary>

![Step 5](README_images/img4.png)

***
</details>
<details>
<summary>Select "Use a configuration file" (apprunner.yaml is already in the repository)</summary>

![Step 6](README_images/img5.png)

***
</details>

<details>
<summary>Choose a name for your service and deploy it. Default settings like 1 CPU and 2 GB RAM are enough.</summary>

![Step 7](README_images/img6.png)

***
</details>

Voilà! Access the URL.

![Voilà](README_images/img7.png)

***

# Going further

<details>
<summary><h2>Modifying the code</h2></summary>

You can commit some changes to your repository and watch how the service is updated automatically.

![Updating a service](README_images/update.png)

</details>

<details>
<summary><h2>Using a custom domain</h2></summary>

If you want to use a custom domain, just click "Link domain" in App Runner and follow the instructions. If you are not using Route 53, you will be asked to create the DNS records in your CloudFlare, Azure DNS or other account. 

![Linking the domain](README_images/link_domain.png)

![Voilà](README_images/domain.png)

</details>

<details>
<summary><h2>Cleaning up</h2></summary>

Don't forget to delete your service when you are no longer using it. You can always redeploy later.

![Deleting a service](README_images/delete.png)

</details>

<details>
<summary><h2>Adding an API endpoint</h2></summary>

Add the following code in app.py

```	
@app.route("/hello_api")
def hello_api():
    return {
		"name": "Wrinkle Five Star",
		"species": "Duck",
		"breed": "American Pekin",
		"hatching_date": "2020-09-09",
		"sex": "Male"
    }
```

Then test your endpoint

![API endpoint](README_images/hello_api.png)

</details>

<details>
<summary><h2>User interface</h2></summary>

In app.py, change the default route from "index.html" to "user_interface.html"

```	
@app.route("/")
def home():
    return render_template("user_interface.html")
```

Access the URL again and make sure the duck appears. 

![Duck](README_images/duck.png)

Below the duck, there are code snippets. Move on the "Storage bucket" chapter. 

</details>

<details>
<summary><h2>Storage bucket</h2></summary>

<details>
<summary>Use the code snippet to create a S3 bucket</summary>

If you have enabled the user interface, you should find consoles under the duck.
You have the choice between running a Python script or running a CLI command. 

![Create S3 bucket](README_images/create_s3_bucket.png)

</details>

<details>
<summary>Check the S3 bucket has been properly created</summary>

Since S3 buckets must be unique across all AWS users, only one of us could name the bucket "workshop-bucket". That's why the script adds your account ID in the name.  

![Created S3 bucket](README_images/created_s3_bucket.png)

</details>

<details>
<summary>Upload duck.glb to S3</summary>

![Upload S3 bucket](README_images/upload_s3_bucket.png)

</details>

<details>
<summary>Check the duck is in the S3 bucket</summary>

![Uploaded S3 bucket](README_images/uploaded_s3_bucket.png)

</details>

<details>
<summary>Download oxford.glb from the bucket</summary>

First, you need to modify the upload code to upload "oxford.glb" instead of "duck.glb", and run it again. 

![Upload S3 bucket](README_images/reupload_s3_bucket.png)

Then, you can use the third code snippet to download oxford.glb. 

![Download S3 bucket](README_images/download_s3_bucket.png)

</details>

<details>
<summary>Check that oxford.glb is downloaded</summary>

The 3D model should now be the door to St. Cross College. 

![Downloaded S3 bucket](README_images/downloaded_s3_bucket.png)

</details>

<details>
<summary>Cleaning up</summary>

Run the fourth snippet to delete the bucket. 

![Cleanup S3 bucket](README_images/cleanup_s3_bucket.png)

</details>

<details>
<summary>Check that the S3 bucket is deleted</summary>

![Cleaned S3 bucket](README_images/cleaned_s3_bucket.png)

</details>

<details>
<summary>TROUBLESHOOTING: Missing S3 permissions</summary>

Are you getting an error when you try to run the first code snippet? Most likely, this is because your AWS App Runner instance is not authorized to use S3. 

![Security error](README_images/security_error.png)

In App Runner, go to Configuration, then Security, and check that the instance is associated to a role. 

![Security configuration](README_images/configuration_security.png)

To this role, attach the S3 full access policy. 

![Attach policy](README_images/attach_policy.png)

</details>

</details>

<details>
<summary><h2>Local testing</h2></summary>

You need to test your changes before publishing them. 

<details>
<summary>Install Python</summary>

```	
https://www.python.org/downloads/
```

***
</details>
<details>
<summary>Install dependencies</summary>

```	
python -m pip install --break-system-packages -r requirements.txt
```

***
</details>
<details>
<summary>Run flask</summary>

```	
python -m flask run --port=80
```

Open localhost in your browser.   

***
</details>

<img width="280" height="126" alt="image" src="https://github.com/user-attachments/assets/60bc8002-f853-4879-b6d4-b95a35e709d9" />

</details>


