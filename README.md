© The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved.

# Explore different providers

This course is available for multiple cloud providers. Choose your preferred platform:

- [Hello Google Cloud](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-gcloud)
- [Hello Microsoft Azure](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-azure)
- [Hello Amazon Web Services](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws) (You are here) (⭐ Most popular)

# University workshop

A modified version of this course was offered as an in-person workshop to a cohort of researchers by the Competency Centre in 2025. 

Everyone has moved on to other projects within the university and new courses and support are now offered by [OxRSE](https://train.rse.ox.ac.uk/material/HPCu/cloud_computing).

# Instructions

<details>
<summary>Go to Amazon ECR / Private registry / Repositories and create a new repository called hello-aws</summary>

***
</details>
<details>
<summary>Go to Code Build / Build Project and create a new build project called hello-aws</summary>

***
</details>
<details>
<summary>Select GitHub/Public repository as the source, name the service role hello-aws-codebuild-role and tick "Use a buildspec file"</summary>

***
</details>
<details>
<summary>Click on the build project's service role / Add permissions / Attach policies and attach AmazonEC2ContainerRegistryPowerUser</summary>

***
</details>
<details>
<summary>Press Start build</summary>

***
</details>
<details>
<summary>Go to Amazon Elastic Container Service / Express Mode. Select the built image and set image selection to tag "latest"</summary>

***
</details>

The app should now be publicly accessible.

<img width="551" height="103" alt="img7" src="https://github.com/user-attachments/assets/08fbbdc2-2707-4491-b4c2-ebe7d7f1ff4b" />

***

# Going further

<details>
<summary><h2>Modifying the code</h2></summary>

If you select your private repository in Codebuild, then every commit will create a new image automatically. After that, you need to press "Update service" in ECS. 

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
<summary>Try to make the duck downloadable</summary>

Hint: if you choose to read it from the bucket, your instance needs a service role 

```bash
@app.route("/download/duck")
def download_duck():
    # something
```

</details>
