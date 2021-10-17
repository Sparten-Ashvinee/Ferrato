#Github Action

Add build_docker_image.yaml in .github/worflows folder

```
name: Create Docker Container

on: [push]

jobs:
  mlops-container:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./week_6_github_actions
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          ref: ${{ github.ref }}
      - name: Build container
        run: |
          docker network create data
          docker build --tag inference:latest .
          docker run -d -p 8000:8000 --network data --name inference_container inference:latest
```

```
Secret key in github for AWS
```

