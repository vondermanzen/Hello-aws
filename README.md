© The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved.

# Explore different providers

This course is available for multiple cloud providers. Choose your preferred platform:

- [Hello Google Cloud](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-gcloud)
- [Hello Microsoft Azure](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-azure)
- [Hello Amazon Web Services](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws) (You are here) (⭐ Most popular)

# University workshop

A modified version of this course was offered as an in-person workshop to a cohort of researchers by the Competency Centre in 2025. 

Everyone has moved on to other projects within the university and new courses and support are now offered by [OxRSE](https://train.rse.ox.ac.uk/material/HPCu/cloud_computing).

# Disclaimer

App Runner [no longers exists](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html). This course must be rewritten for ECS Express. 

# Instructions

<details>
<summary>Copy this repository (Optional: fork it)</summary>

<img width="447" height="368" alt="image" src="https://github.com/user-attachments/assets/01310092-b483-4b5a-adff-3b2640fc2917" />

***
</details>
<details>
<summary>Go to the AWS Console and type "app runner" in the search bar</summary>

<img width="1129" height="219" alt="img1" src="https://github.com/user-attachments/assets/250e6f9f-57a3-4f5b-bb63-86cb9a3ec17c" />

***
</details>
<details>
<summary>Create a new service</summary>

<img width="493" height="203" alt="img2" src="https://github.com/user-attachments/assets/65130195-f121-4c29-846e-92bc30e09574" />

***
</details>
<details>
<summary>Select source code repository and link your repository</summary>

<img width="1516" height="762" alt="img3" src="https://github.com/user-attachments/assets/7a62e400-1bdc-4e0c-8a8b-f8b5737df7ea" />

***
</details>
<details>
<summary>Set deployment to automatic</summary>

<img width="1507" height="242" alt="img4" src="https://github.com/user-attachments/assets/fd589f22-fffc-45c0-8391-c4849f73cd33" />

***
</details>
<details>
<summary>Select "Use a configuration file" (apprunner.yaml is already in the repository)</summary>

<img width="1525" height="273" alt="img5" src="https://github.com/user-attachments/assets/a561dd54-cc4f-4ff0-8fee-ed1bc1762731" />

***
</details>

<details>
<summary>Choose a name for your service and deploy it. Default settings like 1 CPU and 2 GB RAM are enough.</summary>

<img width="1525" height="284" alt="img6" src="https://github.com/user-attachments/assets/f75d5fb5-bb59-437b-bb8a-eb732502bd25" />

***
</details>

The app should now be publicly accessible.

<img width="551" height="103" alt="img7" src="https://github.com/user-attachments/assets/08fbbdc2-2707-4491-b4c2-ebe7d7f1ff4b" />

***

# Going further

<details>
<summary><h2>Modifying the code</h2></summary>

You can commit some changes to your repository and watch how the service is updated automatically.

<img width="674" height="326" alt="update" src="https://github.com/user-attachments/assets/c2c425e1-0579-4cec-8a61-d68d1ed58687" />

</details>

<details>
<summary><h2>Using a custom domain</h2></summary>

If you want to use a custom domain, just click "Link domain" in App Runner and follow the instructions. If you are not using Route 53, you will be asked to create the DNS records in your external account (CloudFlare, Azure DNS, etc.)

<img width="1891" height="568" alt="link_domain" src="https://github.com/user-attachments/assets/1d152ae9-706c-4825-be6a-0a5fbcffb38f" />

<img width="496" height="100" alt="domain" src="https://github.com/user-attachments/assets/d4164e21-cbc3-4de8-a181-592e7b4ee1e8" />


</details>

<details>
<summary><h2>Cleaning up</h2></summary>

Don't forget to delete your service when you are no longer using it. It should be quite easy to redeploy it later with same URL.

<img width="361" height="192" alt="delete" src="https://github.com/user-attachments/assets/6f3d35bf-6616-45a5-a950-9d20dbf0837a" />

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

<img width="491" height="200" alt="hello_api" src="https://github.com/user-attachments/assets/2731d1be-2222-4199-af89-af6a8f8866aa" />

</details>

<details>
<summary><h2>Local testing</h2></summary>

You need to test your changes before publishing them. 

<details>
<summary>Clone the repository (if you haven't already)</summary>

```bash
git clone https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws.git
```

<img width="447" height="368" alt="image" src="https://github.com/user-attachments/assets/2bd75475-4696-42a6-892e-659a7a026c64" />

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

<img width="290" height="110" alt="image" src="https://github.com/user-attachments/assets/371d43c0-8c12-4faa-9f6b-6a8295a7e8d4" />

***
</details>

</details>

***

# Exercise: Ducks and AWS CLI

<details>
<summary>Clone the repository (if you haven't already)</summary>

```bash
git clone https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws.git
```

<img width="447" height="368" alt="image" src="https://github.com/user-attachments/assets/b4669cc5-7e00-4602-be4d-53c1204178f9" />

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

<img width="1852" height="1005" alt="image" src="https://github.com/user-attachments/assets/153165d1-cbd6-41be-a8e1-6d2790d525b8" />

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

<img width="1044" height="500" alt="created_s3_bucket" src="https://github.com/user-attachments/assets/df310f98-eb83-4a02-8b64-c0631eafb40b" />

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

<img width="869" height="421" alt="uploaded_s3_bucket" src="https://github.com/user-attachments/assets/eb352d29-6943-4942-b6d2-6653506fb7c2" />

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

<img width="910" height="247" alt="cleaned_s3_bucket" src="https://github.com/user-attachments/assets/8008a4cc-19a4-459b-800f-d2af1dca5063" />

***
</details>

<details>
<summary>Creating a service role</summary>

Your web app in AWS App Runner can perform the same action, but it needs to be authorized to use S3. 

<img width="420" height="249" alt="security_error" src="https://github.com/user-attachments/assets/2c384b3f-eda3-4f3f-9d22-2b4522b98819" />

In App Runner, go to Configuration, then Security, and associate the instance to a role. 

<img width="920" height="570" alt="configuration_security" src="https://github.com/user-attachments/assets/c66ed83a-0e07-4d95-bb13-bc59f82909d6" />

To this role, attach the S3 full access policy. 

<img width="681" height="447" alt="attach_policy" src="https://github.com/user-attachments/assets/0cd842d1-da45-4f37-9138-a4110f79a0bd" />

Once this is done, it can use AWS CLI or, since this a Python app, the Boto 3 library in app.py. 

</details>

</details>


