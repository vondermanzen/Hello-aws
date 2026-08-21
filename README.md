© The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved.

# Explore different providers

This course is available for multiple cloud providers. Choose your preferred platform:

- [Hello Google Cloud](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-gcloud)
- [Hello Microsoft Azure](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-azure)
- [Hello Amazon Web Services](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws) (You are here) (⭐ Most popular)

# University workshop

A modified version of this course was offered as an in-person workshop for researchers and students by the Competency Centre in 2025. 

Everyone has moved on to other projects in the university and new courses and support are now offered by [OxRSE](https://train.rse.ox.ac.uk/material/HPCu/cloud_computing).

# Instructions

<details>
<summary>Go to Amazon ECR / Private registry / Repositories and create a new repository called hello-aws</summary>

<img width="646" height="275" alt="image" src="https://github.com/user-attachments/assets/9cf071ab-8ca3-4dd4-b215-dccb0c9d7c41" />

***
</details>
<details>
<summary>Go to Code Build / Build Project and create a new build project called hello-aws</summary>

<img width="940" height="247" alt="image" src="https://github.com/user-attachments/assets/68927bff-0a11-43d6-a6a7-57d05ab30f4a" />

***
</details>
<details>
<summary>Select GitHub/Public repository as the source, name the service role for example hello-aws-codebuild-role and tick "Use a buildspec file"</summary>

<img width="922" height="400" alt="image" src="https://github.com/user-attachments/assets/72bbf2f3-eb0c-4ef8-bdae-fc71fb12e607" />

<img width="670" height="188" alt="image" src="https://github.com/user-attachments/assets/90929c30-683a-4bc8-a5b0-843a67808e18" />

<img width="1368" height="252" alt="image" src="https://github.com/user-attachments/assets/1442968e-6e29-4db3-954c-4a2d4f75e461" />

***
</details>
<details>
<summary>Click on the build project's service role / Add permissions / Attach policies and attach AmazonEC2ContainerRegistryPowerUser</summary>
	
<img width="1464" height="258" alt="image" src="https://github.com/user-attachments/assets/d295d6f6-2213-454d-b032-f575fe8e4e19" />

***
</details>
<details>
<summary>Press Start build</summary>

<img width="1119" height="217" alt="image" src="https://github.com/user-attachments/assets/be66b6e8-0409-43c0-a8f1-2ed5c45c4105" />

***
</details>
<details>
<summary>Go to Amazon Elastic Container Service / Express Mode. Select the built image and set image selection to tag "latest"</summary>

<img width="832" height="578" alt="image" src="https://github.com/user-attachments/assets/b807fbbc-4486-454c-ad2f-1e9e6ea42158" />

***
</details>

The app should now be publicly accessible.

<img width="579" height="149" alt="image" src="https://github.com/user-attachments/assets/553e3736-6cbd-4f74-8282-2cff94420fef" />

***

# Going further

<details>
<summary><h2>Modifying the code</h2></summary>

If you select your private repository as the source of the build project, then every commit will create a new image automatically. After that, you need to press "Update service" in ECS. 

</details>

<details>
<summary><h2>Cleaning up</h2></summary>

To clean up fully, you should delete the service, but also the build project, the built image, and the image repository.

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

<img width="647" height="299" alt="image" src="https://github.com/user-attachments/assets/64242c0f-9566-48ce-a15e-9c3277954dbd" />

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

# Exercise: Ducks and buckets

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
<summary>Try to make the duck downloadable</summary>

Hint: if you choose to read it from the bucket, your instance needs a service role 

```bash
@app.route("/download/duck")
def download_duck():
    # something
```

</details>

<details>
<summary><h1>Using AI</h1></summary>

I originally suggested to prompt for a duck army... 

<img width="928" height="701" alt="image" src="https://github.com/user-attachments/assets/9eb25a5f-660c-4917-9399-ccc897b632ec" />

...however one of the researchers decided to create a Ducknado and I reckon that is a worthwhile idea.  

<img width="800" height="416" alt="ducknado" src="https://github.com/user-attachments/assets/9d5b499e-d75d-41fb-b105-e65f6afbd59e" />

</details>
