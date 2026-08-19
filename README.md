© The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved.

A modified version of this workshop was offered in-person to a cohort of researchers by the Competency Centre in 2025. 

Everyone has moved on to other projects within the university and new courses and support are now offered by [OxRSE](https://train.rse.ox.ac.uk/material/HPCu/cloud_computing).

# Explore different providers

This course is available for multiple cloud providers. Choose your preferred platform:

- [Hello Google Cloud](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-gcloud)
- [Hello Microsoft Azure](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-azure)
- [Hello Amazon Web Services](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws) (You are here) (⭐ Most popular)

# Instructions

<details>
<summary>Copy this repository (Optional: fork it)</summary>

![Image](README_images/download.png)

***
</details>
<details>
<summary>Go to the AWS Console and type "app runner" in the search bar</summary>

![Image](README_images/img1.png)

***
</details>
<details>
<summary>Create a new service</summary>

![Image](README_images/img2.png)

***
</details>
<details>
<summary>Select source code repository and link your repository</summary>

![Image](README_images/img3.png)

***
</details>
<details>
<summary>Set deployment to automatic</summary>

![Step 5](README_images/img4.png)

***
</details>
<details>
<summary>Select "Use a configuration file" (apprunner.yaml is already in the repository)</summary>

![Image](README_images/img5.png)

***
</details>

<details>
<summary>Choose a name for your service and deploy it. Default settings like 1 CPU and 2 GB RAM are enough.</summary>

![Image](README_images/img6.png)

***
</details>

The app should now be publicly accessible.

![Image](README_images/img7.png)

***

# Going further

<details>
<summary><h2>Modifying the code</h2></summary>

You can commit some changes to your repository and watch how the service is updated automatically.

![Image](README_images/update.png)

</details>

<details>
<summary><h2>Using a custom domain</h2></summary>

If you want to use a custom domain, just click "Link domain" in App Runner and follow the instructions. If you are not using Route 53, you will be asked to create the DNS records in your external account (CloudFlare, Azure DNS, etc.)

![Image](README_images/link_domain.png)

![Image](README_images/domain.png)

</details>

<details>
<summary><h2>Cleaning up</h2></summary>

Don't forget to delete your service when you are no longer using it. You can always redeploy later.

![Image](README_images/delete.png)

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
<summary><h2>Local testing</h2></summary>

You need to test your changes before publishing them. 

<details>
<summary>Clone the repository (if you haven't already)</summary>

```bash
git clone https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws.git
```
***
</details>

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

</details>

# Exercise: Ducks and AWS CLI

<details>
<summary>Clone the repository (if you haven't already)</summary>

```bash
git clone https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws.git
```
***
</details>

<details>
<summary>Make the duck appear</summary>

Replace index.html with this code to render duck.glb

<details>
<summary><strong>View source code</strong></summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duck Viewer</title>

    <style>
        html, body {
            margin: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background: white;
        }

        #viewer-container {
            width: 100vw;
            height: 100vh;
        }

        canvas {
            display: block;
            width: 100%;
            height: 100%;
        }
    </style>
</head>

<body>

    <div id="viewer-container"></div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/loaders/GLTFLoader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>

    <script>
        const container = document.getElementById('viewer-container');

        // Scene
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0xffffff);

        // Camera
        const camera = new THREE.PerspectiveCamera(
            45,
            container.clientWidth / container.clientHeight,
            0.1,
            1000
        );

        camera.position.set(0, 0.5, 3);

        // Renderer
        const renderer = new THREE.WebGLRenderer({
            antialias: true
        });

        renderer.setSize(
            container.clientWidth,
            container.clientHeight
        );

        renderer.setPixelRatio(window.devicePixelRatio);
        container.appendChild(renderer.domElement);

        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 1.5);
        scene.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xffffff, 2);
        directionalLight.position.set(2, 3, 4);
        scene.add(directionalLight);

        const directionalLight2 = new THREE.DirectionalLight(0xffffff, 1);
        directionalLight2.position.set(-2, 1, -2);
        scene.add(directionalLight2);

	const gridHelper = new THREE.GridHelper(2, 10);
        scene.add(gridHelper);
        
        // Orbit controls
        const controls = new THREE.OrbitControls(
            camera,
            renderer.domElement
        );

        controls.enableDamping = true;
        controls.dampingFactor = 0.05;

        controls.minDistance = 1;
        controls.maxDistance = 10;

        // Load duck
        const loader = new THREE.GLTFLoader();

        loader.load(
            '/duck.glb',

            function (gltf) {
                const model = gltf.scene;

                // Scale duck
                model.scale.set(10, 10, 10);

                // Add duck to scene
                scene.add(model);

                // Center duck
                const box = new THREE.Box3().setFromObject(model);
                const center = box.getCenter(new THREE.Vector3());

                model.position.sub(center);

                // Put duck on the ground
                const newBox = new THREE.Box3().setFromObject(model);
                model.position.y -= newBox.min.y;
            },

            function (xhr) {
                console.log(
                    (xhr.loaded / xhr.total * 100) + '% loaded'
                );
            },

            function (error) {
                console.error(
                    'Error loading duck.glb:',
                    error
                );
            }
        );

        // Animation loop
        function animate() {
            requestAnimationFrame(animate);

            controls.update();

            renderer.render(scene, camera);
        }

        animate();

        // Handle window resizing
        window.addEventListener('resize', function () {
            const width = container.clientWidth;
            const height = container.clientHeight;

            camera.aspect = width / height;
            camera.updateProjectionMatrix();

            renderer.setSize(width, height);
        });
    </script>

</body>
</html>
```

</details>

![Image](README_images/duck.png)

***
</details>

<details>
<summary>Install the AWS CLI</summary>

[Download and install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

***
</details>

<details>
<summary>Create a S3 bucket</summary>

```bash
aws s3api create-bucket --bucket hello-bucket --create-bucket-configuration LocationConstraint=eu-west-2
```

***
</details>

<details>
<summary>Check the S3 bucket has been properly created</summary>

![Created S3 bucket](README_images/created_s3_bucket.png)

***
</details>

<details>
<summary>Upload duck.glb to S3</summary>

```bash
aws s3 cp duck.glb s3://hello-bucket/duck.glb --content-type "model/gltf-binary"
```

***
</details>

<details>
<summary>Check the duck is in the S3 bucket</summary>

![Uploaded S3 bucket](README_images/uploaded_s3_bucket.png)

***
</details>

<details>
<summary>Download the duck from the bucket</summary>

```bash
aws s3 cp s3://hello-bucket/oxford.glb downloaded.glb
```
***
</details>

<details>
<summary>Cleaning up</summary>

```bash
aws s3 rm s3://hello-bucket --recursive
```

```bash
aws s3api delete-bucket --bucket hello-bucket
```

***
</details>

<details>
<summary>Check that the S3 bucket is deleted</summary>

![Cleaned S3 bucket](README_images/cleaned_s3_bucket.png)

***
</details>

<details>
<summary>Creating a service role</summary>

Your web app in AWS App Runner can perform the same action, but it needs to be authorized to use S3. 

![Security error](README_images/security_error.png)

In App Runner, go to Configuration, then Security, and associate the instance to a role. 

![Security configuration](README_images/configuration_security.png)

To this role, attach the S3 full access policy. 

![Attach policy](README_images/attach_policy.png)

Once this is done, it can use AWS CLI or, since this a Python app, the Boto 3 library in app.py. 

</details>

</details>


